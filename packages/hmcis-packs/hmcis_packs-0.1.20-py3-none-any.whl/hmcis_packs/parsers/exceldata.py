import hashlib
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
from typing import Union, Dict, List, Tuple, Optional

import pandas as pd
from pywintypes import com_error
from win32com.client import DispatchEx

from hmcis_packs.clean.cleaner import DataframeCleaner
from hmcis_packs.logger.logger_config import setup_logger

logger = setup_logger(__name__)


@dataclass
class WorkbookStructure:
    """Структура рабочей книги для сравнения."""
    sheet_names: Tuple[str, ...]  # Имена листов
    sheet_count: int  # Количество листов
    file_extension: str  # Расширение файла
    structure_hash: str = ""  # Хеш структуры для быстрого сравнения

    def __post_init__(self):
        # Генерируем хеш структуры для быстрого сравнения
        structure_data = f"{self.sheet_count}:{':'.join(sorted(self.sheet_names))}:{self.file_extension}"
        self.structure_hash = hashlib.md5(structure_data.encode()).hexdigest()[:8]

    def __eq__(self, other) -> bool:
        if not isinstance(other, WorkbookStructure):
            return False
        return self.structure_hash == other.structure_hash

    def __hash__(self) -> int:
        return hash(self.structure_hash)

    def is_similar_to(self, other: 'WorkbookStructure',
                      exact_match: bool = True,
                      ignore_sheet_order: bool = True) -> bool:
        """
        Проверяет схожесть структур.

        Args:
            other: Другая структура для сравнения
            exact_match: Точное совпадение имен листов
            ignore_sheet_order: Игнорировать порядок листов
        """
        if not isinstance(other, WorkbookStructure):
            return False

        # Быстрая проверка по хешу для точного совпадения
        if exact_match and ignore_sheet_order:
            return self == other

        # Проверка количества листов
        if self.sheet_count != other.sheet_count:
            return False

        # Проверка имен листов
        if exact_match:
            if ignore_sheet_order:
                return set(self.sheet_names) == set(other.sheet_names)
            else:
                return self.sheet_names == other.sheet_names

        # Частичное совпадение (можно расширить логику)
        return len(set(self.sheet_names) & set(other.sheet_names)) > 0


SheetInfo = namedtuple('SheetInfo', ['name', 'index', 'used_range', 'row_count', 'col_count'])


class ExcelParser:
    """
    Reads an Excel sheet via a fresh COM instance, cleans it, and returns a DataFrame.

    Parameters:
      filepath: path to the .xlsx file
      sheet: worksheet to read (1-based index or substring of name)
      index_value: row-label to use as index
      retain_duplicates: if False, will drop duplicate columns
      visible: if True, the Excel window pops up (default False)
    """

    def __init__(
            self,
            filepath: Union[str, Path],
            sheet: Union[str, int],
            index_value: str,
            *,
            retain_duplicates: bool = False,
            visible: bool = False,
    ) -> None:
        self.filepath = Path(filepath)
        self.sheet = sheet
        self.index_value = index_value
        self.retain_duplicates = retain_duplicates
        self.visible = visible
        self._app = None
        self._wb = None
        self._structure: Optional[WorkbookStructure] = None

    def __eq__(self, other) -> bool:
        """Сравнение экземпляров по структуре книги."""
        if not isinstance(other, ExcelParser):
            return False

        # Если структуры еще не определены, определяем их
        if self._structure is None:
            self.get_structure()
        if other._structure is None:
            other.get_structure()

        return self._structure == other._structure

    def __hash__(self) -> int:
        """Хеш для использования в множествах и словарях."""
        if self._structure is None:
            self.get_structure()
        return hash(self._structure)

    def __repr__(self) -> str:
        return f"ExcelParser('{self.filepath.name}', sheet={self.sheet})"

    def __enter__(self):
        """Вход в контекстный менеджер - открывает Excel и рабочую книгу."""
        logger.info("Entering ExcelParser context for: %s", self.filepath)

        # Создаем Excel приложение
        try:
            self._app = DispatchEx("Excel.Application")
            self._app.Visible = self.visible
            logger.info("Launched new Excel instance (HWND: %r)", getattr(self._app, "Hwnd", None))

            # Открываем рабочую книгу
            self._wb = self._app.Workbooks.Open(
                Filename=str(self.filepath),
                ReadOnly=True,
                UpdateLinks=0
            )
            logger.info(
                "Sheets count is %s %s",
                self._wb.Sheets.Count,
                [sht.Name for sht in self._wb.Sheets],
            )

            return self

        except com_error as e:
            logger.exception("Failed to open Excel/Workbook: %s", e)
            self._cleanup()
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Выход из контекстного менеджера - закрывает рабочую книгу и Excel."""
        logger.info("Exiting ExcelParser context")
        self._cleanup()

        if exc_type is not None:
            logger.error("Exception occurred in ExcelParser context: %s", exc_val)

        return False  # Не подавляем исключения

    def _cleanup(self):
        """Очистка ресурсов Excel."""
        if self._wb is not None:
            try:
                self._wb.Close(SaveChanges=False)
                logger.info("Closed workbook")
            except com_error as e:
                logger.warning("Error on Workbook.Close(): %s", e)
            finally:
                self._wb = None

        if self._app is not None:
            try:
                self._app.Quit()
                logger.info("Closed Excel instance")
            except com_error as e:
                logger.warning("Error on Excel.Quit(): %s", e)
            finally:
                self._app = None

    def _resolve_sheet(self, wb=None):
        """
        Возвращает COM-объект листа по 1-базному индексу или по подстроке в имени.
        """
        wb = wb or self._wb
        if wb is None:
            raise RuntimeError("Workbook is not open. Use within context manager or open_wb().")

        if isinstance(self.sheet, int):
            try:
                sht = wb.Sheets[self.sheet]  # 1-based
                logger.info("Resolved sheet by 1-based index: %s", sht.Name)
                return sht
            except com_error:
                raise ValueError(f"Sheet index {self.sheet} is out of range.")
        else:
            name_sub = str(self.sheet)
            matches = [sht for sht in wb.Sheets if name_sub in sht.Name]
            if not matches:
                raise ValueError(f"No sheet name containing '{name_sub}' found.")
            if len(matches) > 1:
                logger.warning(
                    "Multiple sheets matched '%s'; using the first: %s",
                    name_sub, matches[0].Name
                )
            logger.info("Resolved sheet by name: %s", matches[0].Name)
            return matches[0]

    def get_sheet(self):
        """Получить текущий лист (должен использоваться в контексте)."""
        if self._wb is None:
            raise RuntimeError("Workbook is not open. Use within context manager.")
        return self._resolve_sheet()

    def get_workbook(self):
        """Получить текущую рабочую книгу (должен использоваться в контексте)."""
        if self._wb is None:
            raise RuntimeError("Workbook is not open. Use within context manager.")
        return self._wb

    def get_structure(self, force_reload: bool = False) -> WorkbookStructure:
        """
        Получает структуру рабочей книги.

        Args:
            force_reload: Принудительно перезагрузить структуру
        """
        if self._structure is not None and not force_reload:
            return self._structure

        # Если книга уже открыта, используем ее
        if self._wb is not None:
            self._structure = self._extract_structure_from_wb(self._wb)
        else:
            # Быстро открываем книгу только для получения структуры
            with self as parser:
                self._structure = self._extract_structure_from_wb(parser._wb)

        logger.info("Extracted structure: %s sheets, hash=%s",
                    self._structure.sheet_count, self._structure.structure_hash)
        return self._structure

    def _extract_structure_from_wb(self, wb) -> WorkbookStructure:
        """Извлекает структуру из открытой рабочей книги."""
        sheet_names = tuple(sheet.Name for sheet in wb.Sheets)
        sheet_count = wb.Sheets.Count
        file_extension = self.filepath.suffix.lower()

        return WorkbookStructure(
            sheet_names=sheet_names,
            sheet_count=sheet_count,
            file_extension=file_extension
        )

    def get_detailed_sheet_info(self) -> List[SheetInfo]:
        """Получает подробную информацию о каждом листе."""
        if self._wb is None:
            with self as parser:
                return parser._get_detailed_info_from_wb()
        else:
            return self._get_detailed_info_from_wb()

    def _get_detailed_info_from_wb(self) -> List[SheetInfo]:
        """Извлекает подробную информацию о листах."""
        sheets_info = []

        for i, sheet in enumerate(self._wb.Sheets, 1):
            try:
                used_range = sheet.UsedRange
                if used_range:
                    row_count = used_range.Rows.Count
                    col_count = used_range.Columns.Count
                    range_address = used_range.Address
                else:
                    row_count = col_count = 0
                    range_address = "Empty"

                sheet_info = SheetInfo(
                    name=sheet.Name,
                    index=i,
                    used_range=range_address,
                    row_count=row_count,
                    col_count=col_count
                )
                sheets_info.append(sheet_info)

            except com_error as e:
                logger.warning("Error reading sheet %s: %s", sheet.Name, e)

        return sheets_info

    def is_similar_to(self, other: 'ExcelParser', **kwargs) -> bool:
        """
        Проверяет схожесть структур с другим экземпляром.

        Args:
            other: Другой экземпляр ExcelParser
            **kwargs: Параметры для is_similar_to метода WorkbookStructure
        """
        if not isinstance(other, ExcelParser):
            return False

        my_structure = self.get_structure()
        other_structure = other.get_structure()

        return my_structure.is_similar_to(other_structure, **kwargs)

    def compare_with(self, other: 'ExcelParser') -> Dict[str, any]:
        """
        Подробное сравнение с другим экземпляром.

        Returns:
            Словарь с результатами сравнения
        """
        if not isinstance(other, ExcelParser):
            return {"error": "Can only compare with another ExcelParser"}

        my_structure = self.get_structure()
        other_structure = other.get_structure()

        comparison = {
            "files": {
                "self": self.filepath.name,
                "other": other.filepath.name
            },
            "identical_structure": my_structure == other_structure,
            "structure_hashes": {
                "self": my_structure.structure_hash,
                "other": other_structure.structure_hash
            },
            "sheet_counts": {
                "self": my_structure.sheet_count,
                "other": other_structure.sheet_count,
                "match": my_structure.sheet_count == other_structure.sheet_count
            },
            "sheet_names": {
                "self": my_structure.sheet_names,
                "other": other_structure.sheet_names,
                "common": tuple(set(my_structure.sheet_names) & set(other_structure.sheet_names)),
                "unique_to_self": tuple(set(my_structure.sheet_names) - set(other_structure.sheet_names)),
                "unique_to_other": tuple(set(other_structure.sheet_names) - set(my_structure.sheet_names))
            },
            "extensions": {
                "self": my_structure.file_extension,
                "other": other_structure.file_extension,
                "match": my_structure.file_extension == other_structure.file_extension
            }
        }

        return comparison

    def read_data(self) -> pd.DataFrame:
        """Основной публичный метод: открыть Excel, выбрать лист, вернуть очищенный DataFrame."""
        # Если уже в контексте, используем открытую книгу
        if self._wb is not None:
            return self._read_data_from_open_wb()

        # Иначе открываем временно через контекстный менеджер
        with self as parser:
            return parser._read_data_from_open_wb()

    def _read_data_from_open_wb(self) -> pd.DataFrame:
        """Читает данные из уже открытой рабочей книги."""
        sheet = self._resolve_sheet()
        logger.info("Processing data on sheet -> %s", sheet.Name)
        return self._process_sheet_data(sheet)

    def _process_sheet_data(self, sheet) -> pd.DataFrame:
        """Обрабатывает данные с листа."""
        raw = sheet.UsedRange.Value  # tuple-of-tuples
        df = pd.DataFrame(raw)
        logger.info("Raw data shape: %s", df.shape)

        cleaner = DataframeCleaner(df)
        cleaner.adj_by_row_index(self.index_value)

        if not self.retain_duplicates:
            cleaner.remove_duplicated_cols()
            logger.info("Removed duplicated columns")

        logger.info("Final cleaned data shape: %s", cleaner.df.shape)
        return cleaner.df

    # Вспомогательные методы для внутреннего использования (больше не нужны как публичные)
    def _excel_app(self):
        """УДАЛЕНО - функциональность перенесена в __enter__/__exit__"""
        pass

    def _open_wb(self, app, *, readonly: bool = True, update_links: bool = False):
        """УДАЛЕНО - функциональность перенесена в __enter__/__exit__"""
        pass

    # Опционально: если нужно просто «временно открыть» книгу снаружи
    # УДАЛЕНО - теперь используем основной контекстный менеджер класса


if __name__ == "__main__":
    # Пример 1: Традиционное использование
    print("=== Традиционное использование ===")
    parser = ExcelParser(
        r"V:\Accounting\Work\Мерц\2025\2 квартал 2025\Июнь 2025\Отчетность\!Начисление МСФО_июнь 2025.xlsx",
        sheet='для IF загрузки',
        index_value="Отдел инициатор",
        retain_duplicates=False,
        visible=True,
    )
    df = parser.read_data()
    print(f"Результат: {df.shape}")

    # Пример 2: Использование как контекстный менеджер
    print("\n=== Использование как контекстный менеджер ===")
    with ExcelParser(
            r"V:\Accounting\Work\Мерц\2025\2 квартал 2025\Июнь 2025\Отчетность\!Начисление МСФО_июнь 2025.xlsx",
            sheet=3,
            index_value="Отдел инициатор",
            visible=True
    ) as parser:
        # Можно получить рабочую книгу и лист
        wb = parser.get_workbook()
        sheet = parser.get_sheet()
        logger.info("Работаем с книгой: %s, лист: %s", wb.Name, sheet.Name)

        # Или просто прочитать данные
        df = parser.read_data()
        print(f"Результат через контекстный менеджер: {df.shape}")

    print("=== Тест завершен ===")

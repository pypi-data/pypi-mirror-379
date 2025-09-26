import os
import asyncio
import tempfile

from google_sheets_telegram_utils.utils.connectors.csv_connector import CsvConnector
from google_sheets_telegram_utils.utils.configs.csv_config import CsvConfig
from google_sheets_telegram_utils.exceptions import RowDoesNotExistException


def _create_temp_csv_file(initial_contents: str = "") -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
    try:
        if initial_contents:
            tmp.write(initial_contents)
    finally:
        tmp.close()
    return tmp.name


def _cleanup_temp_file(path: str) -> None:
    if os.path.exists(path):
        os.unlink(path)


def test_add_rows_increments_ids_and_persists_rows():
    path = _create_temp_csv_file()
    try:
        connector = CsvConnector(CsvConfig(file=path))
        asyncio.run(connector.add_rows([
            ["alice"],
            ["bob"],
        ]))

        rows = asyncio.run(connector._read_fields_and_rows())
        assert rows == [["1", "alice"], ["2", "bob"]]
    finally:
        _cleanup_temp_file(path)


def test_get_row_by_id_found():
    path = _create_temp_csv_file()
    try:
        connector = CsvConnector(CsvConfig(file=path))
        asyncio.run(connector.add_rows([
            ["alice"],
            ["bob"],
            ["carol"],
        ]))

        row = asyncio.run(connector.get_row_by_id(2))
        assert row == {"id": 2, "value_1": "bob"}
    finally:
        _cleanup_temp_file(path)


def test_get_row_by_id_not_found_raises():
    path = _create_temp_csv_file()
    try:
        connector = CsvConnector(CsvConfig(file=path))
        asyncio.run(connector.add_rows([["alice"]]))
        try:
            asyncio.run(connector.get_row_by_id(99))
            assert False, "Expected RowDoesNotExistException"
        except RowDoesNotExistException:
            pass
    finally:
        _cleanup_temp_file(path)


def test_last_id_skips_header_and_handles_empty():
    # File with only header
    path_header_only = _create_temp_csv_file("id,name\n")
    try:
        connector = CsvConnector(CsvConfig(file=path_header_only))
        last_id = asyncio.run(connector._get_last_id())
        assert last_id == 0

        asyncio.run(connector.add_row(["alice"]))
        last_id_after = asyncio.run(connector._get_last_id())
        assert last_id_after == 1
    finally:
        _cleanup_temp_file(path_header_only)



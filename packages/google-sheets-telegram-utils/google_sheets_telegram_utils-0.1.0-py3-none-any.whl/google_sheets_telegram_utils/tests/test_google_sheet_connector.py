import asyncio
from unittest.mock import MagicMock, AsyncMock

from google_sheets_telegram_utils.utils.connectors.google_sheet_connector import GoogleSheetConnector
from google_sheets_telegram_utils.utils.configs.google_sheet_config import GoogleSheetConfig
from google_sheets_telegram_utils.exceptions import RowDoesNotExistException


def _build_connector_with_mocks(records=None, sheet_name='Users'):
    # Prepare fake worksheet and workbook
    worksheet = MagicMock()
    worksheet.get_all_records.return_value = records or []

    workbook = MagicMock()
    workbook.worksheet.return_value = worksheet

    # Patch GoogleSheetConnector._get_workbook to return our fake workbook
    connector = GoogleSheetConnector(
        GoogleSheetConfig(credentials_path='/tmp/creds.json', scope=[], file='File', sheet_name=sheet_name)
    )
    connector._get_workbook = AsyncMock(return_value=workbook)
    return connector, workbook, worksheet


def test_get_row_by_id_found():
    records = [
        {'id': 1, 'username': 'alice'},
        {'id': 2, 'username': 'bob'},
    ]
    connector, _, _ = _build_connector_with_mocks(records)

    row = asyncio.run(connector.get_row_by_id(2))
    assert row == {'id': 2, 'username': 'bob'}


def test_get_row_by_id_not_found_raises():
    records = [
        {'id': 1, 'username': 'alice'},
    ]
    connector, _, _ = _build_connector_with_mocks(records)

    try:
        asyncio.run(connector.get_row_by_id(5))
        assert False, 'Expected RowDoesNotExistException'
    except RowDoesNotExistException:
        pass


def test_add_rows_inserts_at_correct_position():
    # Existing 3 records → insert position should be len(records) + 2 = 5
    records = [
        {'id': 1, 'username': 'alice'},
        {'id': 2, 'username': 'bob'},
        {'id': 3, 'username': 'carol'},
    ]
    connector, workbook, worksheet = _build_connector_with_mocks(records)

    new_rows = [[4, 'dave'], [5, 'erin']]
    asyncio.run(connector.add_rows(new_rows))

    workbook.worksheet.assert_called_once()
    worksheet.get_all_records.assert_called_once()
    worksheet.insert_rows.assert_called_once_with(new_rows, 5, value_input_option='USER_ENTERED')



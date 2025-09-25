import gspread

from google_sheets_telegram_utils.exceptions import RowDoesNotExistException
from google_sheets_telegram_utils.utils.configs.google_sheet_config import GoogleSheetConfig
from google_sheets_telegram_utils.utils.connectors.abstract_connector import AbstractConnector


class GoogleSheetConnector(AbstractConnector):

    def __init__(self, config: GoogleSheetConfig):
        super().__init__(config)
        self.config = config

    async def get_data(self) -> list:
        workbook = await self._get_workbook()
        sheet = workbook.worksheet(self.config.sheet_name)
        data = sheet.get_all_records()
        return [self._coerce_record_types(row) for row in data]

    async def _get_workbook(self) -> gspread.spreadsheet.Spreadsheet:
        client = gspread.service_account(filename=self.config.credentials_path)
        sheet = client.open(self.config.file)
        return sheet

    async def add_rows(self, rows: list) -> None:
        workbook = await self._get_workbook()
        worksheet = workbook.worksheet(self.config.sheet_name)
        records = worksheet.get_all_records()
        insert_position = len(records) + 2
        worksheet.insert_rows(rows, insert_position, value_input_option='USER_ENTERED')

    async def add_row(self, row):
        return await self.add_rows([row])

    async def get_row_by_id(self, pk) -> dict:
        rows = await self.get_data()
        def _match(row):
            try:
                return int(row.get('id')) == int(pk)
            except (ValueError, TypeError):
                return False
        filtered_rows = list(filter(_match, rows))
        if filtered_rows:
            data = filtered_rows[0]
            return data
        raise RowDoesNotExistException

    def _coerce_record_types(self, record: dict) -> dict:
        coerced = dict(record)
        if 'id' in coerced:
            try:
                coerced['id'] = int(coerced['id'])
            except (ValueError, TypeError):
                pass
        for key in ('is_activated', 'is_bot'):
            if key in coerced:
                coerced[key] = self._to_bool(coerced[key])
        return coerced

    @staticmethod
    def _to_bool(value):
        if isinstance(value, bool):
            return value
        if value is None:
            return False
        s = str(value).strip().lower()
        return s in ('true', '1', 'yes', 'y')

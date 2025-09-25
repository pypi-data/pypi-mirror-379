import os
import csv
from google_sheets_telegram_utils.exceptions import RowDoesNotExistException
from google_sheets_telegram_utils.utils.configs.csv_config import CsvConfig
from google_sheets_telegram_utils.utils.connectors.abstract_connector import AbstractConnector


class CsvConnector(AbstractConnector):

    def __init__(self, config: CsvConfig):
        super().__init__(config)
        self.config = config

    def init_file(self):
        if not os.path.exists(self.config.file):
            with open(self.config.file, 'w'):
                ...

    async def get_data(self) -> list:
        rows = await self._read_fields_and_rows()
        if not rows:
            return []
        try:
            int(rows[0][0])
            has_header = False
        except (ValueError, TypeError, IndexError):
            has_header = True
        if has_header:
            header = rows[0]
            data_rows = rows[1:]
            result = []
            for r in data_rows:
                if not r:
                    continue
                item = {header[i]: r[i] if i < len(r) else '' for i in range(len(header))}
                result.append(self._coerce_record_types(item))
            return result
        result = []
        for r in rows:
            if not r:
                continue
            entry = {'id': r[0] if len(r) > 0 else ''}
            for i, value in enumerate(r[1:], start=1):
                entry[f'value_{i}'] = value
            result.append(self._coerce_record_types(entry))
        return result

    async def _read_fields_and_rows(self) -> list:
        rows = []
        with open(self.config.file) as csv_file:
            csvreader = csv.reader(csv_file)
            for row in csvreader:
                rows.append(row)
        return rows

    async def _get_last_id(self) -> int:
        data = await self._read_fields_and_rows()
        if not data:
            return 0
        for row in reversed(data):
            if not row:
                continue
            try:
                return int(row[0])
            except (ValueError, TypeError, IndexError):
                continue
        return 0

    async def add_rows(self, rows: list) -> None:
        new_id = await self._get_last_id() + 1
        with open(self.config.file, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in rows:
                csv_writer.writerow([new_id, *row])
                new_id += 1

    async def add_row(self, row) -> None:
        await self.add_rows([row])

    async def get_row_by_id(self, pk) -> dict:
        data = await self._read_fields_and_rows()
        if not data:
            raise RowDoesNotExistException

        header = None
        try:
            int(data[0][0])
        except (ValueError, TypeError, IndexError):
            header = data[0]
            rows_iterable = data[1:]
        else:
            rows_iterable = data

        str_pk = str(pk)
        for row in rows_iterable:
            if not row:
                continue
            if len(row) > 0 and str(row[0]) == str_pk:
                if header is not None:
                    item = {header[i]: row[i] if i < len(row) else '' for i in range(len(header))}
                    return self._coerce_record_types(item)
                result = {'id': row[0] if len(row) > 0 else ''}
                for i, value in enumerate(row[1:], start=1):
                    result[f'value_{i}'] = value
                return self._coerce_record_types(result)
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

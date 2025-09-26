google-sheets-telegram-utils
=============================

Utilities to integrate Telegram bots with Google Sheets (and CSV as a lightweight alternative).
Provides a simple connector abstraction, user helpers, and ready-to-use handler factory.


Features
--------

- Unified connector interface for CSV and Google Sheets
- Async-compatible handlers for python-telegram-bot v20+
- User model and ``active_user`` decorator to guard commands by registration/activation
- Typed, normalized outputs (``id`` as int, boolean fields as ``bool``)
- Tests for connectors (CSV and Google Sheets via mocks)


Installation
------------

Install from source (until published on PyPI)::

  pip install -e .

Runtime dependencies are declared in ``setup.py`` (``python-telegram-bot``, ``gspread``, etc.).


Quickstart (PTB v20)
--------------------

Minimal example using CSV as a backing store (see ``google_sheets_telegram_utils/presets/main_example.py``)::

  export TOKEN=123456:ABC-DEF
  python -m google_sheets_telegram_utils.presets.main_example

The example wires a ``CsvConnector`` and exposes commands:

- ``/start`` – hello message
- ``/hello`` – greets the user
- ``/register`` – registers the user in the storage (CSV or Google Sheets)


Using CSV connector
-------------------

Example snippet::

  from google_sheets_telegram_utils.utils.connectors.csv_connector import CsvConnector
  from google_sheets_telegram_utils.utils.configs.csv_config import CsvConfig

  connector = CsvConnector(CsvConfig(file='users.csv'))
  # get all data as list[dict]
  data = await connector.get_data()
  # add a row (without id; it will be auto-assigned)
  await connector.add_row(['username', 'first', 'last', 'en', 'false'])
  # fetch by id
  user = await connector.get_row_by_id(1)

Notes:

- If the CSV file contains a header row, it will be used for field names
- Without a header, fallback keys are: ``id``, ``value_1``, ``value_2``, ...
- ``id`` is normalized to ``int``; boolean-like fields (e.g. ``is_activated``, ``is_bot``) are normalized to ``bool``


Using Google Sheets connector
----------------------------

Credentials
~~~~~~~~~~~

Create a Google Cloud service account, grant access to the sheet, and download the JSON key file.

Config and usage::

  from google_sheets_telegram_utils.utils.connectors.google_sheet_connector import GoogleSheetConnector
  from google_sheets_telegram_utils.utils.configs.google_sheet_config import GoogleSheetConfig

  config = GoogleSheetConfig(
      credentials_path='service_account.json',
      scope=['https://www.googleapis.com/auth/spreadsheets'],
      file='Spreadsheet Name',
      sheet_name='Users',
  )
  connector = GoogleSheetConnector(config)
  users = await connector.get_data()
  await connector.add_row([123, 'username', 'first', 'last', 'en', False, True])
  user = await connector.get_row_by_id(123)

Under the hood the connector uses ``gspread.service_account`` and normalizes types similarly to the CSV connector.


Handler factory and decorator
----------------------------

- ``HandlerFactory.get_register_handler(connector)``: returns an async handler to register users
- ``active_user(connector)``: decorator to restrict commands to registered and activated users

Example::

  from google_sheets_telegram_utils.utils.active_user_decorator import active_user
  from google_sheets_telegram_utils.utils.factories.handlers_factory import HandlerFactory

  register_handler = HandlerFactory.get_register_handler(connector)

  @active_user(connector)
  async def secret(update, context):
      await update.message.reply_text('Top secret!')


Development
-----------

Run tests::

  pip install -r requirements-dev.txt  # optional if you maintain one
  pip install pytest
  pytest -q

Code style and typing (recommended)::

  pip install ruff mypy black
  ruff .
  mypy .
  black .


Release checklist
-----------------

1. Update ``README.rst`` and bump version in ``setup.py``
2. Build and upload::

     python -m pip install --upgrade build twine
     python -m build
     python -m twine upload dist/*


License
-------

BSD 2-Clause License. See ``LICENSE``.

from types import SimpleNamespace

from google_sheets_telegram_utils.utils.classes.telegram_user import TelegramUser


def test_from_telegram_user_maps_fields_and_defaults_activation_false():
    tg_user = SimpleNamespace(
        id=123,
        username='alice',
        first_name='Alice',
        last_name='Doe',
        language_code='en',
        is_bot=False,
    )

    user = TelegramUser.from_telegram_user(tg_user)  # type: ignore[arg-type]

    assert user.id == 123
    assert user.username == 'alice'
    assert user.first_name == 'Alice'
    assert user.last_name == 'Doe'
    assert user.language_code == 'en'
    assert user.is_bot is False
    # is_activated not provided -> False
    assert user.is_activated is False


def test_convert_to_list_serializes_booleans_and_activation():
    data = {
        'id': 5,
        'username': 'bob',
        'first_name': 'Bob',
        'last_name': 'Smith',
        'language_code': 'en',
        'is_bot': True,
        'is_activated': 'true',
    }
    user = TelegramUser(data)

    assert user.is_activated is True
    as_list = user.convert_to_list()
    assert as_list == [5, 'bob', 'Bob', 'Smith', 'en', True, 'TRUE']


def test_activation_parsing_handles_various_truthy_values():
    for val in ('TRUE', 'true', 'True'):
        u = TelegramUser({'id': 1, 'username': '', 'first_name': '', 'last_name': '', 'language_code': '', 'is_bot': False, 'is_activated': val})
        assert u.is_activated is True

    u = TelegramUser({'id': 1, 'username': '', 'first_name': '', 'last_name': '', 'language_code': '', 'is_bot': False})
    assert u.is_activated is False


def test_boolean_inputs_for_flags_are_parsed_correctly():
    u1 = TelegramUser({'id': 1, 'username': '', 'first_name': '', 'last_name': '', 'language_code': '', 'is_bot': True, 'is_activated': True})
    assert u1.is_bot is True
    assert u1.is_activated is True

    u2 = TelegramUser({'id': 1, 'username': '', 'first_name': '', 'last_name': '', 'language_code': '', 'is_bot': False, 'is_activated': False})
    assert u2.is_bot is False
    assert u2.is_activated is False


from koine_greek_converter.core.text_field import TextField

import pytest

@pytest.fixture
def text_field():
    text_field = TextField(initial_content='test')
    return text_field

def test_single_cursor_insert(text_field: TextField):
    text_field.selected_area = 3
    text_field.insert('x')
    assert text_field.content == 'tesxt'

def test_multiple_cursor_insert(text_field: TextField):
    text_field.selected_area = [0, 2, 3]
    text_field.insert('x')
    assert text_field.content == 'xtexsxt'

def test_multiple_cursor_insert_mixed_order(text_field: TextField):
    text_field.selected_area = [0, 3, 2]
    text_field.insert('x')
    assert text_field.content == 'xtexsxt'

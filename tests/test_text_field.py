from koine_greek_converter.core.text_field import TextField

import pytest

@pytest.fixture
def text_field():
    text_field = TextField(initial_content='test', selected_area=3)
    return text_field

def test_single_cursor_insert(text_field: TextField):
    text_field.insert('x')
    assert text_field.content == 'tesxt'

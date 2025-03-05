from koine_greek_converter.core.cursor import Cursor, AddCharacter, ReplacePreviousCharacter
from koine_greek_converter.core.cursorable import Cursorable

import pytest

@pytest.fixture
def cursor():
    cursorable = Cursorable('test')
    return Cursor(cursorable, initial_position=3)

def test_add_character(cursor):
    action = AddCharacter(cursor, 'x')
    cursor.perform(action)
    assert all([cursor.cursorable.content == 'tesxt',
                cursor.position == 4])
    
def test_replace_character(cursor):
    action = ReplacePreviousCharacter(cursor, 'x')
    cursor.perform(action)
    assert all([cursor.cursorable.content == 'text',
                cursor.position == 3])

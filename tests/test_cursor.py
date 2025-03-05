from koine_greek_transpiler.common.cursor import Cursor, AddCharacter
from koine_greek_transpiler.common.cursorable import Cursorable

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

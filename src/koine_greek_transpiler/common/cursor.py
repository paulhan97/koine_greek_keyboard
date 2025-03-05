from koine_greek_transpiler.common.cursorable import Cursorable

import abc


class CursorAction(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run():
        raise NotImplementedError


class Cursor:
    def __init__(self, cursorable: Cursorable, initial_position: int = 0):
        self.cursorable = cursorable
        self.position = initial_position

    def __repr__(self) -> str:
        return f'Cursor(cursorable = {self.cursorable}, position = {self.position})'

    @property
    def previous_character(self) -> str | None:
        if self.position == 0:
            return None
        else:
            return self.cursorable.content[self.position - 1]
    
    @property
    def next_character(self) -> str | None:
        if (self.position) == len(self.cursorable.content):
            return None
        else:
            next_character = self.cursorable.content[self.position - 1 : self.position]
            is_space = next_character == chr(32)
            return None if is_space else next_character
        
    def perform(self, action: CursorAction):
        action.run()

    def place_at(self, new_position: int):
        self.position = new_position

    def step(self):
        self.position += 1


class AddCharacter(CursorAction):
    def __init__(self, cursor: Cursor, character: str):
        if len(character) != 1:
            raise ValueError('A character must be a string of length 1')
        self.cursor = cursor
        self.character = character

    def __repr__(self) -> str:
        return f'AddCharacter(cursor = {self.cursor}, character = {self.character}) implements CursorAction'

    def run(self):
        self.cursor.cursorable.append_at(index = self.cursor.position,
                                         to_append = self.character)
        self.cursor.step()

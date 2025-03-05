import koine_greek_transpiler.common.utils as utils

class Cursorable:
    def __init__(self, initial_content: str = ''):
        self.content = initial_content

    def __repr__(self) -> str:
        return f'Cursorable(content = {self.content})'

    def append_at(self, index: int, to_append: str):
        self.content = utils.concat([self.content[:index],
                                      to_append,
                                      self.content[index:]])

    def replace_character_at(self, index: int, replace_with: str):
        self.content = utils.concat([self.content[:index],
                                     replace_with,
                                     self.content[index + 1]])

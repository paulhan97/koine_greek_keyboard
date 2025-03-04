class Cursor:
    def __init__(self, initial_position: int = 0, initial_text: str = ''):
        self.position = initial_position
        self.text = initial_text

    def place_at(self, new_position: int):
        self.position = new_position

    @property
    def previous_character(self) -> str | None:
        if self.position == 0:
            return None
        else:
            return self.text[self.position - 1 :]
    
    @property
    def next_character(self) -> str | None:
        if (self.position + 1) == len(self.text):
            return None
        else:
            next_character = self.text[self.position : self.position + 1]
            is_space = next_character == chr(32)
            return None if is_space else next_character

import koine_greek_converter.core.utils as utils

class TextField:
    def __init__(self,
                 initial_content: str = '',
                 selected_area: int | tuple | list[int | tuple] = 0):
        self.content = initial_content
        self.selected_area = selected_area

    def __repr__(self) -> str:
        return (f'TextField(content = {self.content})'
                f'selected_area = {self.selected_area}')

    def insert(self, insert_str: str):
        if isinstance(self.selected_area, int):
            single_cursor_point = self.selected_area
            self._insert_at(single_cursor_point, insert_str)
        elif utils.is_list_of_ints(self.selected_area):
            multiple_cursor_points = self.selected_area
            multiple_cursor_points.sort(reverse=True)
            for cursor_point in multiple_cursor_points:
                self._insert_at(cursor_point, insert_str)
        else:
            raise TypeError('The insert action should not be called when the selected area contains ranges. Please use the replace action instead')

    def _insert_at(self, index: int, insert_str: str):
        self.content = utils.concat([self.content[:index],
                                     insert_str,
                                     self.content[index:]])

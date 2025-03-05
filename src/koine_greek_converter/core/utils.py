def concat(str_list: list[str]):
    return ''.join(str_list)

def is_list_of_ints(candidate):
    return (isinstance(candidate, list)
            and all(isinstance(i, int) for i in candidate))

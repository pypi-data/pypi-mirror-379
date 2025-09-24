from typing import Union


def get_positive_index(index: Union[int, float], n: int) -> int:
    if isinstance(index, float):
        if 0 <= index <= 1:
            index = int((n - 1) * index + 0.5)
        else:
            raise ValueError(f"Index must be between -{n} and {n-1} or 0.0 and 1.0")

    if -n <= index < n:
        if index < 0:
            index += n
        return index
    else:
        raise ValueError(f"Index must be between -{n} and {n-1} or 0.0 and 1.0")

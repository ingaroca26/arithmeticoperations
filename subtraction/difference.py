def return_difference() -> int:
    minuend: int = 16
    subtrahend: int = 2
    difference: int = minuend - subtrahend
    return difference


def print_difference() -> None:
    difference: int = return_difference()
    f_difference: str = f'The difference is: {difference}.'
    print(f_difference)


if __name__ == '__main__':
    print_difference()

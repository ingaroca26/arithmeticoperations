def return_sum() -> int:
    first_summand: int = 16
    second_summand: int = 2
    sum: int = first_summand + second_summand
    return sum


def print_sum() -> None:
    sum: int = return_sum()
    f_sum: str = f'The sum is: {sum}.'
    print(f_sum)


if __name__ == '__main__':
    print_sum()

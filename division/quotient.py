def return_quotient() -> float:
    dividend: int = 16
    divisor: int = 2
    quotient: float = dividend / divisor
    return quotient


def print_quotient() -> None:
    quotient: float = return_quotient()
    f_quotient: str = f'The quotient is: {quotient}.'
    print(f_quotient)


if __name__ == '__main__':
    print_quotient()

def return_power() -> int:
    base: int = 16
    exponent: int = 2
    power: int = pow(base, exponent)
    return power


def print_power() -> None:
    power: int = return_power()
    f_power: str = f'The power is: {power}.'
    print(f_power)


if __name__ == '__main__':
    print_power()

def return_root() -> float:
    radicand: int = 16
    index: int = 2
    root: float = pow(radicand, 1 / index)
    return root


def print_root() -> None:
    root: float = return_root()
    f_root: str = f'The root is: {root}.'
    print(f_root)


if __name__ == '__main__':
    print_root()

def return_product() -> int:
    multiplicand: int = 16
    multiplier: int = 2
    product: int = multiplicand * multiplier
    return product


def print_product() -> None:
    product: int = return_product()
    f_product: str = f'The product is: {product}.'
    print(f_product)


if __name__ == '__main__':
    print_product()

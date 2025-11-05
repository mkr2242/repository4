"""Prime number checker utility."""

def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number.

    Args:
        n: Integer to evaluate.

    Returns:
        True if *n* is prime, otherwise False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main() -> None:
    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


if __name__ == "__main__":
    main()

"""
Fibonacci & Prime Hybrid
--------------------------
fibonacci(n)   -> returns a list of the first n Fibonacci numbers
is_prime(num)  -> returns True if num is prime, False otherwise
fib_primes(n)  -> returns only the prime numbers from the first n Fibonacci numbers
"""


def fibonacci(n):
    """Return a list of the first n Fibonacci numbers (starting 0, 1, 1, 2, 3, ...)."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)

    return fib_list


def is_prime(num):
    """Return True if num is a prime number, False otherwise."""
    # Primes are defined as integers greater than 1
    if num < 2:
        return False

    # Check for divisors from 2 up to the square root of num
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False  # found a divisor -> not prime

    return True  # no divisors found -> prime


def fib_primes(n):
    """Return only the prime numbers from the first n Fibonacci numbers."""
    fib_sequence = fibonacci(n)  # function calling function
    primes = []

    for num in fib_sequence:
        if is_prime(num):
            primes.append(num)

    return primes


def main():
    print("=== Fibonacci & Prime Hybrid ===\n")

    while True:
        user_input = input("Enter how many Fibonacci terms to generate (or press Enter to quit): ").strip()
        if user_input == "":
            print("Goodbye!")
            break

        try:
            n = int(user_input)
            if n < 0:
                print("Please enter a non-negative number.\n")
                continue
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        fib_sequence = fibonacci(n)
        primes = fib_primes(n)

        print(f"\nFirst {n} Fibonacci numbers: {fib_sequence}")
        print(f"Prime numbers among them:    {primes}\n")


if __name__ == "__main__":
    main()

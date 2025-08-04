"""
Day 7, Homework: Prime Number Tools

Purpose: Create functions to check if a number is prime and find the next prime.
We use functions to determine primality and search for the next prime number.

Expected output when run:
Enter a number: [user types number]
Is [number] prime? [True/False]
The next prime after [number] is [next prime]
"""

def is_prime(n):
    """Check if a number is prime.
    
    Args:
        n: The number to check
    
    Returns:
        True if n is prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisors from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def next_prime(n):
    """Find the next prime number after n.
    
    Args:
        n: The starting number
    
    Returns:
        The next prime number after n
    """
    # Start checking from n+1
    candidate = n + 1
    
    # Keep checking until we find a prime
    while not is_prime(candidate):
        candidate = candidate + 1
    
    return candidate


def main():
    """Get number from user and check if prime, then find next prime."""
    # Get the number from the user
    number_input = input("Enter a number: ")
    number = int(number_input)
    
    # Check if the number is prime
    prime_check = is_prime(number)
    
    # Find the next prime
    next_p = next_prime(number)
    
    # Display the results
    print(f"Is {number} prime? {prime_check}")
    print(f"The next prime after {number} is {next_p}")


if __name__ == "__main__":
    main()

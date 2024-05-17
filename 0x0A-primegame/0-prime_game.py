#!/usr/bin/python3
""" Prime game module """


def sieve(n):
    """ Generate a list of primes up to n using the Sieve of Eratosthenes """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """ this method solves for the winner """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    def play_game(n):
        """ this inner method starts the game """
        nonlocal primes
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            # Find the first prime that is still in the remaining set
            move = None
            for prime in primes:
                if prime in remaining:
                    move = prime
                    break
            if move is None:  # No more moves possible
                return turn ^ 1  # Return the loser, who is the current player
            # Remove the prime and its multiples
            to_remove = set(range(move, n + 1, move))
            remaining -= to_remove
            turn ^= 1  # Switch turns

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            # If n is 1, Ben automatically wins since Maria can't move
            ben_wins += 1
        else:
            winner = play_game(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

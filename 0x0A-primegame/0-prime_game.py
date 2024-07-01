#!/usr/bin/python3
"""Prime Game interview question"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """

    if not x or not nums:
        return None

    def is_prime(num):
        """Checks if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Initialize available numbers for this round
        available_numbers = set(range(1, n + 1))
        current_player = "Maria"

        while available_numbers:
            valid_choices = [num for num in available_numbers if is_prime(num)]
            if not valid_choices:
                break

            # Current player selects the smallest prime number
            play_number = min(valid_choices)
            available_numbers -= set(range(play_number, n + 1, play_number))

            # Switch players
            current_player = "Ben" if current_player == "Maria" else "Maria"

        # Update wins
        if current_player == "Ben":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

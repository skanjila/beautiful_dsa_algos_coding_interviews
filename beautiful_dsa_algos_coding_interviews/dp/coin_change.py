from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Return the fewest number of coins needed to make ``amount``.

    This is a classic bottom-up dynamic programming problem where
    ``dp[x]`` stores the minimum number of coins required to form value ``x``.

    Time complexity: O(amount * len(coins)) because each amount from 1 through
    the target tries every coin denomination once.
    Space complexity: O(amount) because the DP array stores one best answer per
    intermediate amount.
    """

    if amount == 0:
        return 0
    if not coins:
        return -1

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                # If we take this coin last, the rest of the amount has already
                # been solved in ``dp[value - coin]``.
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1

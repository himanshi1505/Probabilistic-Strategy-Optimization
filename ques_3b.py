MOD = 1000000007

def mod_add(a, b):
    """Addition under modulo."""
    return ((a % MOD + b % MOD) % MOD + MOD) % MOD

def mod_multiply(a, b):
    """Multiplication under modulo."""
    return ((a % MOD) * (b % MOD)) % MOD

def mod_inverse(b):
    """Modular inverse using Fermat's little theorem."""
    return pow(b, MOD - 2, MOD)

def mod_divide(a, b):
    """Division under modulo using the modular inverse."""
    return mod_multiply(a, mod_inverse(b))

# Revised optimal strategy function
def optimal_strategy(na, nb, total_rounds):
    max_points = exp_points(na, nb, total_rounds)
    
    # Determine which strategy yields the maximum points
    if dp[total_rounds][int(na * 2)][int(nb * 2)][0] == max_points:
        return [1, 0, 0]  # Aggressive strategy
    elif dp[total_rounds][int(na * 2)][int(nb * 2)][1] == max_points:
        return [0, 1, 0]  # Balanced strategy
    else:
        return [0, 0, 1]  # Defensive strategy
        

# Compute expected points based on the number of rounds left
def exp_points(a, b, remaining_rounds):
    if dp[remaining_rounds][int(a * 2)][int(b * 2)][0] is not None:
        return max(dp[remaining_rounds][int(a * 2)][int(b * 2)])  # Return cached result
    
    if remaining_rounds == 0:
        return 0  # No rounds left, no points to calculate
    
    dp[remaining_rounds][int(a * 2)][int(b * 2)][0] = 0
    dp[remaining_rounds][int(a * 2)][int(b * 2)][0] += (
        (exp_points(a + 1, b, remaining_rounds - 1) + 1) * (b / (a + b) + 0.7 + 5 / 11) / 3
    )
    dp[remaining_rounds][int(a * 2)][int(b * 2)][0] += exp_points(a + 0.5, b + 0.5, remaining_rounds - 1) * 0
    dp[remaining_rounds][int(a * 2)][int(b * 2)][0] += (
        exp_points(a, b + 1, remaining_rounds - 1) * (a / (a + b) + 0.3 + 6 / 11) / 3
    )

    dp[remaining_rounds][int(a * 2)][int(b * 2)][1] = 0
    dp[remaining_rounds][int(a * 2)][int(b * 2)][1] += (
        (exp_points(a + 1, b, remaining_rounds - 1) + 1) * (0.3 + 1 / 3 + 0.3) / 3
    )
    dp[remaining_rounds][int(a * 2)][int(b * 2)][1] += (
        exp_points(a + 0.5, b + 0.5, remaining_rounds - 1) + 0.5) * (1 / 3 + 1 / 2) / 3
    dp[remaining_rounds][int(a * 2)][int(b * 2)][1] += (
        exp_points(a, b + 1, remaining_rounds - 1) * (0.7 + 1 / 3 + 0.2) / 3
    )
    
    dp[remaining_rounds][int(a * 2)][int(b * 2)][2] = 0
    dp[remaining_rounds][int(a * 2)][int(b * 2)][2] += (
        (exp_points(a + 1, b, remaining_rounds - 1) + 1) * (6 / 11 + 0.2 + 0.1) / 3
    )
    dp[remaining_rounds][int(a * 2)][int(b * 2)][2] += (
        (exp_points(a + 0.5, b + 0.5, remaining_rounds - 1) + 0.5) * (0.5 + 0.8) / 3
    )
    dp[remaining_rounds][int(a * 2)][int(b * 2)][2] += (
        exp_points(a, b + 1, remaining_rounds - 1) * (5 / 11 + 0.3 + 0.1) / 3
    )
    
    return max(dp[remaining_rounds][int(a * 2)][int(b * 2)])

# Wrapper function to calculate the total expected points
def expected_points(total_rounds):
    # Clear the dp table
    # dp = [[[None for _ in range(3)] for _ in range(200)] for _ in range(200)]
    # for i in range(200):
    #     for j in range(200):
    #         for 
    
    # Start computation from the initial state
    return 1 + exp_points(1, 1, total_rounds - 2)

# Initialize a global dp table for memoization
dp = [[[[None for _ in range(3)] for _ in range(60)] for _ in range(60)] for _ in range(50)]

# Main execution logic
if __name__ == "__main__":
    # Example: total rounds = 4
    print(expected_points(6))

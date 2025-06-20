"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    global dp 
    return dp[alice_wins][bob_wins]
    pass
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    global dp 
    exp=0
    #derived formula in theory
    for i in range (1,t) : 
        exp = mod_add(exp, mod_multiply( mod_add(mod_multiply(2,i),-t) , dp[i][t-i]))

    return exp
    pass

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    
    global dp 

    variance = 0  
    
    #i--alice wins i matches, j--alice loses i matches
    for i in range (1,t) : 
        j = t-i 
        ij = mod_add(i,-j)
        #var=E(X^2)-(E(X))^2
        #since expectation is always 0 because dp[i][j]=dp[j][i] always, so var=E(X^2)

        variance = mod_add(variance , mod_multiply(dp[i][j] , mod_multiply(ij,ij)))
    

    return variance
    pass




# calculating and storing dp[i][j] as global variable
#T1T2+T3T4 can be maximum 198 
T = 200
dp = [[0 for x in range(T)] for y in range(T)]

# Base case-- dp[1][1] = 1, given in question
dp[1][1] = 1

# dp[i][j]--prob that alice wins i matches and bob wins j matches
for i in range(1, T):
    for j in range(1, T):
        if i + 1 < T:
            probability = mod_divide(j, i + j)
            dp[i+1][j] = mod_add(
                dp[i+1][j],
                mod_multiply(dp[i][j], probability)
            )
        
        if j + 1 < T:
            probability = mod_divide(i, i + j)
            dp[i][j+1] = mod_add(
                dp[i][j+1],
                mod_multiply(dp[i][j], probability)
            )


   




# Main execution
if __name__ == "__main__":
    
    T1T2 = 98 
    T3T4 = 88
    probability=calc_prob(T1T2,T3T4) 
    print(f"Probability that after 186 rounds, Alice wins 98 matches and Bob wins 88 matches: {probability}")
    expectation = calc_expectation(T3T4)
    variance = calc_variance(T3T4)
    print(f"Expected value after 88 rounds: {expectation}")
    print(f"Variance after 88 rounds: {variance}")
    pass
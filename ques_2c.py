import random

class Alice:
    def __init__(self):
        # self.past_play_styles = np.array([1,1])  
        # self.results = np.array([14,0])           
        # self.opp_play_styles = np.array([1,1])  
        # self.points = 1
        self.past_play_styles = [1,1]
        self.results = [1,0]           
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        # result=1 alice won, 0.5- draw, 0 alice lost

        if self.results[-1]==0:  # Bob won last time so bob plays defence
            return 1  # alice should play balanced
        
        elif self.results[-1]==0.5:  # draw last time so bob plays balanced
            return 0  #  alice should play attack
        
        else:# Bob lost last time so bob plays attack
            defence = 6 / 11 
            attack = 1 - (self.points / len(self.results))
            #if prob of winning of alice while playing defence> prob of winning while playing attack then play defence else play attack
            if defence > attack:
                return 2
            else:
                return 0
        
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        # self.past_play_styles = np.append(self.past_play_styles, own_style)
        # self.results = np.append(self.results, result)
        # self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        # self.points += result
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        # self.past_play_styles = np.array([1,1])  
        # self.results = np.array([0,1])           
        # self.opp_play_styles = np.array([1,1])  
        # self.points = 1
        self.past_play_styles =[1,1]
        self.results = [0,1]       
        self.opp_play_styles = [1,1]   
        self.points = 1
 


    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        # self.past_play_styles = np.append(self.past_play_styles, own_style)
        # self.results = np.append(self.results, result)
        # self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        # self.points += result
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    p=payoff_matrix[alice_move][bob_move]
    outcome = random.choices([1, 0.5, 0],weights= p)[0]

    #updating results of alice and bob
    alice.observe_result(alice_move, bob_move, outcome)
    bob.observe_result(bob_move, alice_move, 1-outcome)

    # Updating payoff matrix for attack-attack case
    total_points= alice.points + bob.points
    a=bob.points/total_points
    b=alice.points/total_points
    payoff_matrix[0][0] = (a,0,b) 
    pass

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    payoff_matrix = [
        [(0.5,0,0.5), (0.7, 0, 0.3), (5/11, 0, 6/11)],
        [(0.3, 0, 0.7), (1/3, 1/3, 1/3), (0.3, 0.5, 0.2)],
        [(6/11, 0, 5/11), (0.2, 0.5, 0.3), (0.1, 0.8, 0.1)]
    ]
    
    total_rounds = 0  # total rounds in all simulations
    simulations = 0    # total no. of simulations
    
    for _ in range(100000):  
        alice = Alice()
        bob = Bob()
        rounds = 0 # no. of rounds it took Alice for T wins in 1 monte carlo simulation 
        alice_wins = 0  # no. of Alice's wins in 1 monte carlo simulation 

        # Simulate rounds until Alice gets T wins
        while alice_wins < T:
            #ap_before-- alice points before running the round
            ap_before = alice.points

        
            simulate_round(alice, bob, payoff_matrix)

           #ap_after-- alice points after running the round
            ap_after = alice.points

            # Alice won the round if her points have increased by 1, so comparing points
            if ap_after== ap_before+1:
                alice_wins += 1  

            rounds += 1
        #keeping track of total rounds and simulations
        total_rounds += rounds
        simulations += 1

    # Returning the average number of rounds it took for Alice to reach T wins
    return total_rounds / simulations
    pass
if __name__ == "__main__":
    T3T4 = 88  
    
    
    estimated_tau = estimate_tau(T3T4)
    
    print(f"\nThe expected number of rounds for Alice to win {T3T4} times: {estimated_tau}")
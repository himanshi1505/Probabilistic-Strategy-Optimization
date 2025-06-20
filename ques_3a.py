import random



class Alice:
    def __init__(self):
        # self.past_play_styles = np.array([1,1])  
        # self.results = np.array([1,0])           
        # self.opp_play_styles = np.array([1,1])  
        # self.points = 1
        self.past_play_styles = [1,1]
        self.results = [1,0]           
        self.opp_play_styles = [1,1]
        self.points = 1


    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        
        
        na=self.points
        nb=len(self.results)-na
        k=nb/(na+nb) 
        
        #k--attack
        if (k > 0.34091):
            return 0
        else:
            return 2
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
        pass

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
        move = random.choice([0, 1, 2])
        return move
        
        
    
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
    
    
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    payoff_matrix = [
        [(0.5,0,0.5), (0.7, 0, 0.3), (5/11, 0, 6/11)],
        [(0.3, 0, 0.7), (1/3, 1/3, 1/3), (0.3, 0.5, 0.2)],
        [(6/11, 0, 5/11), (0.2, 0.5, 0.3), (0.1, 0.8, 0.1)]
    ]
    
    
    
    alice = Alice()
    bob = Bob()
    
    for i in range(num_rounds):
        simulate_round(alice, bob,payoff_matrix)
    print(f"Average points of Alice after {num_rounds} games: {alice.points}")
    print(f"Average points of Alice after {num_rounds} games: {bob.points}")
    
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=100000)
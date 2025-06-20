import numpy as np

class Alice:
    def _init_(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. If you think there is no better strategy than 2a,
        then implement the same strategy here. Else implement that non greedy strategy here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if (len(self.results) == 2):
            return 2
        else:
            if self.results[-1] == 0:
                return 1
            elif self.results[-1] == 0.5:
                return 0
            else:
                x = len(self.results)
                z = (x-self.points)/x
                if z > 6 /11:
                    return 0
                else:
                    return 2
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result
       

class Bob:
    def _init_(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
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
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    x = alice.play_move()
    y = bob.play_move()
    z = payoff_matrix[x,y]
    prob = np.random.uniform(0, 1)
    if (prob <= z[0]):
        result_alice = 1
        result_bob = 0
        alice.observe_result(x, y, result_alice)
        bob.observe_result(y, x, result_bob)
    elif (prob <= z[0] + z[1]):
        result_alice = 0.5
        result_bob = 0.5
        alice.observe_result(x, y, result_alice)
        bob.observe_result(y, x, result_bob)
    else:
        result_alice = 0
        result_bob = 1
        alice.observe_result(x, y, result_alice)
        bob.observe_result(y, x, result_bob)
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    rounds = 0
    a = 0
    b = 0
    while (rounds < num_rounds):
        payoff_matrix = np.array(
            [
                [(1/2, 0, 1/2), (7 / 10, 0, 3 / 10), (5 / 11, 0, 6 / 11)],
                [(3 / 10, 0, 7 / 10), (1 / 3, 1 / 3, 1 / 3), (3 / 10, 1 / 2, 1 / 5)],
                [(6 / 11, 0, 5 / 11), (1 / 5, 1 / 2, 3 / 10), (1 / 10, 4 / 5, 1 / 10)],
            ]
        )
        alice = Alice()
        bob = Bob()
        for i in range(3):
            simulate_round(alice, bob, payoff_matrix)
            x = alice.points
            y = bob.points
            payoff_matrix = np.array(
                [
                    [(x/(x+y), 0, y/(x+y)), (7 / 10, 0, 3 / 10), (5 / 11, 0, 6 / 11)],
                    [(3 / 10, 0, 7 / 10), (1 / 3, 1 / 3, 1 / 3), (3 / 10, 1 / 2, 1 / 5)],
                    [(6 / 11, 0, 5 / 11), (1 / 5, 1 / 2, 3 / 10), (1 / 10, 4 / 5, 1 / 10)],
                ]
            )
            a += x
            b += y 
    print(a)
    print(b)
 

# Run Monte Carlo simulation with a specified number of rounds
if _name_ == "_main_":
    monte_carlo(num_rounds=10^5)
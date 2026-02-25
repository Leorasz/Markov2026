import numpy as np

def gambler_retirement_simulation(num_simulations=100_000, 
                                  initial_money=10, 
                                  p_win=0.35, 
                                  q_lose=0.4, 
                                  s_retire=0.25):

    final_amounts = np.zeros(num_simulations, dtype=float)
    
    for sim in range(num_simulations):
        money = initial_money
        while money > 0:
            r = np.random.rand()
            if r < s_retire:
                final_amounts[sim] = money
                break
            elif r < s_retire + p_win:
                money += 1
            else:
                money -= 1
        
    return np.mean(final_amounts)

average_final = gambler_retirement_simulation()
print(f"Average final amount over {100_000:,} simulations: {average_final:.5f}")

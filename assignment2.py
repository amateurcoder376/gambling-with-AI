import gymnasium as gym
import numpy as np
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)
env = env.unwrapped
mdp = env.P
init_state = env.reset()
goal_state = 15
LEFT, DOWN, RIGHT, UP = range(4)
pi = {
    0:RIGHT, 1:RIGHT, 2:DOWN, 3:LEFT,
    4:DOWN, 5:LEFT, 6:DOWN, 7:LEFT,
    8:RIGHT, 9:RIGHT, 10:DOWN, 11:LEFT,
    12:LEFT, 13:RIGHT, 14:RIGHT, 15:LEFT
}
val = dict()
for state in mdp:
    val[state] = np.random.random()

# Since 5, 7, 11, 12 and 15 are terminal states, we know their values are 0

val[5] = 0
val[7] = 0
val[11] = 0
val[12] = 0
val[15] = 0

def get_new_value_fn(val, mdp, pi, gamma = 1.0):
    
    new_val = dict()
    for s in mdp:
        new_val[s]=0
        for prob,next_state,reward,terminated in mdp[s][pi[s]]:
            new_val[s]+=prob*(reward+gamma*val[next_state])
    return new_val

def policy_evaluation(val, mdp, pi, epsilon=1e-10, gamma=1.0):
    count = 0
    while True:
        prev_val=val
        val = get_new_value_fn(prev_val,mdp,pi,gamma)
        temp=dict()
        temp[count]=val[count]-prev_val[count]
        if temp[count]<0 :
            temp[count]*=-1
        if temp[count]<epsilon :
            break
        count+=1
    return val, count 

def policy_improvement(val, mdp, pi, gamma=1.0):
    new_pi = dict()
    q = dict()
    for s in mdp:
        q[s]=dict()
        for a in mdp[s]:
            q[s][a]=0
            for prob,next_state,reward,terminated in mdp[s][a]:
                q[s][a]+=prob*(reward+gamma*val[next_state])
        new_pi[s]=max(q[s], key = lambda key:q[s][key])
    return new_pi, q

def policy_iteration(mdp, epsilon=1e-10, gamma=1.0):
    pi = dict()
    val = dict()
    count = 0
    pi = {
    0:RIGHT, 1:RIGHT, 2:DOWN, 3:LEFT,
    4:DOWN, 5:LEFT, 6:DOWN, 7:LEFT,
    8:RIGHT, 9:RIGHT, 10:DOWN, 11:LEFT,
    12:LEFT, 13:RIGHT, 14:RIGHT, 15:LEFT
    }   
    for state in mdp:
        val[state] = np.random.random()
    val[5] = 0
    val[7] = 0
    val[11] = 0
    val[12] = 0
    val[15] = 0
    while True :
        prev_pi=pi
        val=policy_evaluation(val,mdp,pi,epsilon,gamma)
        pi=policy_improvement(val,mdp,prev_pi,gamma)
        count+=1
        if prev_pi==pi :
            break
    return pi, val, count

def value_iteration(mdp, gamma=1.0, epsilon=1e-10):
    val = {s: 0 for s in mdp}
    count = 0
    q = dict()
    while True :
        for s in mdp:
            q[s]=dict()
            for a in mdp[s]:
                q[s][a]=0
                for prob,next_state,reward,terminated in mdp[s][a]:
                    q[s][a]+=prob*(reward+gamma*val[next_state])
            temp=dict()
            temp[s]=max(q[s],key =lambda key:q[s][key])-val[s]
            if temp[s]<0:
                temp[s]*=-1
        if max(temp,key =lambda key:temp[key])<epsilon:
            break
        val=max(q[s],key =lambda key:q[s][key])
    pi = {s: max(q[s], key=q[s].get) for s in mdp}
    return pi, val, count

def print_policy(policy, env):
    """
    Prints the policy for the 4x4 FrozenLake environment in a grid layout.
    """
    action_symbols = {0: '←', 1: '↓', 2: '→', 3: '↑'}  #action symbols
    grid_size = env.desc.shape  #get the grid dimensions (e.g., 4x4)
    
    policy_symbols = np.array([action_symbols[action] for cell,action in policy.items()])
    policy_grid = policy_symbols.reshape(grid_size)  #reshape into a grid

    print("Policy Grid:")
    for row in policy_grid:
        print(" ".join(row))


pi1, val1, count1 = policy_iteration(mdp)
pi2, val2, count2 = value_iteration(mdp)

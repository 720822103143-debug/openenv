import random

Q = {}

def get_state_key(state):
    return tuple(state)

def choose_action(state, actions, epsilon=0.2):
    # exploration
    if random.random() < epsilon:
        return random.choice(actions)

    state_key = get_state_key(state)

    # exploitation
    best_action = actions[0]
    best_value = -1e9

    for a in actions:
        val = Q.get((state_key, tuple(a)), 0)
        if val > best_value:
            best_value = val
            best_action = a

    return best_action


def update_q(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    state_key = get_state_key(state)
    next_key = get_state_key(next_state)

    current = Q.get((state_key, tuple(action)), 0)

    # future reward estimate
    future = 0

    Q[(state_key, tuple(action))] = current + alpha * (reward + gamma * future - current)
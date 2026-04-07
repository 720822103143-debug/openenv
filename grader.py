def evaluate(total_reward, max_possible_reward):
    score = total_reward / max_possible_reward

    # normalize between 0 and 1
    if score > 1:
        score = 1.0
    if score < 0:
        score = 0.0

    return round(score, 2)
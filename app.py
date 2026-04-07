from agent import choose_action, update_q
from fastapi import FastAPI
from env.scheduler_env import TaskSchedulerEnv
from tasks import EASY, MEDIUM, HARD
from grader import evaluate

app = FastAPI()

def greedy_policy(pending):
    return [job["id"] for job in sorted(pending, key=lambda x: -x["priority"])[:2]]
    
def run_task(task):
    env = TaskSchedulerEnv(task)
    state = env.reset()

    total_reward = 0
    done = False

    while not done:
        pending = state["pending_jobs"]

        if not pending:
            break

        # state representation
        curr_state = [(j["priority"], j["duration"]) for j in pending[:3]]

        # possible actions
        actions = []

        if len(pending) >= 2:
            actions.append([pending[0]["id"], pending[1]["id"]])
            actions.append([pending[-1]["id"], pending[-2]["id"]])
        else:
            actions.append([pending[0]["id"]])

        # RL choose action
        action_ids = choose_action(curr_state, actions)

        action = {"assign_job_ids": action_ids}

        next_state, reward, done, _ = env.step(action)

        next_pending = next_state["pending_jobs"]
        next_state_repr = [(j["priority"], j["duration"]) for j in next_pending[:3]]

        # update Q
        update_q(curr_state, action_ids, reward, next_state_repr)

        state = next_state
        total_reward += reward

    max_reward = sum(job["priority"] * 3 for job in task)
    score = evaluate(total_reward, max_reward)
    
    from agent import Q
    print("Q-table size:", len(Q))

    return {
        "reward": total_reward,
        "score": float(score)
    }

# ✅ ROOT ROUTE (THIS FIXES 404)
@app.get("/")
def home():
    return {"status": "RUNNING ✅"}


# ✅ RUN ROUTE
@app.get("/run")
def run_all():
    return {
        "easy": run_task(EASY),
        "medium": run_task(MEDIUM),
        "hard": run_task(HARD),
    }
class TaskSchedulerEnv:
    def __init__(self, jobs=None):
        self.initial_jobs = jobs
        self.reset()

    def reset(self):
        self.time = 0
        self.cpu_limit = 2

        if self.initial_jobs:
            from copy import deepcopy
            self.pending_jobs = deepcopy(self.initial_jobs)
        else:
            self.pending_jobs = [
                {"id": 1, "duration": 3, "priority": 1},
                {"id": 2, "duration": 2, "priority": 2},
            ]

        self.running_jobs = []
        self.completed_jobs = []

        return self.state()

    def state(self):
        return {
            "time": self.time,
            "cpu_available": self.cpu_limit - len(self.running_jobs),
            "pending_jobs": self.pending_jobs,
            "running_jobs": self.running_jobs,
        }

    def step(self, action):
        reward = 0

        # assign jobs
        for job_id in action.get("assign_job_ids", []):
            for job in self.pending_jobs:
                if job["id"] == job_id and len(self.running_jobs) < self.cpu_limit:
                    self.running_jobs.append(job)
                    self.pending_jobs.remove(job)
                    break

        # process jobs
        finished = []
        for job in self.running_jobs:
            job["duration"] -= 1
            if job["duration"] <= 0:
                finished.append(job)

        for job in finished:
            self.running_jobs.remove(job)
            self.completed_jobs.append(job)
            reward += 2 + job["priority"]

        # penalty
        reward -= 0.1 * len(self.pending_jobs)

        self.time += 1

        done = len(self.pending_jobs) == 0 and len(self.running_jobs) == 0

        return self.state(), reward, done, {}
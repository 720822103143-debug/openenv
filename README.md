# openenv
Built a real-world task scheduling environment using OpenEnv standards. Implemented a Q-learning agent to optimize CPU job execution based on priority and duration. Deployed an interactive RL dashboard using Gradio on Hugging Face Spaces for live simulation and evaluation.
---
CPU task scheduling RL environment
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

Task Scheduler RL Environment

This project simulates CPU task scheduling using a Reinforcement Learning environment.

Features:
- Priority-based job scheduling
- EASY, MEDIUM, HARD task sets
- Reward-based evaluation system
- FastAPI deployment on Hugging Face Spaces

Endpoints:
- `/` → Status check
- `/run` → Runs all tasks and returns scores

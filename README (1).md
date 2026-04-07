---
title: Task Scheduler Env
emoji: 🔥
colorFrom: gray
colorTo: yellow
sdk: docker
pinned: false
license: mit
short_description: CPU task scheduling RL environment
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
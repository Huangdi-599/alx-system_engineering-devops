#!/usr/bin/python3
# """Returns to-do list information for all employees."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_tasks = {}
    for user in users:
        tasks = requests.get(url + "todos", params={"userId": user.get("id")}).json()
        user_tasks = []
        for task in tasks:
            user_tasks.append({"username": user.get("username"),
                                "task": task.get("title"),
                                "completed": task.get("completed")})
        all_tasks[user.get("id")] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


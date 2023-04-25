#!/usr/bin/python3
# """Returns to-do list information for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employers = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = []
    for task in tasks:
        completed_tasks.append({"task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": employers.get("username")})

    data = {employers.get("id"): completed_tasks}

    with open('{}.json'.format(sys.argv[1]), 'w') as json_file:
        json.dump(data, json_file)

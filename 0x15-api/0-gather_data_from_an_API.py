#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employers = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title")
                 for task in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employers.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]

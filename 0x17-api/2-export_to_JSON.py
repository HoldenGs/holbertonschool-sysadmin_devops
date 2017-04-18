#!/usr/bin/python3

"""
Export the user's tasks to a CSV file
Format:
./1-export_to_CSV.py <user_id>
"""
import requests
from sys import argv

if __name__ == '__main__':

    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    task_list = []
    for item in todo:
        task_list.append('"task": "{}", "completed": "{}", "username": "{}"'
                         .format(item.get('title'), item.get('complete'),
                                 user.get('username')))
    todo_json = '{"' + argv[1] + '": [{' +  '}, {'.join(task_list) + '}]}'
    with open('{}.json'.format(user_id), 'w') as json_file:
        json_file.write(todo_json)

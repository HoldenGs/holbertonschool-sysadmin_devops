#!/usr/bin/python3

"""
Export the user's tasks to a CSV file
Format:
./1-export_to_CSV.py <user_id>
"""
import requests
from sys import argv

if __name__ == '__main__':

    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todos = requests.get(todo_url).json()
    user_list = []
    for user in requests.get(user_url).json():
        task_list = []
        for item in requests.get(todo_url + str(user.get('id'))).json():
            task_list.append('"task": "{}", "completed"\
: "{}", "username": "{}"'.format(item.get('title'), item.get('complete'),
                                 user.get('username')))
        todo_json = '"' + str(user.get('id')) \
                    + '": [{' + '}, {'.join(task_list) + '}]'
        user_list.append(todo_json)
    json = '{' + ', '.join(user_list) + '}'
    with open('todo_all_employees.json', 'w') as json_file:
        json_file.write(json)

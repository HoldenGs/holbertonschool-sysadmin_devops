#!/usr/bin/python3

"""
Export the user's tasks to a CSV file
Format:
./1-export_to_CSV.py <user_id>
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    csv_format = ''
    for item in todo:
        csv_format += '"{}","{}","{}","{}"\n'.format(item.get('userId'),
                                                     user.get('username'),
                                                     item.get('completed'),
                                                     item.get('title'))
    with open('{}.csv'.format(user_id), mode='w') as csv:
        csv.write(csv_format)

#!/usr/bin/python3

if __name__ == '__main__':
    """
    Grab the todo list for the specified user id
    Format:
    ./0-gather_data_from_an_API.py <user_id>
    """
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

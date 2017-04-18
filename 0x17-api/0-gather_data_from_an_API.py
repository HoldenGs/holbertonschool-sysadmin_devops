#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    from sys import argv

    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    todo_done = len([o for o in todo if o.get('completed') == True])
    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                        todo_done,
                                                        len(todo)))
    for item in todo:
        print('\t{}'.format(item.get('title')))

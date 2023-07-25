#!/usr/bin/python3
"""A script that uses api to store information
in a csv file"""

if __name__ == '__main__':
    import requests
    import sys
    import json

    api_todo = 'https://jsonplaceholder.typicode.com/todos'
    api_user = 'https://jsonplaceholder.typicode.com/users'
    user = int(sys.argv[1])
    value_todo = {'userId': user}
    value_user = {'id': user}
    filename = f'{str(user)}.json'

    r_todo = requests.get(api_todo, params=value_todo)
    r_user = requests.get(api_user, params=value_user)

    todo_list = r_todo.json()
    user_list = r_user.json()

    tasks = ''
    number_of_tasks = len(todo_list)
    completed_task = 0
    username = user_list[0].get('username')

    ar_dict = []

    for data in todo_list:
        new_dict = {}
        new_dict['task'] = data.get('title')
        new_dict['completed'] = data.get('completed')
        new_dict['username'] = username
        ar_dict.append(new_dict)

    json_dict = {str(user): ar_dict}

    with open(filename, mode='w') as newfile:
        json.dump(json_dict, newfile)

#!/usr/bin/python3
"""A script that uses api to print the required employee
information in a well formatted way"""

if __name__ == '__main__':
    import requests
    import sys

    api_todo = 'https://jsonplaceholder.typicode.com/todos'
    api_user = 'https://jsonplaceholder.typicode.com/users'
    user = int(sys.argv[1])
    value_todo = {'userId': user}
    value_user = {'id': user}

    r_todo = requests.get(api_todo, params=value_todo)
    r_user = requests.get(api_user, params=value_user)

    todo_list = r_todo.json()
    user_list = r_user.json()

    tasks = ''
    number_of_tasks = len(todo_list)
    completed_task = 0
    name = user_list[0].get('name')

    for i in range(number_of_tasks):
        if todo_list[i].get('completed'):
            completed_task += 1
            tasks += '\t ' + todo_list[i].get('title') + '\n'

    text = 'Employee {} is done with tasks({}/{}):'
    print(text.format(name, completed_task, number_of_tasks))
    print(tasks, end='')

#!/usr/bin/python3
"""A script that uses api to store information
in a csv file"""

if __name__ == '__main__':
    import requests
    import sys
    import json

    api_todo = 'https://jsonplaceholder.typicode.com/todos'
    api_user = 'https://jsonplaceholder.typicode.com/users'

    all_user = requests.get(api_user)
    employee_details = all_user.json()

    filename = 'todo_all_employees.json'
    employee_dict = {}

    for employee in employee_details:
        id = employee.get('id')
        id = int(id)

        value_todo = {'userId': id}
        value_user = {'id': id}

        r_todo = requests.get(api_todo, params=value_todo)
        r_user = requests.get(api_user, params=value_user)

        todo_list = r_todo.json()
        user_list = r_user.json()

        username = user_list[0].get('username')
        ar_dict = []

        for data in todo_list:
            new_dict = {}
            new_dict['username'] = username
            new_dict['task'] = data.get('title')
            new_dict['completed'] = data.get('completed')
            ar_dict.append(new_dict)

        employee_dict[str(id)] = ar_dict

    with open(filename, mode='w') as newfile:
        json.dump(employee_dict, newfile)

#!/usr/bin/python3
"""A script that uses api to store information
in a csv file"""

if __name__ == '__main__':
    import requests
    import sys
    import csv

    api_todo = 'https://jsonplaceholder.typicode.com/todos'
    api_user = 'https://jsonplaceholder.typicode.com/users'
    user = int(sys.argv[1])
    value_todo = {'userId': user}
    value_user = {'id': user}
    filename = f'{str(user)}.csv'

    r_todo = requests.get(api_todo, params=value_todo)
    r_user = requests.get(api_user, params=value_user)

    todo_list = r_todo.json()
    user_list = r_user.json()

    tasks = ''
    number_of_tasks = len(todo_list)
    completed_task = 0
    username = user_list[0].get('username')

    with open(filename, mode='w', newline='') as newfile:
        writer = csv.writer(newfile, quoting=csv.QUOTE_ALL)
        for data in todo_list:
            csv_arr = []
            csv_arr.append(user)
            csv_arr.append(username)
            csv_arr.append(data.get('completed'))
            csv_arr.append(data.get('title'))
            writer.writerow(csv_arr)

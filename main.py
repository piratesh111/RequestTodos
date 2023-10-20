import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if entry["completed"] == True:
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1
    return completedTasksFrequencyByUser

def get_user_with_most_completed_tasks(completedTasksFrequencyByUser):
    userIdWithMaxCompletedAmaountOfTasks = []
    maxAmountOfCompletedTask = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUser.items():
        if numberOfCompletedTasks == maxAmountOfCompletedTask:
            userIdWithMaxCompletedAmaountOfTasks.append(userId)
    return userIdWithMaxCompletedAmaountOfTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("nie wlasciwy format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    UsersWithMostCompletedTasks = get_user_with_most_completed_tasks(completedTasksFrequencyByUser)
    

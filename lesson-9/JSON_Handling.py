import json
import csv


with open(r'd:\Projects\github\homework stuf\lesson-9\tasks.json') as f:
    tasks = json.load(f)


total = len(tasks)
completed = sum(t['completed'] for t in tasks)
pending = total - completed
avg_priority = sum(t['priority'] for t in tasks) / total if total else 0


for t in tasks:
    if t['id'] == 1:
        t['completed'] = True


with open(r'd:\Projects\github\homework stuf\lesson-9\tasks.json', 'w') as f:
    json.dump(tasks, f, indent=4)


with open(r'd:\Projects\github\homework stuf\lesson-9\tasks.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
    for t in tasks:
        writer.writerow([t['id'], t['task'], t['completed'], t['priority']])



import csv

grades = {}


with open(r'd:\Projects\github\homework stuf\lesson-9\grades.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        subject = row['Subject']
        grade = float(row['Grade'])
        if subject not in grades:
            grades[subject] = []
        grades[subject].append(grade)


averages = []
for subject, scores in grades.items():
    avg = sum(scores) / len(scores)
    averages.append({'Subject': subject, 'Average Grade': round(avg, 2)})


with open(r'd:\Projects\github\homework stuf\lesson-9\average_grades.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Subject', 'Average Grade'])
    writer.writeheader()
    writer.writerows(averages)


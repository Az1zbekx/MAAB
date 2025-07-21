import csv
import os

if not os.path.exists("grades.csv"):
    with open("grades.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Name", "Subject", "Grade"])
        w.writerow(["Alice", "Math", "85"])
        w.writerow(["Bob", "Science", "78"])
        w.writerow(["Carol", "Math", "92"])
        w.writerow(["Dave", "History", "74"])

grades = []
with open("grades.csv", "r") as f:
    r = csv.DictReader(f)
    for row in r:
        row["Grade"] = int(row["Grade"])
        grades.append(row)

subjects = {}
for row in grades:
    subj = row["Subject"]
    if subj not in subjects:
        subjects[subj] = []
    subjects[subj].append(row["Grade"])

averages = []
for subj in subjects:
    avg = sum(subjects[subj]) / len(subjects[subj])
    averages.append({"Subject": subj, "Average Grade": round(avg, 1)})

with open("average_grades.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["Subject", "Average Grade"])
    w.writeheader()
    w.writerows(averages)

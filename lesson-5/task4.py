universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    student_counts = []
    tuition_fees = []
    for university in data:
        student_counts.append(university[1])
        tuition_fees.append(university[2])
    return student_counts, tuition_fees

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

students, tuitions = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuitions)

mean_students = mean(students)
median_students = median(students)

mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,.0f}")
print()
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,.0f}")
print("******************************")

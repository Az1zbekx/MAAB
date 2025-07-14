import os
import string
from collections import Counter

if not os.path.exists('sample.txt'):
    print("The file sample.txt was not found.")
    txt = input("Please enter some text. This text will be written to the file sample.txt = ")
    with open("sample.txt", 'w') as file:
        file.write(txt)

with open('sample.txt', 'r') as file:
    txt = file.read()

txt = txt.lower()
txt = txt.translate(str.maketrans('', '', string.punctuation))
words = txt.split()
total_words = len(words)

word_count = Counter(words)

while True:
    try:
        n = int(input("How many most common words would you like to show = "))
        if n <= 0:
            print("Enter a positive number.")
            continue
        break
    except ValueError:
        print("Enter only whole numbers.")

top_n = word_count.most_common(n)

print(f"\nTotal words: {total_words}")
print(f"Top {n} most common words:")
for word, count in top_n:
    print(f"{word} - {count} time{'s' if count > 1 else ''}")

with open("word_count_report.txt", 'w') as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write(f"Top {n} Words:\n")
    for word, count in top_n:
        report.write(f"{word} - {count}\n")

print("\nThe results were written to the file 'word_count_report.txt'")

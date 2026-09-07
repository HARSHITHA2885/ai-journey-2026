# Day 1 - Python Fundamentals
# Date: September 7, 2026

# --------------------------------------------------
# 1. Find the maximum of three numbers
# --------------------------------------------------

a = 25
b = 42
c = 18

maximum = max(a, b, c)
print("Maximum:", maximum)


# --------------------------------------------------
# 2. Count vowels in a string
# --------------------------------------------------

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"

count = 0

for character in text:
    if character in vowels:
        count += 1

print("Number of vowels:", count)


# --------------------------------------------------
# 3. Reverse a string
# --------------------------------------------------

text = "Python"

reversed_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)


# --------------------------------------------------
# 4. Check whether a string is a palindrome
# --------------------------------------------------

text = "madam"

if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")


# --------------------------------------------------
# 5. Find duplicate elements in a list
# --------------------------------------------------

numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate elements:", duplicates)


# --------------------------------------------------
# 6. Count the frequency of words
# --------------------------------------------------

sentence = "python is easy and python is powerful"

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


# --------------------------------------------------
# 7. Find the second-largest number
# --------------------------------------------------

numbers = [10, 25, 7, 42, 18]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Second-largest number:", second_largest)


# --------------------------------------------------
# 8. Calculate a student's average marks
# --------------------------------------------------

marks = [85, 78, 92, 88, 76]

average = sum(marks) / len(marks)

print("Average marks:", average)


# --------------------------------------------------
# 9. Classify student marks
# --------------------------------------------------

def classify_marks(mark):
    if mark >= 90:
        return "Excellent"
    elif mark >= 75:
        return "Very Good"
    elif mark >= 60:
        return "Good"
    elif mark >= 40:
        return "Pass"
    else:
        return "Fail"


student_mark = 82

result = classify_marks(student_mark)

print("Student mark:", student_mark)
print("Performance:", result)

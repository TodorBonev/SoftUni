def rate_the_grade(grade):
    result = ""
    if 2 <= grade <= 2.99:
        result = "Fail"
    elif 3.00 <= grade <= 3.49:
        result = "Poor"
    elif 3.50 <= grade <= 4.49:
        result = "Good"
    elif 4.50 <= grade <= 5.49:
        result = "Very Good"
    elif 5.50 <= grade <= 6.00:
        result = "Excellent"
    print(result)


current_grade = float(input())
rate_the_grade(current_grade)
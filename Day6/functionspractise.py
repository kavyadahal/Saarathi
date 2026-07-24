def celsius_to_f(c):
    return c * 9 / 5 + 32


def grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "Fail"


def average(*nums):
    return sum(nums) / len(nums)


# Call each and print the results
print(celsius_to_f(30))       # 86.0
print(grade(72))              # B
print(average(4, 9, 1, 6))    # 5.0
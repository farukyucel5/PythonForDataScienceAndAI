def classify_bmi(bmi):
    if bmi < 18.5:
        return "cılız"
    elif 18.5 <= bmi < 24.9:
        return "fit"
    elif 25 <= bmi < 29.9:
        return "kilolu"
    else:
        return "obez"
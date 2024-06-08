def bmi(weight, height):
    bmi_index = weight / (height * height)

    if bmi_index <= 18.5:
        return "Underweight"

    if bmi_index <= 25.0:
        return "Normal"

    if bmi_index <= 30:
        return "Overweight"

    return "Obese"


# 9.BMI Calculator
# Print “Let’s calculate your BMI (kg/m2)” to the console.
# Ask the user about the weight in KG.
# Ask the user about the height in CM.
# Read the users weight as a float.
# Read the users height.
# Define a function to calculate the BMI and show info if they are
# underweight, overweight or normal weight.

def bmi_calculator():

    print("Let’s calculate your BMI (kg/m2)")
    weight_kg = float(input('What is your weight in kg? \n'))
    height_cm = int(input('What is you height in cm? \n'))

    bmi = round(weight_kg / ((0.01 * height_cm) ** 2), 1)

    print(f'Your BMI is: {bmi}')
    if bmi <= 18.5:
        return 'You must eat more, you are underweight!!'
    elif 18.5 < bmi <= 25:
        return 'Congrats, you are normal'
    elif 25 < bmi:
        return 'Stop eating!! You are overweight'


print(bmi_calculator())

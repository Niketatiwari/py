def bodymassindex(height, weight):
    return round((weight / height**2),2)

h = float(input("enter ur height in centimetres: "))
w = float(input("enter ur weight in kg: "))
print("welcome to BMI calculator")
bmi = bodymassindex(h, w)
print("your BMI is: ",bmi)

if bmi <= 18.5:
    print("you are underweight")
elif 18.5<bmi<=24.9:
    print("your weight is normal")
elif 25< bmi <= 29.29:
    print("you are overweight")
else:
    print("you are obese")
#Create a program that calculates the body fat percentage for a given weight and body fat weight. Then, determine if the person is in a healthy range.

weight = float(input("Enter your weight in kilograms: "))
body_fat_weight = float(input("Enter your body fat weight in kilograms: "))
gender = input("Enter your gender (male/female): ")
body_fat_percentage = (body_fat_weight * 100) // weight
if gender == 'male':
    is_healthy = 10 <= body_fat_percentage <= 20
elif gender == 'female':
    is_healthy = 18 <= body_fat_percentage <= 28
else:
    print("Error: Gender should be 'male' or 'female.'")
    weight = 0
    body_fat_weight = 0
    gender = ""
    body_fat_percentage = 0
    is_healthy = False
if is_healthy:
    print("Your body fat percentage is", body_fat_percentage, "% which is in a healthy range.")
else:
    print("Your body fat percentage is", body_fat_percentage, "% which is not in a healthy range.")

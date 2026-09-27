coffee_type = ["Espresso", "Black Coffee", "Americano", "Macchiato", "Affogato"]
for coffee in coffee_type:
    if coffee != "Espresso":
        print(coffee)
    else:
        print(coffee)




print()
languages = ["PYTHON", "JAVA", "C++"]
for language in languages:
    if language == "python":
        print(language.lower())
    else:
        print(language.title())



print()
ages = ["18", "19", "20", "21"]
for age in ages:
    if age >= "18":
        print(age)
    elif age <= "18":
        print(age)
    else:
        print(age)



print()
ages = ["18", "19", "20", "21", "25"]
for age in ages:
    if age == "25":
        print(age)
    elif age == "21":
        print(age)




print()
ages = ["18", "19", "20", "21", "25"]
for age in ages:
    if age > "25":
        print(age)
    elif age == "21":
        print(age)
    elif "18" < age < "21":
        print(age)

print()
X = 50
y = 25

if X >= 50 or y > 25:
    print("one of the conditions is false!")


print()
X = 20
Y = 15

if X <= 20 and Y <= 15:
    print("one of the conditions is true!")



print()
classes = ["Computer Science", "Discrete Mathematics", "Network Engineering", "Automation", "Acting"]
for cls in classes:
    if cls == "Computer Science":
        print(cls)
        break
    else:
        print(cls)


print()
classes = ["Computer Science", "Discrete Mathematics", "Network Engineering", "Automation", "Acting"]
for cls in classes:
    if cls == "Drama":
        print(cls)
    elif cls != "Acting":
        print(cls)


print()
classes = ["Computer Science", "Discrete Mathematics", "Network Engineering", "Automation", "Acting"]
for cls in classes:
    if cls == "Dancing":
        print(cls)
        break
    else:
        print("I have not signed up for this class yet!!")
        break

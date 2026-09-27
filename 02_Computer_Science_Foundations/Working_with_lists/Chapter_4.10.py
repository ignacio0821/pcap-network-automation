my_foods = ["carne asada", "torta", "menudo", "bean burrito", "spanish rice", "shashilk","Ukrainian pancakes"]
print(f"The first three items of the list are.")
for food in my_foods[:3]:
    print(food.title(), "\n")

print(f"Three items from the middle list are.")
for food in my_foods[3:6]:
    print(f"{food.title()}\n")


print(f"The last three items on the list are.")
for food in my_foods[-3:]:
    print(food.title())
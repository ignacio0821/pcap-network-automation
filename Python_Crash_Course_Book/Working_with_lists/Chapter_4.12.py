foods = ["pizza", "sushi", "ramen", "avocado toast", "rotisserie chicken"]
friend_food = foods[:]
foods.append("burrito")
friend_food.append("shrimp")
print(f"[!]😊 I am hungry now!!--")
for food in foods:
    print(food)

print()

print(f"My friend also enjoys to eat well!!--")
for food in friend_food:
    print(food)

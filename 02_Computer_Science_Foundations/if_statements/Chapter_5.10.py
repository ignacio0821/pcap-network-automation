current_users = ["UserNode", "Datacore", "Wanderbit", "Staticfade", "DeminFade", "GraphiteStitch"]
new_users = ["GraphiteStitch", "RustCanvas", "ChalkStudio", "CobaltBlue", "MacroStudio"]
for new_user in new_users:
    if new_user not in current_users:
        print(f" You {new_user} have been successfully added!")
    else:
        print(f" You {new_user} will need to select a different user name")




print()
current_users = ["UserNode", "Datacore", "Wanderbit", "Staticfade", "DeminFade", "GraphiteStitch"]
new_users = ["GraphiteStitch", "RustCanvas", "ChalkStudio", "CobaltBlue", "MacroStudio"]
for new_user in new_users:
    if new_user not in current_users:
        print(f" You {new_user} have been successfully added!")

        current_users.append(new_user)
    else:
        print(f" You {new_user} will need to select a different user name", end=" ")

print("\n ---Final Mixed User list ---")

for mix_user in current_users:
    print(mix_user)


print()
current_users = ["UserNode", "Datacore", "Wanderbit", "Staticfade", "DeminFade", "GraphiteStitch"]
new_users = ["GraphiteStitch", "RustCanvas", "ChalkStudio", "CobaltBlue", "MacroStudio"]

current_users_lower = {user.lower() for user in current_users}

for new_user in new_users:
    if new_user.lower() not in current_users_lower:
        print(f" You {new_user} have been successfully added!")
    else:
        print(f" You {new_user} will need to select a different user name")


print()
current_users = ["UserNode", "Datacore", "Wanderbit", "Staticfade", "DeminFade", "GraphiteStitch"]
new_users = ["GraphiteStitch", "RustCanvas", "ChalkStudio", "CobaltBlue", "MacroStudio"]

# 1. Create a lowercase set of current users for safe, case-insensitive comparison
current_users_lower = {user.lower() for user in current_users}

# 2. Process new users
for new_user in new_users:
    if new_user.lower() not in current_users_lower:
        print(f"You {new_user} have been successfully added!")

        # Add to both lists so the script tracks it in real-time
        current_users.append(new_user)
        current_users_lower.add(new_user.lower())
    else:
        print(f"You {new_user} will need to select a different user name.")

print("\n--- Final Mixed User List ---")

# 3. Print the final list (GraphiteStitch will only print once)
for mix_user in current_users:
    print(mix_user)























# list
equipment_2 = []
equipment_1 = ["curl bar", "jump rope", "sledgehammer", "tire", "sled", "Kettlebell", "dip stand", "pullup bar"]
print(equipment_1)
print(equipment_1[0].title())
print(equipment_1[1])
print(equipment_1[2].upper())
print(equipment_1[-1])
print(f"[!] This is a must for beautiful biceps {equipment_1[0].upper()}")
equipment_1.append("bench")
print(equipment_1)
equipment_2.append("Plates")
equipment_2.append("heavy bag")
equipment_2.append("speed bag")
print(equipment_2)
equipment_1.insert(3, "Coffin")
print(equipment_1)
del equipment_2[0]
print(equipment_2)
popped_list = equipment_2.pop()
print(equipment_2)
print(popped_list)

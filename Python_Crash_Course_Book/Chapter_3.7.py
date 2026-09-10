# Guest list

people = ["Abe Lincoln", "Geronimo", "Patton", "JFK", "Danny Trejo"]
people_popped = people.pop(3)
people.insert(3, "McArthur")
print(people)
print(f"[!] ATTENTION: JFK can no longer attend the Year end bash")

print(f" Please attend the end of the Year Bash -- {people}\n")
people.insert(0, "Hercules")
people.append("Elvis")
print(f"[!] Attention: I am happy to inform all we have found a massive round table for the year end event! {people}")
people.pop(3)
people.pop(2)
new_list = people.pop()
print(f" my apologies --{people.pop(3)}-- at this time your are uninvited!")
print(f" my apologies __{people.pop(2)}-- at this time your are uninvited!")
print(f" my apologies __{people.pop(0)}-- at this time your are uninvited!")
print(f" ATTN: 😁 --{people} You are the lucky ones and still invited to attend!!")
print(f"[!]😑 ATTN: The massive round table will not be available in time for the dinner!!, Some of the invited guest will now be unable to attend!")
del people[0]
print(people)

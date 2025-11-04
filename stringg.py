
letter = """ Dear <name>, 
you are selected
<date> """
print(letter.replace("<name>", "shezan").replace("<date>", "24 september"))
friends =[ "apple" , "orange", 5 , 345.06 , False, 'Akash', "Rohan"]
# 
friends.append("Shezan")
print(friends)
l1 = [1, 34,65,2,6,11]
# l1.reverse()
# l1.sort()
# l1.insert(3, 44)
l1.pop(3)
print(l1)
fruits =[]
f1 = input( "Enter fruit name : ")
fruits.append(f1)
f2 = input("Enetr fruit name : ")
fruits.append(f2)
print(fruits)
q = [1,2,3]
print(sum(q))
marks = {
    "shezan": 21,
    "kaif" : 24,
    "anik": 56,
    0: "shihab"
}

# print(marks["shezan"])
marks.update({"shezan": 99})
print(marks)
str = "Apnacollage"

print(str)

# s ={1,2,3,6,5,5,5, "harry"} 
# e = set()

# s.add(67)
# print(s, type(s))
s1={ 1, 4, 5}
s2 = {7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))
word = {
    "Sahajjo": "help",
    "Nodi": "river",
}

words = input("Enter any word: ")
print(word.get(words, "Word not found"))

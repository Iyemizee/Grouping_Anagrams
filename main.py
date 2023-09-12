#this was another leet code project i did
#basically to group anagrams and return as a list
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

#the logic used for this is using a dictionary
#sort every item in the list and use the sorted item as the key while the word would be the value
#i.e {aet:[eat,tea,ate], ant:[tan,nat],abt:[bat]

final_list = []
dict = {}

for index,word in enumerate(strs):
    new_str = "".join(sorted(word)) #the word is sorted and joined as a string
    if dict.get(new_str, None) is None: #using .get to set the value to none
        dict[new_str] = [word]      #new string is the key and the word would be the value as a list
    else:
        dict[new_str].append(word)
for key,val in dict.items(): #iterating our new dictionary and only pickig the valut to be appended into the empty list
    final_list.append(val)
print(final_list)

#kinda compelex.. a little difficult to figure out
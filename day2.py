# #word replacement
# sentence=input('Enter Your sentence: ')
# print(sentence)
# word1=input('Enter your word to replace: ')
# word2=input('Enter your word to replace it with: ')
# print(sentence.replace(word1, word2))

#Lists
lang=['Java', 'Python', 'C++', 'Dart', 2004, True]  #can also use list(('java',24,False)) [List Constructor]
print(lang)
print(lang[0])
print(lang[2][2])
print(lang[2:])
print(type(lang))
lang[2]='C'
print(lang)
print(lang[-1])

#List Methods
list1=[1,3,5,6,7,2,9,5,8,2]
list2=['rust','ruby','swift','assembly']
# list1.extend(list2)
print(list1)

list2.append('go')
print(list2)

list2.insert(1, 'java')
print(list2)

list2.remove('swift')
print(list2)

# list2.clear()
# print(list2)

print(list2.index('go'))
print(list2.count('go'))


list1.sort()
print(list1)

# list2.reverse()
# print(list2)

list3=list2.copy()
print(list3)

list2.pop(1)
print(list2)

del list2[0]
print(list2)
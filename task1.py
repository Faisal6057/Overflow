# Creating a list and performing different operations.
myList =[]
for i in range(1,5):
    myList.append(i**2)
print(myList)
myList.remove(4)
print(myList)
myList.append(5)
print(myList)
myList.insert(0,2)
print("LIST: ",myList)

# Creating dictionary
myDict = {}
myDict['name'] = 'John'
myDict['age'] = 20
myDict['id'] = '121'
myDict['branch'] = 'cse'
print(myDict)
print("Dictionary:",myDict.values())

# Creating Sets

mySet =set()
mySet.add(1)
mySet.add(2)
[mySet.add(i**3) for i in range(2,5)]
print("SET: ",mySet)
mySet.remove(2)
print("SET: ",mySet)




****** targil 1:
  
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_fr = [i for i in fruits  if i.count('a') > 0 ]
print(new_fr)


****** targil 2:
  
some_list = [1,4,7,12,19,22, 23, 26]
sort_list = [(f'{x} is even') if x % 2 == 0 else (f'{x} is odd') for x in some_list  ]
print(sort_list)


****** targil 3:
  
list1 = [1,2]
list2 = [4,5]
tup_list = [(j,i)  for j in list1 for i in list2  ]
print(tup_list)  
  

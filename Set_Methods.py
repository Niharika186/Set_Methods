'''A set itself is mutable(cannot be changed),but we can add or remove the elements'''
'''Empty curly braket represents dictonary'''
# a={}
# print(a,type(a)) # {} dict

'''Curly bracket with inside elements-set '''
# b={1,2,3,4}
# print(b,type(b)) # {1,2,3,4} set 

'''Set cannot have index positions'''
# c={1,2,3,4,5}
# print(c[0]) # TypeError: 'set' object is not subscriptable

'''set is unordered, it not shows the output as same in the input order'''
# d={2,5.6,'hii',(2,3)}
# print(d,type(d)) #  {(2, 3), 2, 'hii', 5.6} set 

'''A set cannot contain a list,it will shows the error'''
# a={5,8.9,'hello',(27,9),[2,4]}
# print(a,type(a)) # TypeError: unhashable type: 'list'

'''A set cannot contain one more set inside it,it will shows the error'''
# b={5,8.9,'hello',(27,9),{1,2}}
# print(b,type(b)) # TypeError: unhashable type: 'set'

'''Set Methods'''
# a={1,2,3}
# b=(5,6,7)
# a.add(b)
# print(a) # {(5, 6, 7), 1, 2, 3}

# a={1,2,3}
# a.clear()
# print(a) # set() (empty set represtent as set())

'Discard-If the given element is not in input it shows same input(nothing do chnages),but if the element is there in input it will remove that & shows the output'
# x={11,22,33,44,55,66}
# x.discard(66)
# print(x) # {33, 22, 55, 11, 44} 
# x.discard(44)
# print(x) # {33, 22, 55, 11}

# a={1,2,3,4};b={3,4,5,6};c={5,6,7};d={4,5,6}
# print(a.intersection(b)) # {3,4}
# print(a.intersection(c)) # set() (if nothing are same in both sets,it will show set())
# print(a.intersection(d)) # {4}
# print(b.intersection(c)) # {5,6}
# print(c.intersection(d)) # {5,6}

# a={1,2,3,4};b={3,4,5,6};c={5,6,7};d={4,5,6}
# print(a.isdisjoint(b)) # False (If the same elements are there in both sets)
# print(a.isdisjoint(c)) # True (If the elements are unique in both sets)
# print(a.isdisjoint(d)) # False

# x={10,20,30,40,50}
# x.pop() 
# print(x) # {20, 40, 10, 30}
# z={1,2,3,4}
# z.pop()
# print(z) # {2, 3, 4} (it will remove random element in the sets)

# a={'hii',2,3.4,(8,9)}
# a.remove(2)
# print(a) # {3.4, (8, 9), 'hii'}

'''Union- it will combine both sets'''
# a={2,4,6,8};b={1,3,5,7} 
# print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
# print(b.union(a)) # {1, 2, 3, 4, 5, 6, 7, 8}

'''difference-it will remove the same elements present in the both sets and give the elements in in the first set'''
# x={21,13,45,76}
# y={34,56,21}
# print(x.difference(y)) # {13, 76, 45}
# print(y.difference(x)) # {56, 34}
# print(x-y) # {13, 76, 45}
# print(y-x) # 

'''issubset-returns true if another set contains this set otherwise false'''
# a={10,20,30,40}
# b={20,30}
# c={10,20,30,40,50}
# print(a.issubset(b)) # Flase
# print(b.issubset(a)) # True
# print(a.issubset(c)) # True
# print(c.issubset(a)) # Flase

# a={1,2,3}   
# b={4,5,6}
# c={7,8,9}
# a.update(b)
# b.update(c)
# c.update(a)
# print(a) # {1,2,3,4,5,6} 
# print(b) # {4,5,6,7,8,9}
# print(c) # {1, 2, 3, 7, 8, 9}

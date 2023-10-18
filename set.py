#Set data type

#1.implicit

a = {'a','b','c'}
print(a)

#2.explicit

a = set(('a','b','c'))
print(type(a))

#3.data type /varabail annotation

a:set = {'a','b','c'}
print(type(a))

#CRUD OPERAtions on set

#.*Create
#1.add:
a:set = {'a','b','c'}
a.add('d')
print(a)

#.*Update
a:set = {'a','b','c'}
b:set = {'b','c','d'}
a.update(b)
print(a)

#.*Delete
#1.Remove

a:set = {'a','b','c'}
a.remove('b')
print(a)

#2.Discard

a:set = {'a','b','c'}
a.discard('d')
print(a)

#3.pop

a:set = {'a','b','c'}
a.pop()
print(a)

#Some other methods of set

#Union

a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.union(b))

#intersection

a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.intersection(b))

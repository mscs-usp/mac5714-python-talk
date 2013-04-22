from material import *

m = Material('Design Patterns')
m.tags.add('Computer Science')
m.like(); m.like()
print m.likes
print m.description()
print m.tags

b = Book(title = 'Design Patterns', author = 'GoF', tags = ['Computer Science', 'Software Design'])
print b.likes
print b.description()
print b.tags

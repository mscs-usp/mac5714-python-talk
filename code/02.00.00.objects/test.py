from employee import *

bob = Employee('Bob Smith')
sue = Employee('Sue Jones', 40000.00, 'programmer')
tom = Manager(name='Tom Doe', pay=50000.00)

for obj in (bob, sue, tom):
    print obj
    obj.giveRaise(.10) # run this obj's giveRaise
    print obj # run common __str__ method

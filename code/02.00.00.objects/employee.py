class Employee(object):
    """
    a general employee: data+logic
    """

    def __init__(self, name, pay=0.0, job=None):
        self.name = name
        self.pay = pay
        self.job = job

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return ('<%s => %s: %s, %s>'
                %(self.__class__.__name__,
                  self.name, self.job, self.pay))


class Manager(Employee):
    """
    an employee with custom raise
    """

    def __init__(self, name, pay):
        super(Manager, self).__init__(name, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        super(Manager, self).giveRaise(percent + bonus)


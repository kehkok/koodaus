"""
    Simple class tutorial to show inheritance
"""


class Base(object):
    """
    A Base Class

    Attributes
    ----------
    name    : str
        Name of person

    Methods
    -------
    getName()
        Print the name
    """
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


class Child(Base):
    """
    A Child Class

    Attributes
    ----------
    name    : str
        Name of person
    age     : int
        The age of the person

    Methods
    -------
    getAge()
        Print the age
    """
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age =age

    # Go get name
    def getAge(self):
        return self.age


class GrandChild(Child):
    """
    A Grand Child Class

    Attributes
    ----------
    name    : str
        Name of person
    age     : int
        The age of the person
    address : str
        The address of the person

    Methods
    -------
    getAddress()
        Print the address
    """
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Sample code
sobj = GrandChild("Yonex King", 18, "No. 3, Jalan Bukit Jalil.")
print(sobj.getName(), sobj.getAge(), sobj.getAddress())

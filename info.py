#staticmethod  there is no need instance of outher class to know about this instance (no need to self)
# @abstractmethod shoud any inherited have to implement (overloading from inheritance)
# mix-in Base class tells there is a method, class of mix-in bring implementation /
    #himself (return "string").
# interface is the opposite. they have methods and obligations meix-in to have implementation
# @property it for read only, cannot be overwritten. Calling without parameters. \
    # It's looks like data attributes
# Its treated as data atributes. Calling that method without brackets ()
#Dyp-typeing caares is there a method that we can use

#class Class:
    #_LOCAL_ATRIBUTES = [] class atributes its cvalificate as DATA and methods

    #def __init__(self, name: str): #name is dependency def - method
    #self.name = name atributes

    #def methods(self): method
        # ...

#SOLID
#S - Single resposibility
    # - one class shoud be resposibility for one specific functionality
#O - Open / Close
    # - shoud be open for extension, and close for modification
#L - List of substitutions
    # - shoud have same behavior with base class
#I - Interface agregation
    # - mix-in shoud not have methods then is not going to be used
#D - Dependencies inversions
    # - parent class no need to know about theirs children
    # !!! ditails depends on abstraction
    # replace methods isinstance with baseclass

#iterators - It's an object that we can iterate over __iter__ and __next__


#testing:
# #unit tests, - pattern matching tripple A pattern: range - we creat information, act -calling method, assert - expected result
# #intigrations tests, test flow, you can modify
# end to end tests - QA automatically clicks on the program (usually can be bot)
#mooking tests - third part apis 



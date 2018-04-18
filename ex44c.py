#Inheritance versus Composition
#When you are doing inheritance, there a re three ways that the parent and child classes interact:
# 1. Actions on the child imply and action on the parent
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# Alter Before or After

class Parent(object):

    def altered(self):
        print("PARENT altered()")
#executeing altered in dad prints the above
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()
#from dad and son execute altered
dad.altered()
son.altered()

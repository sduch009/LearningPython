#Inheritance versus Composition
#When you are doing inheritance, there a re three ways that the parent and child classes interact:
# 1. Actions on the child imply and action on the parent
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

#Override Explicitly

class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

#Composition
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(boject):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTEHR altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

#When to use?

#YOU DON'T WANT TO HAVE DUPLICATED CODE ALL OVER YOUR SOFTWARE, INHERITANCE SOLVES THIS PROBLEM
#BY CREATING A MECHANISM FOR YOU TO HAVE IMPLIED FEATURES IN BASE CLASSES.

#THREE GUIDELINES WHEN TO DO WHICH
# 1- AVOID MULTIPLE INHERITANCE AT ALL COSTS, AS IT'S TOO COMPLEX TO BE RELIABLE. IF YOU'RE STUCK WITH IT, THEN BE PREPARED TO KNOW THE CLASS HIERARCHY AND SPEND TIME FINDING WHERE EVERYTHING IS COMING FROM.
# 2- USE COMPOSITION TO PACKAGE CODE INTO MODULES THAT ARE USED IN MANY DIFFERENT UNRELATED PLACED ANS SITUATIONS.
# 3- USE INHERITANCE ONLY WHEN THERE ARE CLEARLY RELATED REUSABLE PIECES OF CODE THAT FIT UNDER A SINGLE COMMON CONCEPT OR IF YOU HAVE TO BECAUSE OF SOMETHING YOU'RE USING.

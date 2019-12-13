namesTuple = ("Hadi", "Mehrdad", "Hossein", "Pegah")
namesSet = {"Hadi", "Mehrdad", "Hossein", "Pegah"}
namesList = ["Hadi", "Mehrdad", "Hossein", "Pegah"]

def printName(names):
    """
        prints names of technical team
    """
    for name in names:
        print(name)


help(printName)

namesList[1] = "new"

printName(namesTuple)
printName(namesSet)
printName(namesList)
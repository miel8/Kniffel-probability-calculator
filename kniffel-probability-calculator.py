from random import randint

def rollFiveDiceAndCheckForKniffel(): # Does what the name suggests
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    roll4 = randint(1, 6)
    roll5 = randint(1, 6)
    if roll1 == roll2 == roll3 == roll4 == roll5:
        return True
    else:
        return False

def returnNumberOfThrowsToKniffel(): #Also does after it's name, needs rollFiveDiceAndCheckForKniffel()
    throws = 0
    success = False
    while not success:
        throws += 1
        success = rollFiveDiceAndCheckForKniffel()
    return throws

def addListFiguresTogether(list:list): #Adds numbers in a given list together and returns the total
    total = 0
    for i in list:
        total += i
    return total

def calculateaverage(numberlist:list): #Calculates the average value of all numbers in a given list, needs addListFiguresTogether() also the math module probably has this but I was too lazy to check when I made this so..
    numberOfItems = len(numberlist)
    total = addListFiguresTogether(numberlist)
    return total/numberOfItems


i = 0
results = []
avg = 0
if input("Output during calculation (~25% Slower) [y/n]? ")=="y": #Outputs are given after each kniffel has been achieved    
    for i in range(0, int(input("Number of Kniffels: "))):
        result = returnNumberOfThrowsToKniffel() 
        results.append(result)
        avg=calculateaverage(results)
        print("Throws: ", result, "  AVG: ", avg, "Probability: ", 100 / avg) 
        #What this outputs: (1) The amount of throws it took for this kniffel (2) The current average throws for a kniffel (3) The current calculated probability of a kniffel based on the avg throws
else:
    for i in range(0, int(input("Number of Kniffels: "))):
        result = returnNumberOfThrowsToKniffel()
        results.append(result)

print("Final average: ", calculateaverage(results), "Probability: ", 100/calculateaverage(results),"%")

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is likely'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Fo Sho'
    
print(getAnswer(random.randint(1,4)))
#r = random.randint(1,4)
#fortune = getAnswer(r)
#print(fortune)

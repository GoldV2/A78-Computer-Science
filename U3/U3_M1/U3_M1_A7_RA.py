# Program name: U1_M1_A7_RA.py
# Program purpose: print formatting
# Created/revised: R. Almeida on 10-22-20

# 4
numberErrors = 0

print('An integer of', 14, "combined with strings causes", numberErrors, "TypeRrors in comma formatted print!")

# 5
print('I had', 2, 'eggs and', 4, 'pieces of bacon for breakfast')

# 6
name = input('What is your name?\n\n>>> ')
street = input('What is the name of your street?\n\n>>> ')
stNumber = int(input('What is your street number?\n\n>>> '))
print(name, 'lives at', stNumber, street)

# 7
nBears = 3
nPenguins = 5
zooName = 'South Park Zoo'
print('In', zooName, 'there are', nBears, 'bears and', nPenguins, 'penguins. In total there are', nBears + nPenguins, 'animals.')

# 8 
class Training:
    def __init__(self, name, time, groupNum, minEarly):
        self.name = name
        self.time = time
        self.groupNum = groupNum
        self.minEarly = minEarly

    def printInfo(self):
        print(self.name, 'will start at', self.time, 'there will be', self.groupNum, 'people. Everyone is expected to arrive', self.minEarly, 'minutes earlier.')

    def changeTime(self):
        newTime = input(f'What is the new time for {self.name}?\n\n>>> ')
        self.time = newTime
        print('The time has been changed to', self.time)

    def changeGroupNum(self):
        newGroupNum = int(input('What is the new group size?\n\n>>> '))
        print('Group size has been changed from', self.groupNum, 'to', newGroupNum)
        self.groupNum = newGroupNum

rafaelTraining = Training('Rafael\'s Training Class', '10:30 am', 24, '10')
rafaelTraining.printInfo()
rafaelTraining.changeTime()
rafaelTraining.changeGroupNum()
rafaelTraining.printInfo()
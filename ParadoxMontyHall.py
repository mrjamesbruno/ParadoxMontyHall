import random, datetime

playerSwitch = True
dateTimeNow = datetime.datetime.now()
i = 1
countLoose = 0
countWon = 0
def mainLoop():
    global i,playerSwitch,countLoose,countWon
    while i <= 10000:
        doors = random.randint(1,3)
        player = random.randint(1,3)
        diffDoorsPlayer = doors-player
        #znach ugadal srazy > v konechnom itoge esli playerSwitch=true budet ne ugadal i naoborot
        if diffDoorsPlayer == 0:
            if playerSwitch: countLoose +=1
            else: countWon += 1
        else: # esli srazu neugadal
            if playerSwitch: countWon +=1
            else: countLoose += 1
        i +=1
        #print(f'playerSwitch: {playerSwitch}, Wins: {countWon}, Losses: {countLoose}')

    print(f'Final scoore >> {dateTimeNow} > playerSwitch: {playerSwitch},  Wins: {countWon}, Losses: {countLoose}')
    file = open('Scoore.txt', 'a')
    file.write(f'Final scoore >> {dateTimeNow} > playerSwitch: {playerSwitch}, Wins: {countWon}, Losses: {countLoose}\n')
    file.close()
    input("Press Enter to continue...")
    countLoose = 0
    countWon = 0
    i = 1
    mainLoop()
mainLoop()
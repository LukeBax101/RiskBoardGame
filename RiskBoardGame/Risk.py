from tkinter import *
import random

noOfPlayers = 0
players = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
instance = 0
coloursLeft = ["dark green","red","orange","blue","dark grey"]
playerTurn = 0


noOfCardsButton = 0
noOfTroopsLabel = 0
placeTroopsPart = True
battlePart = False
movePart = False
selected = [42,42]

aftermath = False
cardGiven = False
permitMove = False
playing = False
linkedCount = []
done = []

def resetBoo():
    global placeTroopsPart,battlePart,movepart,selected,aftermath,cardGiven,permitMove,linkedCount,done
    placeTroopsPart = True
    battlePart = False
    movePart = False
    aftermath = False
    cardGiven = False
    permitMove = False
    selected = [42,42]
    linkedCount = []
    done = []

def startMenu():
    gameFrame.pack_forget()
    colours.pack_forget()
    menu.pack()

def endGame():
    main.destroy()
    
def playerColours():
    gameFrame.pack_forget()
    colours.pack()
    menu.pack_forget()
    global instance,coloursLeft
    if instance == noOfPlayers:
        playGame()
    else:
        if instance == 0:
            colourFramesTop[0].grid(row= 0,column = 0)
            packColourButtons(coloursLeft)
        elif instance == 1:
            colourFramesTop[1].grid(row= 0,column = 0)
            packColourButtons(coloursLeft)
        elif instance == 2:
            colourFramesTop[2].grid(row= 0,column = 0)
            packColourButtons(coloursLeft)
        elif instance == 3:
            colourFramesTop[3].grid(row= 0,column = 0)
            packColourButtons(coloursLeft)
        elif instance == 4:
            colourFramesTop[4].grid(row= 0,column = 0)
            packColourButtons(coloursLeft)
        
def playGame():
    global noOfPlayers,playerTurn
    playersClearUp()
    colours.pack_forget()
    countryAllo()
    nextPlayerGo()

def nextPlayerGo():
    global noOfPlayers,playerTurn, players
    gameFrame.pack_forget()
    players[playerTurn][2] = players[playerTurn][2] + 3
    calculateTroops()
    resetBoo()
    takeTurn(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)
    


def selectNextPlayer():
    global noOfPlayers, playerTurn,cardGiven,playing
    if cardGiven == True:
        players[playerTurn][1] = players[playerTurn][1]+1
    if playerTurn+1 < noOfPlayers:
        playerTurn = playerTurn +1
    else:
        playerTurn = 0
    clearScreen()
    playing = True
    nextPlayerGo()

def clearScreen():
    global noOfCardsButton, noOfTroopsLabel
    noOfCardsButton.grid_forget()
    noOfTroopsLabel.grid_forget()


def refresh():
    global players, playerTurn,playing
    #if playing == True:
     #   clearAll()
    buildTopFrame(playerTurn)
    buildBottomFrame(playerTurn)
    buildMap()
    #buildInstructionPanel()


##################################################################################################################################################################
    #############################################################################################################################################################
    ##################################################################################################################################################################

def buildInstructionPanel():
    global players,countries,playerTurn, placeTroopsPart,aftermath,permitMove,selected
    sea = "#009475"
    instructionPanel = Frame(board, bg = sea, width = 200, height = 250)
    instructionPanel.place(x = 10, y = 400)
    placeFrame = Frame(instructionPanel)
    attackFrame = Frame(instructionPanel)
    placeTitle = Label(placeFrame, text = "Place your Troops", font = medFont, fg = "red", bg = sea)
    placeTitle.grid(row = 0, column = 0)
    placeNorm = Label(placeFrame, text = "Click on any of your countries to place a troop", font = textFont, fg = "red", bg = sea, wraplength = 200)
    placeAttack = Label(placeFrame, text = "Click on either of the two countries last involved in battle to place a troop on them", font = textFont, fg = "red", wraplength = 200,bg = sea)
    placeMove = Label(placeFrame, text = "Click on either of the two countries between which troops are moving to place a troop on them", font = textFont, fg = "red", wraplength = 200,bg = sea)
    attackTitle = Label(placeFrame, text = "Attack or Manoeuvre", font = medFont, fg = "red", bg = sea)
    attackTitle.grid(row = 0, column = 0)
    attack1 = Label(attackFrame, text = "Click on any country owned by you to attack from it or source your troops for a move from it", font = textFont,fg = "red",wraplength = 200, bg = sea)
    attack2 = Label(attackFrame, text = "Click on any neighboring enemy country to attack, or a freindly one to move.", font = textFont,fg = "red",wraplength = 200, bg = sea)

    if players[playerTurn][2] > 0:
        attackFrame.pack_forget()
        placeFrame.pack(fill = BOTH, expand = True)
        if permitMove == True:
            placeNorm.grid_forget()
            placeAttack.grid_forget()
            placeMove.grid(row = 1, column = 0)
        elif aftermath == True:
            placeNorm.grid_forget()
            placeAttack.grid(row = 1, column = 0)
            placeMove.grid_forget()
        elif placeTroopsPart == True:
            placeNorm.grid(row = 1, column = 0)
            placeAttack.grid_forget()
            placeMove.grid_forget()
    else:
        placeFrame.pack_forget()
        attackFrame.pack(fill = BOTH, expand = True)
        if selected[1] == 42:
            if selected[0] == 42:
                attack1.grid(row = 1,column = 0)
                attack2.grid_forget()
            if selected[0] != 42:
                attack1.grid_forget()
                attack2.grid(row=1,column = 0)
        
        
    
    




def takeTurn(x):
    global placeTroopsPart,battlePart,movePart
    refresh()
    
    

def battle(x,y):
    blackNo = attackDie(x)
    redNo = defendDie(y)
    orBlackNo = []
    orRedNo = []
    for a in range(x):
        maxi = 0
        for v in range(3-a):
            if blackNo[v] > maxi:
                maxi= blackNo[v]
        orBlackNo.append(maxi)
        blackNo.remove(maxi)
    for b in range(y):
        maxiRed = 0
        for m in range(2-b):
            if redNo[m] >= maxiRed:
                maxiRed = redNo[m]
        orRedNo.append(maxiRed)
        redNo.remove(maxiRed)
    if x>y:
        z = y
    if x<y:
        z = x
    if x ==y:
        z = x
    attackLost = 0
    defLost = 0
    for u in range(z):
        if orRedNo[u] >= orBlackNo[u]:
            attackLost = attackLost +1
        elif orBlackNo[u] > orRedNo[u]:
            defLost = defLost +1
    battleResult(attackLost,defLost)
    return [attackLost,defLost]

def battleResult(a,d):
    attacktext = ("Attackers lost {0} troops".format(str(a)))
    deftext = ("Defenders lost {0} troops".format(str(d)))
    attackLabel = Label(bottomFrameLeft,text = attacktext,font = buttonFont)
    defendlabel = Label(bottomFrameLeft,text = deftext, font = buttonFont, fg = "red")
    attackLabel.grid(row = 0, column = 5, padx = 120)
    defendlabel.grid(row = 1, column = 5, padx = 120)


def opposite(x):
    if x == "dark green":
        y = "white"
    if x == "red":
        y = "black"
    if x == "orange":
        y = "black"
    if x == "blue":
        y = "white"
    if x == "dark grey":
        y = "black"
    return y


def buildTopFrame(x):
    global players
    playerTurnText = "Player " + str(x+1) +"'s go!!"
    currentPlayerColour = players[x][0]
    bgcolour = opposite(currentPlayerColour)
    playerTurnLabel = Label(topFrameLeft,text = playerTurnText,font = buttonFont,bg = currentPlayerColour, fg = bgcolour)
    playerTurnLabel.grid(row = 0, column = 0,padx = 40)
    endGo = Button(topFrameLeft,text = "END GO",command=selectNextPlayer,bg = "red",font = textFont)
    endGo.grid(row = 0, column = 1,padx = 40)
    instructionsButton.grid(row = 0, column = 2,padx = 40)
    mapButton.grid(row = 0, column = 3, padx = 20)
    
def buildBottomFrame(x):
    global players,noOfCardsButton,noOfTroopsLabel
    currentPlayerColour = players[x][0]
    bgcolour = opposite(currentPlayerColour)
    noOfCardsText = "No. of Cards: " + str(players[x][1])
    noOfCardsButton = Button(bottomFrameRight,text = noOfCardsText,font = buttonFont,bg= currentPlayerColour, fg = bgcolour,command = cards, height = 1, width = 15, relief = RIDGE)
    noOfCardsButton.grid_forget()
    noOfCardsButton.grid(row = 0, column = 7,rowspan = 2)
    troops = players[playerTurn][2]
    noOfTroopsText = "No. of Troops: " + str(troops)
    noOfTroopsLabel = Label(bottomFrameRight,text = noOfTroopsText,font = buttonFont,bg= currentPlayerColour,fg = bgcolour, padx = 10, height = 1, width = 11, bd = 7.9)
    noOfTroopsLabel.grid_forget()
    noOfTroopsLabel.grid(row = 0, column = 6, rowspan = 2)


def attackDie(noOfDieAttack):
    global blackDie,firstBlackDielabel, secBlackDielabel,thirdBlackDielabel
    if noOfDieAttack == 1:
        firstNoBlack = random.randint(0,5)
        firstBlackDielabel = Label(bottomFrameLeft,image = blackDie[firstNoBlack],padx = 20)
        firstBlackDielabel.grid(row = 0, column = 0,rowspan = 2)
        secNoBlack = -1
        secBlackDielabel = Label(bottomFrameLeft,width = 5, height = 4,padx = 20)
        secBlackDielabel.grid(row = 0, column = 1,rowspan = 2)
        thirdNoBlack = -1
        thirdBlackDielabel = Label(bottomFrameLeft,width = 5, height = 4,padx = 20)
        thirdBlackDielabel.grid(row = 0, column = 2,rowspan = 2)
    if noOfDieAttack == 2:
        firstNoBlack = random.randint(0,5)
        firstBlackDielabel = Label(bottomFrameLeft,image = blackDie[firstNoBlack],padx = 20)
        firstBlackDielabel.grid(row = 0, column = 0,rowspan = 2)
        secNoBlack = random.randint(0,5)
        secBlackDielabel = Label(bottomFrameLeft,image = blackDie[secNoBlack],padx = 20)
        secBlackDielabel.grid(row = 0, column = 1,rowspan = 2)
        thirdNoBlack = -1
        thirdBlackDielabel = Label(bottomFrameLeft,width = 5, height = 4,padx = 20)
        thirdBlackDielabel.grid(row = 0, column = 2,rowspan = 2)
    if noOfDieAttack == 3:
        firstNoBlack = random.randint(0,5)
        firstBlackDielabel = Label(bottomFrameLeft,image = blackDie[firstNoBlack],padx = 20)
        firstBlackDielabel.grid(row = 0, column = 0,rowspan = 2)
        secNoBlack = random.randint(0,5)
        secBlackDielabel = Label(bottomFrameLeft,image = blackDie[secNoBlack],padx = 20)
        secBlackDielabel.grid(row = 0, column = 1,rowspan = 2)
        thirdNoBlack = random.randint(0,5)
        thirdBlackDielabel = Label(bottomFrameLeft,image = blackDie[thirdNoBlack],padx = 20)
        thirdBlackDielabel.grid(row = 0, column = 2,rowspan = 2)
    return [firstNoBlack,secNoBlack,thirdNoBlack]
    

def defendDie(noOfDieDef):
    global redDie,firstRedDielabel,secRedDielabel
    
    if noOfDieDef == 1:
        firstNoRed = random.randint(0,5)
        firstRedDielabel = Label(bottomFrameLeft,image = redDie[firstNoRed],padx = 20)
        firstRedDielabel.grid(row = 0, column = 3,rowspan = 2)
        secRedDielabel.grid_forget()
        secNoRed = -1
        secRedDielabel = Label(bottomFrameLeft,width = 5, height = 4,padx = 20)
        secRedDielabel.grid(row = 0, column = 4,rowspan = 2)
    if noOfDieDef == 2:
        firstNoRed = random.randint(0,5)
        firstRedDielabel = Label(bottomFrameLeft,image = redDie[firstNoRed],padx = 20)
        firstRedDielabel.grid(row = 0, column = 3,rowspan = 2)
        secNoRed = random.randint(0,5)
        secRedDielabel = Label(bottomFrameLeft,image = redDie[secNoRed],padx = 20)
        secRedDielabel.grid(row = 0, column = 4,rowspan = 2)
    return [firstNoRed,secNoRed]


def calculateTroops():
    global players, playerTurn, countries
    countriesOwned = 0
    continents = [[0,1,2,3,4,5,6,7,8],[9,10,11,12],[13,14,15,16,17,18,19],[20,21,22,23,24,25],[26,27,28,29,30,31,32,33,34,35,36,37],[38,39,40,41]]
    NA = True
    SA = True
    E = True
    Af = True
    As = True
    Au = True
    continentsBoo = [NA,SA,E,Af,As,Au]
    for y in range(42):
        if countries[y][1] == playerTurn:
            countriesOwned = countriesOwned +1
    if countriesOwned >=12:
        if countriesOwned<=14:
            players[playerTurn][2] = players[playerTurn][2] +1
        elif countriesOwned<=17:
            players[playerTurn][2] = players[playerTurn][2] +2
        elif countriesOwned<=20:
            players[playerTurn][2] = players[playerTurn][2] +3
        elif countriesOwned<=23:
            players[playerTurn][2] = players[playerTurn][2] +4
        elif countriesOwned<=26:
            players[playerTurn][2] = players[playerTurn][2] +5
        elif countriesOwned<=29:
            players[playerTurn][2] = players[playerTurn][2] +6
        elif countriesOwned<=32:
            players[playerTurn][2] = players[playerTurn][2] +7
        elif countriesOwned<=35:
            players[playerTurn][2] = players[playerTurn][2] +8
        elif countriesOwned<=39:
            players[playerTurn][2] = players[playerTurn][2] +9
        elif countriesOwned<=42:
            players[playerTurn][2] = players[playerTurn][2] +10
    for f in range(6):
        for c in continents[f]:
            if playerTurn != countries[c][1]:
                continentsBoo[f] = False
    if continentsBoo[0] == True:
        players[playerTurn][2] = players[playerTurn][2] +5
    if continentsBoo[1] == True:
        players[playerTurn][2] = players[playerTurn][2] +2
    if continentsBoo[2] == True:
        players[playerTurn][2] = players[playerTurn][2] +5
    if continentsBoo[3] == True:
        players[playerTurn][2] = players[playerTurn][2] +3
    if continentsBoo[4] == True:
        players[playerTurn][2] = players[playerTurn][2] +7
    if continentsBoo[5] == True:
        players[playerTurn][2] = players[playerTurn][2] +2
                


def cards():
    global players, playerTurn,placeTroopsPart
    noOfCards = players[playerTurn][1]
    if placeTroopsPart == True:
        if noOfCards > 0 :
            gameFrame.pack_forget()
            cardFrame.pack(fill = BOTH, expand = True)
            for j in range(10):
                cardButton[j].grid_forget()
            for t in range(noOfCards):
                if t <=4:
                    cardButton[t].grid(row=1,column = t)
                else:
                    cardButton[t].grid(row=2,column = t-5)
            
    
def onecard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 1
    players[playerTurn][2] = players[playerTurn][2] + 1
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def twocard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 2
    players[playerTurn][2] = players[playerTurn][2] + 2
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def threecard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 3
    players[playerTurn][2] = players[playerTurn][2] + 4
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def fourcard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 4
    players[playerTurn][2] = players[playerTurn][2] + 7
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def fivecard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 5
    players[playerTurn][2] = players[playerTurn][2] + 10
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def sixcard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 6
    players[playerTurn][2] = players[playerTurn][2] + 13
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def sevencard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 7
    players[playerTurn][2] = players[playerTurn][2] + 17
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def eightcard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 8
    players[playerTurn][2] = players[playerTurn][2] + 21
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

def ninecard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 9
    players[playerTurn][2] = players[playerTurn][2] + 25
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)
    
def tencard():
    global players,playerTurn
    players[playerTurn][1] = players[playerTurn][1] - 10
    players[playerTurn][2] = players[playerTurn][2] + 30
    cardFrame.pack_forget()
    clearScreen()
    buildBottomFrame(playerTurn)
    gameFrame.pack(fill = BOTH, expand = True)

    
    
def playersClearUp():
    global players, noOfPlayers
    while len(players) > noOfPlayers:
        temp = players.pop()
    


def instructions():
    gameFrame.pack_forget()
    instructionFrame.pack(fill = BOTH, expand = True)

def back():
    instructionFrame.pack_forget()
    gameFrame.pack(fill = BOTH, expand= True)
    
def packColourButtons(x):
    for r in range(5):
        colourButtons[r].grid_forget()
    if x[0] == "dark green":
        colourButtons[0].grid(row = 0,column = 0)
    if x[1] == "red":
        colourButtons[1].grid(row = 0,column = 2)
    if x[2] == "orange":
        colourButtons[2].grid(row = 0,column = 4)
    if x[3] == "blue":
        colourButtons[3].grid(row = 1,column = 1)
    if x[4] == "dark grey":
        colourButtons[4].grid(row = 1,column = 3)
  
def greenColour():
    global coloursLeft, instance
    coloursLeft[0] = 0
    players[instance][0] = "dark green"
    instance = instance + 1
    playerColours()

    
def redColour():
    global coloursLeft, instance
    coloursLeft[1] = 0
    players[instance][0] = "red"
    instance = instance + 1
    playerColours()
    
def yellowColour():
    global coloursLeft, instance
    coloursLeft[2] = 0
    players[instance][0] = "orange"
    instance = instance + 1
    playerColours()
    
def blueColour():
    global coloursLeft, instance
    coloursLeft[3] = 0
    players[instance][0] = "blue"
    instance = instance + 1
    playerColours()
    
def greyColour():
    global coloursLeft, instance
    coloursLeft[4] = 0
    players[instance][0] = "dark grey"
    instance = instance + 1
    playerColours()

def twoPlayer():
    global noOfPlayers
    noOfPlayers = 2
    playerColours()

def threePlayer():
    global noOfPlayers
    noOfPlayers = 3
    playerColours()

def fourPlayer():
    global noOfPlayers
    noOfPlayers = 4
    playerColours()

def fivePlayer():
    global noOfPlayers
    noOfPlayers = 5
    playerColours()


def countryAllo():
    global players, noOfPlayers, countries
    countriesLeft = []
    for z in range(42):
        countriesLeft.append(z)
    instance = 0
    while len(countriesLeft) >0:
        tempCount = random.randint(0,len(countriesLeft)-1)
        country = countriesLeft[tempCount]
        if instance < (noOfPlayers-1):
            countries[country][1] = instance
            instance = instance +1
        elif instance == (noOfPlayers-1):
            countries[country][1] = instance
            instance = 0
        countriesLeft.remove(country)
    
            
        
def dismap():
    gameFrame.pack_forget()
    mapFrame.pack(fill = BOTH, expand = True)

def back2():
    mapFrame.pack_forget()
    gameFrame.pack(fill = BOTH, expand= True)


def countriesOwnedCal():
    global players,playerTurn,countries
    owned = []
    for u in range(42):
        if countries[u][1] == playerTurn:
            owned.append(u)
    return owned

def ownedLinksA(x,z):
    global countries
    ownedLink = []
    for e in z:
        if e in countries[x][3]:
            ownedLink.append(e)
    return ownedLink

    
def linked(x,z):
    global countries,linkedCount,done
    link = False
    ownedLinks = ownedLinksA(x,z)
    done.append(x)
    for w in ownedLinks:
        linkedCount.append(w)
    for v in linkedCount:
        if v not in done:
            linked(v,z)



def movePieces():
    global selected,countries,permitMove,linkedCount
    source = selected[0]
    target = selected[1]
    countriesOwned = countriesOwnedCal()
    linked(source,countriesOwned)
    if target in linkedCount:
        permitMove = True
        movePool(selected)

def movePool(x):
    global countries,players,playerTurn
    first = x[0]
    second = x[1]
    overall = countries[first][2] + countries[second][2] -2
    countries[first][2] = 1
    countries[second][2] = 1
    players[playerTurn][2] = players[playerTurn][2]+ overall
    
def war():
    global selected,countries,players,playerTurn,cardGiven
    attacker = selected[1]
    defender = selected[0]
    if defender in countries[attacker][3]:
        if countries[defender][2] < 2:
            x = 1
        else:
            x = 2
        if countries[attacker][2] == 2:
            y = 1
        elif countries[attacker][2] ==3:
            y = 2
        else:
            y = 3
        outcome = battle(y,x)

        attackLost = outcome[0]
        defendLost = outcome[1]
        countries[attacker][2] = countries[attacker][2] -attackLost
        countries[defender][2] = countries[defender][2] -defendLost
        
        if countries[defender][2] <= 0:
            cardGiven = True
            countries[defender][1] = playerTurn
            countries[defender][2] = 1
            countries[attacker][2] = countries[attacker][2]-1
            spare = countries[attacker][2]-1
            countries[attacker][2] = countries[attacker][2]-spare
            if spare != 0:
                pool(selected,spare)
        
    
def pool(selected, spare):
    global players, playerTurn,aftermath
    players[playerTurn][2] = players[playerTurn][2] + spare
    aftermath = True
                      



                      
def countryTurn(x):
    global selected,countries,players,playerTurn,placeTroopsPart,aftermath,permitMove
    if permitMove == True:
        if countries[x][0] in selected:
            countries[x][2] = countries[x][2]+1
            players[playerTurn][2] = players[playerTurn][2]-1
            refresh()
            if players[playerTurn][2] == 0:
                permitMove = False
                selected = [42,42]
                refresh()
                selectNextPlayer()
    elif aftermath == True:
         if countries[x][0] in selected:
            countries[x][2] = countries[x][2]+1
            players[playerTurn][2] = players[playerTurn][2]-1
            if players[playerTurn][2] == 0:
                aftermath = False
                selected = [42,42]
            refresh()             
    elif placeTroopsPart == True:
        if countries[x][1] == playerTurn:
            countries[x][2] = countries[x][2]+1
            players[playerTurn][2] = players[playerTurn][2]-1
            if players[playerTurn][2] == 0:
                placeTroopsPart = False
            refresh()
    else:
        selected[1] = selected[0]
        selected[0] = x
        if selected[1] != 42:
            ownedCountries = countriesOwnedCal()
            if selected[1] in ownedCountries:
                if selected[0] in ownedCountries:
                    if selected[0] != selected[1]:
                        movePieces()
                        refresh()
                else:
                    if countries[(selected[1])][2] > 1:
                        war()
                        refresh()
                
            
def clearDice():
    global firstRedDielabel, secRedDielabel, firstBlackDielabel,secBlackDielabel,thirdBlackDielabel
    #firstRedDielabel.grid_forget()
    #secRedDielabel.grid_forget()
    #firstBlackDielabel.grid_forget()
    #secBlackDielabel.grid_forget()
    #thirdBlackDielabel.grid_forget()
            
def Alaska():
    countryTurn(0)
    clearDice()
            
def NorthWestTer():
    countryTurn(1)
    clearDice()
    
def Greenland():
    countryTurn(2)
    clearDice()
    
def Alberta():
    countryTurn(3)
    clearDice()
    
def Orlando():
    countryTurn(4)
    clearDice()
    
def Qubec():
    countryTurn(5)
    clearDice()
    
def WesternUS():
    countryTurn(6)
    clearDice()
    
def EasternUS():
    countryTurn(7)
    clearDice()
    
def CentralAmerica():
    countryTurn(8)
    clearDice()
    
def Venezuela():
    countryTurn(9)
    clearDice()
    
def Peru():
    countryTurn(10)
    clearDice()
    
def Brazil():
    countryTurn(11)
    clearDice()
    
def Argentina():
    countryTurn(12)
    clearDice()
    
def Iceland():
    countryTurn(13)
    clearDice
    
def Scandenavia():
    countryTurn(14)
    clearDice
    
def Russia():
    countryTurn(15)
    clearDice
    
def GB():
    countryTurn(16)
    clearDice
    
def NorthEurope():
    countryTurn(17)
    clearDice
    
def WesternEurope():
    countryTurn(18)
    clearDice
    
def SouthernEurope():
    countryTurn(19)
    clearDice
    
def NorthAfrica():
    countryTurn(20)
    clearDice
    
def Egypt():
    countryTurn(21)
    clearDice
    
def Congo():
    countryTurn(22)
    clearDice
    
def EastAfrica():
    countryTurn(23)
    clearDice
    
def SouthAfrica():
    countryTurn(24)
    clearDice
    
def Madagascar():
    countryTurn(25)
    clearDice
    
def Ural():
    countryTurn(26)
    clearDice
    
def Serbia():
    countryTurn(27)
    clearDice
    
def Yakutsk():
    countryTurn(28)
    clearDice
    
def Kamchatka():
    countryTurn(29)
    clearDice
    
def Afghanistan():
    countryTurn(30)
    clearDice
    
def Irkutsk():
    countryTurn(31)
    clearDice
    
def Japan():
    countryTurn(32)
    clearDice
    
def Mongolia():
    countryTurn(33)
    clearDice
    
def MiddleEast():
    countryTurn(34)
    clearDice
    
def India():
    countryTurn(35)
    clearDice
    
def China():
    countryTurn(36)
    clearDice
    
def Siam():
    countryTurn(37)
    clearDice
    
def Indonesia():
    countryTurn(38)
    clearDice
    
def NewGuinea():
    countryTurn(39)
    clearDice
    
def WesternAustralia():
    countryTurn(40)
    clearDice
    
def EasternAustralia():
    countryTurn(41)
    clearDice
    


main = Tk()

titleFont = ("Times New Roman",25)
medFont = ("Times New Roman",20,"bold")
buttonFont = ("Times New Roman",15,"bold")
textFont = ("Times New Roman",13,"bold")
main.title("RISK")


w, h = main.winfo_screenwidth(), main.winfo_screenheight()
main.overrideredirect(1)
main.geometry("%dx%d+0+0" % (w, h))






firstRedDielabel = Label(main)
secRedDielabel = Label(main)
firstBlackDielabel = Label(main)
secBlackDielabel = Label(main)
thirdBlackDielabel = Label(main)
firstBlackDielabel.grid_forget()
secBlackDielabel.grid_forget()
thirdBlackDielabel.grid_forget()
firstRedDielabel.grid_forget()
secRedDielabel.grid_forget()





blackDie1 = PhotoImage(file= "DiceCube1.1.gif")
blackDie2 = PhotoImage(file= "DiceCube2.1.gif")
blackDie3 = PhotoImage(file= "DiceCube3.1.gif")
blackDie4 = PhotoImage(file= "DiceCube4.1.gif")
blackDie5 = PhotoImage(file= "DiceCube5.1.gif")
blackDie6 = PhotoImage(file= "DiceCube6.1.gif")

blackDie = [blackDie1,blackDie2,blackDie3,blackDie4,blackDie5,blackDie6]

redDie1 = PhotoImage(file = "RedDie1.gif")
redDie2 = PhotoImage(file = "RedDie2.gif")
redDie3 = PhotoImage(file = "RedDie3.gif")
redDie4 = PhotoImage(file = "RedDie4.gif")
redDie5 = PhotoImage(file = "RedDie5.gif")
redDie6 = PhotoImage(file = "RedDie6.gif")

redDie = [redDie1,redDie2,redDie3,redDie4,redDie5,redDie6]

mappic = PhotoImage(file = "Map.gif")

menu = Frame(main)
title = Label(menu, text= "RISK",font = titleFont,height = 5)
title.grid(row = 0,column = 0)
playerQ = Label(menu,text = "How many players are there?",font = buttonFont)
playerQ.grid(row = 1, column = 0)
buttonFrame = Frame(menu)
buttonFrame.grid(row = 2,column = 0)
PlayerTwo = Button(buttonFrame,text = "2", font = buttonFont,width = 8,height = 2,bg = "blue",command = twoPlayer)
PlayerTwo.grid(row = 2, column = 1)
PlayerThree = Button(buttonFrame,text = "3", font = buttonFont,width = 8,height = 2,bg = "blue",command = threePlayer)
PlayerThree.grid(row = 3, column = 2)
PlayerFour = Button(buttonFrame,text = "4", font = buttonFont,width = 8,height = 2,bg = "blue",command = fourPlayer)
PlayerFour.grid(row = 2, column = 3)
PlayerFive = Button(buttonFrame,text = "5", font = buttonFont,width = 8,height = 2,bg = "blue",command = fivePlayer)
PlayerFive.grid(row = 3, column = 4)





colours = Frame(main)
colourFramesTop = [0,0,0,0,0]
coloursList = ["dark green","red","orange","blue","dark grey"]
for i in range(5):
    colourFramesTop[i] = Frame(colours)
    labelText = "Player " + (str(i+1)) +" pick a colour:"
    playerpickLabel = Label(colourFramesTop[i],text = labelText,font = buttonFont)
    playerpickLabel.grid(row = 0,column = 1,pady = 50,columnspan = 3)

colourButtons = [0,0,0,0,0]
colourFrameBottom = Frame(colours)
colourFrameBottom.grid(row = 1,column = 0)
colourButtons[0] = Button(colourFrameBottom,bg = coloursList[0], width = 8,height = 2,font = buttonFont,command = greenColour)
colourButtons[1] = Button(colourFrameBottom,bg = coloursList[1], width = 8,height = 2,font = buttonFont,command = redColour)
colourButtons[2] = Button(colourFrameBottom,bg = coloursList[2], width = 8,height = 2,font = buttonFont,command = yellowColour)
colourButtons[3] = Button(colourFrameBottom,bg = coloursList[3], width = 8,height = 2,font = buttonFont,command = blueColour)
colourButtons[4] = Button(colourFrameBottom,bg = coloursList[4], width = 8,height = 2,font = buttonFont,command = greyColour)
    



gameFrame = Frame(main)
topFrame = Frame(gameFrame,height = 85)
topFrame.pack(fill = X)
board = Frame(gameFrame, bg = "#009475")
board.pack(fill = BOTH, expand = True)
bottomFrame = Frame(gameFrame, height = 85)
bottomFrame.pack(fill=X)

topFrameLeft = Frame(topFrame)
topFrameLeft.pack(side = LEFT)
bottomFrameLeft = Frame(bottomFrame)
bottomFrameRight = Frame(bottomFrame)
bottomFrameLeft.pack(side = LEFT)
bottomFrameRight.pack(side = RIGHT)

#top frame set up
instructionsButton = Button(topFrameLeft, text = "Instuctions",bg = "red", font = textFont ,command = instructions)

instructionFrame = Frame(main)
instructionText = "-------------------------------------------------------------------------   Instructions    -------------------------------------------------------------------------             * To place troops, click on any country owned by your player, this will place a single troop on that country. The counter in the corner indicates how many are left *                                                                                                                                                                                             *The amount of troops depends on how many countries you own, if you own any full continents or cards you trade in.*                                                                                                                           *To trade in a set of cards, click on the counter in the bottom corner, this will take you to a page where you can select how many.*                                                                                                                               *Once all your troops are placed, click on a country of yours you wish to attack from. Once selected click on another country adjacent to yours to attack*                                                                                                                                                                                                                                                                        *The display in the bottom corner shows the outcome of the battle.*                                                                                                                                                                        *An attack will use as many troops as it can, and a defending country will use as many troops as they can.*                                                                                                                                                                              *To attack again, simply repeat, the number in the country shows how many troops there are present there.*                                                                                                                                                                         *If an attack is unsuccessful the remaining troops will fall back to their original country.*                                                                                                                                                                       * If an attack is successful, then the entire original army (barring those standing guard) will be replaced into the pool to be spread across the attacking country and the newly defeated one by clicking on them respectivly.*                                                                                                                                                                       *Once you are finished attacking, to manoeuvre you troops, click on a country already owned by you and then another also owned by you which is connected to it, these troops will then be put into the pool to be spread out between the two countries.*                                                                                                                                                                        *Once you have finished you move, click the end go button and pass control to the next player*                                                                                                                                                                        *When the game is finished, click the end game button to exit.*                                                                                                                                                                                                                *To view the map for boundary lines, click the map button at the top. Click anywhere to exit*                                                                                                                                                                                     *Click anywhere to exit instructions*"
instructionLabel = Button(instructionFrame,font = textFont,text = instructionText,command = back, wraplength = 1000, fg = "dark green")
instructionLabel.pack(fill = BOTH, expand = True)
endGameFrame = Frame(topFrame)
endGameFrame.pack(side = RIGHT, padx = 10)
endGameButton = Button(endGameFrame, text = "END GAME", command = endGame,bg = "red", font = textFont)
endGameButton.pack(side = RIGHT)

mapButton = Button(topFrameLeft, text = "Map", bg = "red", font = textFont, command = dismap)
mapFrame = Frame(main)
mapPage = Button(mapFrame,image = mappic, command = back2, bg = "#009475")
mapPage.pack(fill = BOTH, expand = True)


cardFrame = Frame(main)
cardFrameTop =Frame(cardFrame)
cardFrameTop.pack()
cardFrameBottom =Frame(cardFrame)
cardFrameBottom.pack()
cardlabel = Label(cardFrameTop, text = "How many cards would you like to trade in?", font = buttonFont)
cardlabel.grid(row = 0, column = 0, columnspan = 5, pady = 100)
cardButton = [0,0,0,0,0,0,0,0,0,0]
cardButton[0] = Button(cardFrameBottom,text = "1 - 1 Troop",command = onecard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[1] = Button(cardFrameBottom,text = "2 - 2 Troops",command = twocard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[2] = Button(cardFrameBottom,text = "3 - 4 Troops",command = threecard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[3] = Button(cardFrameBottom,text = "4 - 7 Troops",command = fourcard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[4] = Button(cardFrameBottom,text = "5 - 10 Troops",command = fivecard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[5] = Button(cardFrameBottom,text = "6 - 13 Troops",command = sixcard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[6] = Button(cardFrameBottom,text = "7 - 17 Troops",command = sevencard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[7] = Button(cardFrameBottom,text = "8 - 21 Troops",command = eightcard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[8] = Button(cardFrameBottom,text = "9 - 25 Troops",command = ninecard,height = 3,width = 15,font = textFont,bg = "red")
cardButton[9] = Button(cardFrameBottom,text = "10 - 30 Troops",command = tencard,height = 3,width = 15,font = textFont,bg = "red")


def buildMap():
    global players, countries
    countryColours = [[],[]]
    for n in range(42):
        if countries[n][1] == 0:
            colour = players[0][0]
            countryColours[0].append(colour)
            textColour = opposite(colour)
            countryColours[1].append(textColour)
        elif countries[n][1] == 1:
            colour = players[1][0]
            countryColours[0].append(colour)
            textColour = opposite(colour)
            countryColours[1].append(textColour)
        elif countries[n][1] == 2:
            colour = players[2][0]
            countryColours[0].append(colour)
            textColour = opposite(colour)
            countryColours[1].append(textColour)
        elif countries[n][1] == 3:
            colour = players[3][0]
            countryColours[0].append(colour)
            textColour = opposite(colour)
            countryColours[1].append(textColour)
        elif countries[n][1] == 4:
            colour = players[4][0]
            countryColours[0].append(colour)
            textColour = opposite(colour)
            countryColours[1].append(textColour)
    
    sea = "#009475"

    
    
    America = Frame(board, width = 1000,height = 300)
    America.place(x = 100, y = 25)
    NAmerica1 = Frame(America, height = 14, bg = sea)
    NAmerica1.pack(fill = X, expand = True)
    NAmerica2 = Frame(America, height = 30, bg = sea )
    NAmerica2.pack(fill = X, expand = True)
    NAmerica3 = Frame(America, height = 45, bg = sea)
    NAmerica3.pack(fill = X, expand = True)
    NAmerica4 = Frame(America, height = 45, bg = sea)
    NAmerica4.pack(fill = X, expand = True)
    NAmerica5 = Frame(America, height = 45, bg = sea)
    NAmerica5.pack(fill = X, expand = True)
    
    NAmerica11 = Frame(NAmerica1, width = 280,height = 14, bg = sea)
    NAmerica11.pack(fill = X, expand = True, side = LEFT) 
    greenLand = Button(NAmerica1, width = 10, height = 3, text = "Greenland ({0})".format(countries[2][2]),font = textFont,bg = countryColours[0][2],wraplength = 100,fg = countryColours[1][2], command = Greenland)
     
    alaska = Button(NAmerica2,width = 5, height = 2, text = "Alaska ({0})".format(countries[0][2]), font = textFont,wraplength = 50,bg = countryColours[0][0],fg = countryColours[1][0], command = Alaska )
    NWTerritory = Button(NAmerica2,width = 11, height = 2, text = "NW Territory ({0})".format(countries[1][2]),wraplength = 110 ,font = textFont,bg = countryColours[0][1],fg = countryColours[1][1], command =  NorthWestTer)

    NAmerica31 = Frame(NAmerica3, width = 40,height = 14, bg = sea)
    NAmerica31.pack(side = LEFT)
    alberta = Button(NAmerica3, width = 6, height = 3, text = "Alberta ({0})".format(countries[3][2]),font = textFont,wraplength = 60,bg = countryColours[0][3],fg = countryColours[1][3], command = Alberta )
    orlando = Button(NAmerica3, width = 11, height = 3, text = "Orlando ({0})".format(countries[4][2]),font = textFont,wraplength = 110,bg = countryColours[0][4],fg = countryColours[1][4], command = Orlando )
    qubec = Button(NAmerica3, width = 6, height = 3, text = "Qubec ({0})".format(countries[5][2]),font = textFont,wraplength = 60,bg = countryColours[0][5],fg = countryColours[1][5], command = Qubec )

    NAmerica41 = Frame(NAmerica4, width = 72,height = 14, bg = sea)
    NAmerica41.pack(side = LEFT)
    WUS = Button(NAmerica4, width = 9, height = 4, text = "Western United States ({0})".format(countries[6][2]),font = textFont,wraplength = 80,bg = countryColours[0][6],fg = countryColours[1][6] , command = WesternUS)
    EUS = Button(NAmerica4, width = 9, height = 4, text = "Eastern United States ({0})".format(countries[7][2]),font = textFont,wraplength = 80,bg = countryColours[0][7],fg = countryColours[1][7], command = EasternUS )

    NAmerica51 = Frame(NAmerica5, width = 120,height = 14, bg = sea)
    NAmerica51.pack(side = LEFT)
    CAmerica = Button(NAmerica5, width = 7, height = 3, text = "Central America ({0})".format(countries[8][2]),font = textFont,wraplength = 65,bg = countryColours[0][8],fg = countryColours[1][8], command =  CentralAmerica)



    SAmerica1 = Frame(America, height = 14, bg = sea)
    SAmerica1.pack(fill = X, expand = True)
    SAmerica2 = Frame(America, height = 30, bg = sea )
    SAmerica2.pack(fill = X, expand = True)
    SAmerica3 = Frame(America, height = 45, bg = sea)
    SAmerica3.pack(fill = X, expand = True)


    SAmerica11 = Frame(SAmerica1, width = 152,height = 14, bg = sea)
    SAmerica11.pack(side = LEFT)
    venezuela =  Button(SAmerica1, width = 9, height = 2, text = "Venezuela ({0})".format(countries[9][2]),font = textFont,wraplength = 90,bg = countryColours[0][9],fg = countryColours[1][9], command =  Venezuela)


    SAmerica21 = Frame(SAmerica2, width = 120,height = 14, bg = sea)
    SAmerica21.pack(side = LEFT)
    peru =  Button(SAmerica2, width = 5, height = 5, text = "Peru ({0})".format(countries[10][2]),font = textFont,wraplength = 50,bg = countryColours[0][10],fg = countryColours[1][10] , command = Peru)
    brazil =  Button(SAmerica2, width = 11, height = 5, text = "Brazil ({0})".format(countries[11][2]),font = textFont,wraplength = 110,bg = countryColours[0][11],fg = countryColours[1][11], command =  Brazil)

    SAmerica31 = Frame(SAmerica3, width = 160,height = 14, bg = sea)
    SAmerica31.pack(side = LEFT)
    argentina =  Button(SAmerica3, width = 7, height = 5, text = "Argentina ({0})".format(countries[12][2]),font = textFont, wraplength = 75,bg = countryColours[0][12],fg = countryColours[1][12], command = Argentina )






    Europe = Frame(board, width = 1000,height = 300, bg = sea)
    Europe.place(x = 570, y = 50)
    
    WEurope = Frame(Europe)
    WEurope.pack(side = LEFT)

    
    NWEurope = Frame(WEurope, bg = sea)
    NWEurope.pack(side = TOP)



    NWWEurope = Frame(NWEurope, bg = sea)
    NWWEurope.pack(side = LEFT)

    NWWEurope1 = Frame(NWWEurope,width = 100, height = 20,bg = sea)
    NWWEurope1.pack()

    NWWEurope2 = Frame(NWWEurope,width = 100, height = 20,bg = sea)
    NWWEurope2.pack()

    NWWEurope3 = Frame(NWWEurope,width = 100, height = 40,bg = sea)
    NWWEurope3.pack()

    NWWEurope4 = Frame(NWWEurope,width = 100, height = 20,bg = sea)
    NWWEurope4.pack()

    NWWEurope5 = Frame(NWWEurope,width = 100, height = 30,bg = sea)
    NWWEurope5.pack()

        
    NWWEurope21 = Frame(NWWEurope2,width = 10,bg= sea)
    NWWEurope21.pack(side = LEFT)
    iceland = Button(NWWEurope2, width = 6, height = 2, text = "Iceland ({0})".format(countries[13][2]),wraplength = 60,font = textFont,bg = countryColours[0][13],fg = countryColours[1][13], command = Iceland )

    NWWEurope41 = Frame(NWWEurope4,width = 45,bg= sea)
    NWWEurope41.pack(side = LEFT)
    gb = Button(NWWEurope4, width = 3, height = 2, text = "GB ({0})".format(countries[16][2]),font = textFont,bg = countryColours[0][16],fg = countryColours[1][16] , command = GB,wraplength = 30)




    NWEEurope = Frame(NWEurope, bg = sea)
    NWEEurope.pack(side = LEFT, anchor = N)

    NWEEurope1 = Frame(NWEEurope,width = 80, height = 20,bg = sea)
    NWEEurope1.pack(anchor = N)

    NWEEurope2 = Frame(NWEEurope,width = 80, height = 20,bg = sea)
    NWEEurope2.pack()

    NWEEurope11 = Frame(NWEEurope1,width = 10,bg= sea)
    NWEEurope11.pack(side = LEFT, anchor = N)
    scandinavia = Button(NWEEurope1, width = 8, height = 3, text = "Scandinavia  ({0})".format(countries[14][2]),font = textFont,wraplength = 90,bg = countryColours[0][14],fg = countryColours[1][14] , command = Scandenavia)
    

    northEurope = Button(NWEEurope2, width = 9, height = 6, text = "North Europe ({0})".format(countries[17][2]),font = textFont, wraplength = 100,bg = countryColours[0][17],fg = countryColours[1][17] , command = NorthEurope)


    CWEurope1 = Frame(WEurope, bg = sea)
    CWEurope1.pack(fill = X)

    
    southEurope = Button(CWEurope1, width = 7, height = 3, text = "Southern Europe ({0})".format(countries[19][2]),font = textFont, wraplength = 100,bg = countryColours[0][19],fg = countryColours[1][19] , command = SouthernEurope)
    westEurope = Button(CWEurope1, width = 7, height = 3, text = "Western Europe ({0})".format(countries[18][2]),font = textFont, wraplength = 100,bg = countryColours[0][18],fg = countryColours[1][18] , command = WesternEurope)

    CWEurope2 = Frame(WEurope, bg = sea,height = 20)
    CWEurope2.pack(fill = X)

    CWEurope3 = Frame(WEurope, bg = sea,height = 20)
    CWEurope3.pack(fill = X)

    ECWEurope3 = Frame(CWEurope3, bg= sea)
    ECWEurope3.pack(side = LEFT)



    ECWEurope31 = Frame(ECWEurope3, bg = sea)
    ECWEurope31.pack()

    ECWEurope32 = Frame(ECWEurope3, bg = sea)
    ECWEurope32.pack()
    
    northAfrica = Button(ECWEurope31, width = 8, height = 3, text = "North Africa ({0})".format(countries[20][2]),font = textFont, wraplength = 60,bg = countryColours[0][20],fg = countryColours[1][20], command =  NorthAfrica)

    ECWEurope321 = Frame(ECWEurope32, bg = sea, width = 20)
    ECWEurope321.pack(side = LEFT)

    congo = Button(ECWEurope32, width = 6, height = 3, text = "Congo ({0})".format(countries[22][2]),font = textFont, wraplength = 60,bg = countryColours[0][22],fg = countryColours[1][22] , command = Congo)

    WCWEurope3 = Frame(CWEurope3, bg= sea)
    WCWEurope3.pack(side = LEFT)

    WCWEurope31 = Frame(WCWEurope3, bg = sea)
    WCWEurope31.pack()

    WCWEurope32 = Frame(WCWEurope3, bg = sea)
    WCWEurope32.pack(anchor = W)

    egypt = Button(WCWEurope31,width = 10, height = 2, text = "Egypt ({0})".format(countries[21][2]),font = textFont, wraplength = 100,bg = countryColours[0][21],fg = countryColours[1][21] , command = Egypt)


    eastAfrica = Button(WCWEurope32,width = 8, height = 4, text = "East Africa ({0})".format(countries[23][2]),font = textFont, wraplength = 100,bg = countryColours[0][23],fg = countryColours[1][23], command =  EastAfrica)

    SWEurope = Frame(WEurope, bg = sea)
    SWEurope.pack(fill = X , expand = True)


    SWEurope1 = Frame(SWEurope, bg = sea, width = 52)
    SWEurope1.pack(side = LEFT)

    southAfrica = Button(SWEurope,width = 7, height = 4, text = "South Africa ({0})".format(countries[24][2]),font = textFont, wraplength = 60,bg = countryColours[0][24],fg = countryColours[1][24] , command = SouthAfrica)  


    CEurope = Frame(Europe, bg = sea)
    CEurope.pack(fill = Y, expand = True,anchor = N, side = LEFT)

    NCEurope = Frame(CEurope, bg = sea)
    NCEurope.pack()

    SCEurope = Frame(CEurope, bg = sea)
    SCEurope.pack(anchor = W)

    NCEurope1 = Frame(NCEurope, bg = sea)
    NCEurope1.pack(side = LEFT)

    russia = Button(NCEurope1,width = 8, height = 11, text = "Russia ({0})".format(countries[15][2]),font = textFont, wraplength = 60,bg = countryColours[0][15],fg = countryColours[1][15] , command = Russia)

    NCEurope2 = Frame(NCEurope, bg = sea)
    NCEurope2.pack(side = LEFT, anchor = S)

    ural = Button(NCEurope2,width = 6, height = 5, text = "Ural ({0})".format(countries[26][2]),font = textFont, wraplength = 60,bg = countryColours[0][26],fg = countryColours[1][26] , command = Ural)
    afghanistan = Button(NCEurope2,width = 6, height = 5, text = "Afghanistan ({0})".format(countries[30][2]),font = textFont, wraplength = 60,bg = countryColours[0][30],fg = countryColours[1][30], command = Afghanistan )

    NCEurope3 = Frame(NCEurope, bg = sea)
    NCEurope3.pack(side = LEFT, anchor = N)

    serbia = Button(NCEurope3,width = 5, height = 9, text = "Serbia ({0})".format(countries[27][2]),font = textFont, wraplength = 60,bg = countryColours[0][27],fg = countryColours[1][27] , command = Serbia )


    middleEast = Button(SCEurope,width = 10, height = 8, text = "Middle East ({0})".format(countries[34][2]),font = textFont, wraplength = 60,bg = countryColours[0][34],fg = countryColours[1][34], command =  MiddleEast)
    india = Button(SCEurope,width = 10, height = 6, text = "India ({0})".format(countries[35][2]),font = textFont, wraplength = 60,bg = countryColours[0][35],fg = countryColours[1][35], command = India )

    SSCEurope = Frame(CEurope, bg = sea)
    SSCEurope.pack(fill = BOTH, expand = True)
    
    madagascar = Button(SSCEurope, width = 3, height = 3,bg = countryColours[0][25],fg = countryColours[1][25], command = Madagascar)
    madagascarLabel = Label(SSCEurope, text = "Madagascar ({0})".format(countries[25][2]),font = textFont, bg = sea, fg = countryColours[1][25] )
    SSCEurope1 = Frame(SSCEurope, bg = sea, height = 40)
    SSCEurope1.pack(anchor = W)


    EEurope = Frame(Europe, bg = sea)
    EEurope.pack(side = LEFT, anchor = N)

    NEEurope = Frame(EEurope, bg = sea)
    NEEurope.pack(anchor = N)

    NEEurope1 = Frame(NEEurope, bg = sea)
    NEEurope1.pack(side = LEFT)

    yakutsk = Button(NEEurope1,width = 7, height = 3, text = "Yakutsk ({0})".format(countries[28][2]),font = textFont, wraplength = 60,bg = countryColours[0][28],fg = countryColours[1][28] , command = Yakutsk)
    irkutsk = Button(NEEurope1,width = 7, height = 2, text = "Irkutsk ({0})".format(countries[31][2]),font = textFont, wraplength = 60,bg = countryColours[0][31],fg = countryColours[1][31] , command = Irkutsk)


    NEEurope2 = Frame(NEEurope, bg = sea)
    NEEurope2.pack(side = LEFT)

    kamchatka = Button(NEEurope2,width = 7, height = 5, text = "Kamchatka ({0})".format(countries[29][2]),font = textFont, wraplength = 60,bg = countryColours[0][29],fg = countryColours[1][29] , command = Kamchatka)


    EEurope2 = Frame(EEurope, bg = sea)
    EEurope2.pack(anchor = W)

    mongolia = Button(EEurope2,width = 11, height = 2, text = "Mongolia ({0})".format(countries[33][2]),font = textFont, wraplength = 80,bg = countryColours[0][33],fg = countryColours[1][33] , command = Mongolia)
    EEurope25 = Frame(EEurope, bg = sea)
    EEurope25.pack( anchor = W)
    china = Button(EEurope25,width = 14, height = 4, text = "China ({0})".format(countries[36][2]),font = textFont, wraplength = 60,bg = countryColours[0][36],fg = countryColours[1][36], command = China )

    EEurope3 = Frame(EEurope, bg = sea)
    EEurope3.pack(anchor = W)
    siam = Button(EEurope3,width = 7, height = 2, text = "Siam ({0})".format(countries[37][2]),font = textFont, wraplength = 60,bg = countryColours[0][37],fg = countryColours[1][37] , command = Siam)

    EEurope31 = Frame(EEurope3, bg = sea, height = 30)
    EEurope31.pack(side = RIGHT)
    EEurope4 = Frame(EEurope, bg = sea, height = 80)
    EEurope4.pack(fill = X , expand = True)

    EEurope5 = Frame(EEurope, bg = sea)
    EEurope5.pack( fill = X,expand = True )

    indonesia = Button(EEurope5,width = 7, height = 3, text = "Indonesia ({0})".format(countries[38][2]),font = textFont, wraplength = 80,bg = countryColours[0][38],fg = countryColours[1][38], command = Indonesia )

    newGuinea = Button(EEurope5,width = 5, height = 3, text = "New Guinea ({0})".format(countries[39][2]),font = textFont, wraplength = 60,bg = countryColours[0][39],fg = countryColours[1][39] , command = NewGuinea)
    
    
    EEurope6 = Frame(EEurope, bg = sea, height = 40)
    EEurope6.pack(fill = X, expand = True)
    
    EEurope7 = Frame(EEurope, bg = sea)
    EEurope7.pack()

    EEurope71 = Frame(EEurope7 , bg = sea, width = 5)
    EEurope71.pack(side = LEFT)

    westernAus = Button(EEurope7,width = 6, height = 3, text = "Western Australia ({0})".format(countries[40][2]),font = textFont, wraplength = 80,bg = countryColours[0][40],fg = countryColours[1][40] , command = WesternAustralia)
    
    easternAus  = Button(EEurope7,width = 7, height = 3, text = "Easten Australia ({0})".format(countries[41][2]),font = textFont, wraplength = 80,bg = countryColours[0][41],fg = countryColours[1][41], command = EasternAustralia)
    fillerLabel = Label(NCEurope3, text = "---------", font = textFont, height = 2, bg = sea)


    japan = Button(board,width = 2, height = 3,bg = countryColours[0][32],fg = countryColours[1][32] , command = Japan)
    japanLabel = Label(board,text = "Japan ({0})".format(countries[32][2]), font = textFont, bg = sea,fg = countryColours[1][32])
    
    alaska.pack(side = LEFT)
    greenLand.pack(side = RIGHT)
    NWTerritory.pack(side = LEFT)
    alberta.pack(side = LEFT,anchor = N)
    orlando.pack(side = LEFT)
    qubec.pack(side = LEFT)
    WUS.pack(side = LEFT)
    EUS.pack(side = LEFT)
    CAmerica.pack(side = LEFT)
    venezuela.pack(side=LEFT)
    peru.pack(side=LEFT)
    brazil.pack(side=LEFT)
    argentina.pack(side = LEFT)
    iceland.pack(side = LEFT)
    gb.pack(side = LEFT)
    scandinavia.pack(side = RIGHT)
    northEurope.pack(side = LEFT)
    southEurope.pack(side = RIGHT)
    westEurope.pack(side = RIGHT)
    northAfrica.pack(side = LEFT)
    congo.pack(side = LEFT)
    egypt.pack(side = LEFT)
    eastAfrica.pack(side = LEFT)
    southAfrica.pack(side = LEFT)
    russia.pack(side = LEFT)
    afghanistan.pack(side = BOTTOM)
    ural.pack(side = BOTTOM)
    serbia.pack(side= TOP)
    middleEast.pack(side = LEFT, anchor = W)
    india.pack(anchor = N)
    madagascar.pack(anchor = W)
    madagascarLabel.pack(anchor = W)
    yakutsk.pack(side = TOP)
    irkutsk.pack(side = TOP)
    kamchatka.pack()
    mongolia.pack(side = LEFT,anchor = W)
    china.pack(anchor = W)
    siam.pack(anchor = W)
    indonesia.pack(side = LEFT)
    newGuinea.pack(side = RIGHT)
    westernAus.pack(side = LEFT)
    easternAus.pack(side = LEFT)
    japan.place(x = 1200, y = 130)
    japanLabel.place(x = 1185, y = 190)
    fillerLabel.pack(fill = Y, expand = True)




countries = [[0,0,1,[1,3,29]],
            [1,0,1,[0,2,3,4]],
            [2,0,1,[1,4,5,13]],
            [3,0,1,[0,1,4,6]],
            [4,0,2,[1,2,3,5,6,7]],
            [5,0,1,[2,4,7]],
            [6,0,1,[3,4,7,8]],
            [7,0,1,[4,5,6,8]],
            [8,0,1,[6,7,9]],
            [9,0,1,[8,10,11]],
            [10,0,1,[9,11,12]],
            [11,0,1,[9,10,12,20]],
            [12,0,1,[10,11]],
            [13,0,1,[2,14,16]],
            [14,0,1,[13,15,16,17]],
            [15,0,2,[14,17,19,26,30,34]],
            [16,0,1,[13,14,17,18]],
            [17,0,2,[14,15,16,18,19]],
            [18,0,2,[16,17,19,20]],
            [19,0,2,[15,17,18,20,21,34]],
            [20,0,1,[11,18,19,21,22,23]],
            [21,0,1,[19,20,23,34]],
            [22,0,2,[20,23,24]],
            [23,0,1,[20,21,22,24,25,34]],
            [24,0,1,[22,23,25]],
            [25,0,1,[23,24]],
            [26,0,2,[15,27,30,36]],
            [27,0,2,[26,28,30,31,33,36]],
            [28,0,2,[27,29,31]],
            [29,0,1,[0,28,31,32,33]],
            [30,0,2,[15,26,27,34,35,36]],
            [31,0,2,[27,28,29,33]],
            [32,0,1,[29,33]],
            [33,0,2,[27,29,31,32,36]],
            [34,0,1,[15,19,21,23,30,35]],
            [35,0,1,[30,34,36,37]],
            [36,0,1,[26,27,30,33,35,37]],
            [37,0,1,[35,36,38]],
            [38,0,1,[37,39,40]],
            [39,0,1,[38,40,41]],
            [40,0,1,[38,39,41]],
            [41,0,1,[39,40]]]

startMenu()
main.mainloop()

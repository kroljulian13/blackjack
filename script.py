import matplotlib.pyplot as plt
import numpy as np
import random
from strategy import matcher

#funkcja zliczania punktów (ogarnia kombinacje tylko do 2 asów)
# A = 11 lub 1  
# figura z A 21
# split not implemented

# to implement double bet when getting 11 (hit with only 1 card allowed)

cardsDef11 = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"D":10,"K":10,"A":11}
cardsDef1  = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"D":10,"K":10,"A":1}

def score(cards):
    counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0

    if "A" in cards: 
        aCount=0
        for card in cards:
            counter1 += cardsDef1[card]
            counter2 += cardsDef11[card]
            counter3 += cardsDef1[card]
            if card == "A": 
                aCount+=1
                if aCount == 2:
                    counter3 = counter3+10             

        result =  [counter1, counter2, counter3]

        result=list(set(result))  # removing double values
        return sorted(result)

    else:
        for card in cards:
            counter += cardsDef11[card]
        return [counter]

def bestScore(scores):
    #asuming that input values are sorted
    result = scores[0]
    for item in reversed(scores):
        if item <= 21:
            return item

    return result


def hiLo(init, krupier, user):
    rate = init
    for item in krupier:
        if cardsDef11[item] > 9:
            rate -=1
        if cardsDef11[item] < 7:
            rate +=1
    for item in user:
        if cardsDef11[item] > 9:
            rate -=1
        if cardsDef11[item] < 7:
            rate +=1
    
    return rate

def game(dobraneKarty, money, baseBet, idlePlay, maxBet, selectedStrategy, strategyCoeff): # az do rozdania wszystkich kart w tali
    talia=['2','2','2','2',
           '3','3','3','3',
           '4','4','4','4',
           '5','5','5','5',
           '6','6','6','6',
           '7','7','7','7',
           '8','8','8','8',
           '9','9','9','9',
           '10','10','10','10',
           'J','J','J','J',
           'D','D','D','D',
           'K','K','K','K',
           'A','A','A','A'
            ]
    report=[]
    gamesRegister=[]
    #extending to 4 decks
    talia.extend(talia)
    talia.extend(talia)
    
    rozdanie = 0
    zostaloKart = 0
    totalWin=0
    HL = 0 
    realHL =0
    
    while len(talia) > 10:
        rozdanie +=1
        zostaloKart = len(talia)

        #pojedyncze rozdanie
        krupier = []
        user = []
        result = 0

        #bet set according to strategy
        if selectedStrategy=="hiloActive":
            baseBetHL=baseBet+realHL*baseBet
        
        elif selectedStrategy=="betStrategyActive":
            baseBetHL=baseBet*matcher(gamesRegister, strategyCoeff)
            if baseBetHL==0:
                baseBetHL=baseBet

        else:
            baseBetHL=baseBet

        if baseBetHL<idlePlay:
            baseBetHL= idlePlay

        #pobranie karty przez krupiera
        krupier=random.sample(talia, 1)
        for item in krupier:
            talia.remove(item)

        #dobieranie kart przez usera
        user=random.sample(talia, 2)
        for item in user:
            talia.remove(item)

        hitLimit = 0
        # if bestScore(score(krupier)) < 7:
        #     hitLimit=5
        while bestScore(score(user)) < (17-dobraneKarty-hitLimit):
            newCard=random.sample(talia, 1)
            for item in newCard:
                talia.remove(item)
            user.extend(newCard)

        #dobieranie kart przez krupiera
        if bestScore(score(user)) <= 21:
            while bestScore(score(krupier)) < bestScore(score(user)):
                newCard=random.sample(talia, 1)
                for item in newCard:
                    talia.remove(item)
                krupier.extend(newCard)
            # czy remis
            if bestScore(score(krupier)) == bestScore(score(user)):
                result = 0

            elif bestScore(score(krupier)) > 21:
                result = 1
                totalWin+=1
                money += baseBetHL
            
            else:
                money -= baseBetHL    

        else:
            money -= baseBetHL

        if result==0:
            gamesRegister.append("L")
            resultBackground="lose"
        elif result==1:
            gamesRegister.append("W")
            resultBackground="win"
        
        if len(gamesRegister)>6:
            gamesRegister.pop(0)


        HL = hiLo(HL, krupier, user)
        realHL = HL/4

        print("\nUser: "+str(bestScore(score(user))), user)
        print("Krupier: "+str(bestScore(score(krupier))), krupier)
        # print("Talia: ",talia)
        print("Result: "+str(totalWin)+"/"+str(rozdanie))
        print("Zostało kart:", len(talia))
        print("real HI-LO: "+str(realHL))
        print("money: ",money)
        print("bet :",baseBetHL)
        print("game register :",gamesRegister)
        report.append({ 
            "no": str(rozdanie),
            "userScore": str(bestScore(score(user))), 
            "userCards": user,
            "krupierScore": str(bestScore(score(krupier))),
            "krupierCards": krupier,
            "totalWin": str(totalWin),
            "cardsLeft": str(len(talia)),
            "realHL": str(realHL),
            "balance":str(money),
            "bet": str(baseBetHL),
            "result": resultBackground
            })
    
    return report

# cykl 1..2..3 (kilkaset rozdań) - dobieram 0..1..2 kart gdy score < 17
    #----- losuj karte dla krupiera -> Input 1
    #----- losuj karty dla usera -> Input 2
    # dobieraj karty dla krupiera az > Input 2
    # zapisz wygrana/przegrana -> Output


    
# money = []
# balance = 1000
# for i in range(1):
#     baseBet = 10
#     # balance =  game(0, balance, baseBet)
#     money.append( game(0, 1000, baseBet))

# print(money)

# plt.hist(money, normed=True, bins=30)
# plt.ylabel('Probability')
# plt.show()
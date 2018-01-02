
# strategy generator

# default strategy
defaultStrategy = { 
    "L" : {
        "bet" : 1,
        "L" : {
            "bet" : 4,
            "L" : { 
                "bet" : 8,
                "W" : { 
                    "bet" : 4,
                    "W" : {
                        "bet": 1
                    },
                    "L" : {
                        "bet": 1
                    }
                },
                "L" : {  
                    "bet" : 8,
                    "W" : {
                        "bet": 1
                    },
                    "L" : {
                        "bet": 16
                    }
                }  
            },
            "W" : { 
                "bet" : 4,
                "W" : {
                    "bet" : 4,
                    "W" : {
                        "bet": 1
                    },
                    "L" : {
                        "bet": 1
                    }
                },
                "L" : {
                    "bet" : 4,
                    "W" : {
                        "bet": 1
                    },
                    "L" : {
                        "bet": 1
                    }
                }
            }
        }
    }
}

# new results should be added to the end of array older than 10 past results 
# should be removed
userGamesResults = ["W","L","L","W"]

# check for matching pattern, starting from last item of array digging down

def matcher(userGamesResults, strategy=defaultStrategy ):
    
    betMultiply=0 # starting bet

    for item in range(len(userGamesResults)):
        # level 1 check
        for item1 in strategy:
            if item1 == userGamesResults[item]:
                # print('level #1 passed => bet {}'.format(str(strategy[item1]['bet'])))
                betMultiply=strategy[item1]['bet']
                
                # level 2 check
                for item2 in strategy[item1]:
                    if item+1 < len(userGamesResults):
                        if item2 == userGamesResults[item + 1]:
                            # print('level #2 passed => bet {}'.format(str(strategy[item1][item2]['bet'])))
                            betMultiply=strategy[item1][item2]['bet']
                            if item+1==len(userGamesResults)-1:
                                return betMultiply

                            # level 3 check
                            for item3 in strategy[item1][item2]:
                                if item+2 < len(userGamesResults):
                                    if item3 == userGamesResults[item + 2]:
                                        # print('level #3 passed => bet {}'.format(str(strategy[item1][item2][item3]['bet'])))
                                        betMultiply=strategy[item1][item2][item3]['bet']
                                        if item+2==len(userGamesResults)-1:
                                            return betMultiply

                                        # level 4 check
                                        for item4 in strategy[item1][item2][item3]:
                                            if item+3 < len(userGamesResults):
                                                if item4 == userGamesResults[item + 3]:
                                                    # print('level #4 passed => bet {}'.format(str(strategy[item1][item2][item3][item4]['bet'])))
                                                    betMultiply=strategy[item1][item2][item3][item4]['bet']
                                                    if item+3==len(userGamesResults)-1:
                                                        return betMultiply      

                                                    # level 5 check
                                                    for item5 in strategy[item1][item2][item3][item4]:
                                                        if item+4 < len(userGamesResults):
                                                            if item5 == userGamesResults[item + 4]:
                                                                # print('level #5 passed => bet {}'.format(str(strategy[item1][item2][item3][item4][item5]['bet'])))
                                                                betMultiply=strategy[item1][item2][item3][item4][item5]['bet']
                                                                if item+4==len(userGamesResults)-1:
                                                                    return betMultiply    

                                                            else:
                                                                betMultiply=0

                                                else:
                                                    betMultiply=0
                                    else:
                                        betMultiply=0 
                        else:
                            betMultiply=0



    return betMultiply


# matcher(userGamesResults, strategy )
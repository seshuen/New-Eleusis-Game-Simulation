"""
CMSC 671 Artificial Intelligence
The Game of New Eleusis - Phase 2
Team: Anonymous Agents
Seshagopalan Narasimhan XP27536
Rashmi Prava Patro AK14498
Rashmi Kunchakuri GV78738
"""
"""
1) http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=3
2) https://stackoverflow.com/questions/6521892/how-to-access-a-dictionary-key-value-present-inside-a-list
3) https://alexlouden.com/posts/2015-defaultdict-in-python.html
4) https://www.tutorialspoint.com/python/python_dictionary.htm
5) https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches


"""
from new_eleusis import *
from boardState import *
from God import God
from standAlone import *
from attribute import *
from trainingData import *
import collections
import random
from random import randint
from math import *

god = God()
board = boardState()
# create Instance of attribute class
a = attribute()
# Generate Rule Map
ruleMap = getMap()
keyRule = ruleMap.keys()
""" =============================== Initialize all the variables ========================================="""
cardDeck = []
cardsPlayed = 0
firstPlay = False
godRule = ""
playerRule = ""
attributeMap = {}
gotRule = False
myrulelist = []
__boardState = []
safePlay = 0
cardSet = []

""" =============================== Functions ========================================="""
# def setRule(rule):
#     """
#     # To set the rule to gods rule
#     """
#     return god.setRule(rule)

def generate_random_card():
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "H", "D", "C"]
    return values[randint(0, len(values)-1)] + suits[randint(0, len(suits)-1)]

def setCardsPlayed(num):
    global cardsPlayed
    cardsPlayed = num

def getCardsPlayed():
    global cardsPlayed
    return cardsPlayed

def chooseCard(hand):
    return random.choice(hand)


def testRule(godRule, playerRule):
    global gotRule
    playerTestCards = []
    godTestCards = []
    cards = []

    try:
        god.setRule(playerRule)
    except Exception as inst:
        pass
    # Generate Cards
    for i in range(0,10):
        cards.append(generateCard())

    # Check Players Rule
    for i in range(0,len(cards) - 1):
        cardtuple = cards[i:i+3]
        # print ("Cardtuple ")
        # print (cardtuple)
        if(len(cardtuple) == 3):
            __checkP = god.__validate__(cardtuple)
            if( str(__checkP) == "True"):
                playerTestCards.append("Legal")
            else:
                playerTestCards.append("Illegal")
    # Set Rule back to gods
    god.setRule(godRule)
    for i in range(0,len(cards) - 1):
        cardtuple = cards[i:i+3]
        if(len(cardtuple) == 3):
            __checkG = god.__validate__(cardtuple)
            if( str(__checkG) == "True"):
                godTestCards.append("Legal")
            else:
                godTestCards.append("Illegal")
    # Check if all cards are same
    testCard = zip(godTestCards, playerTestCards)

    for values in testCard:
        if(values[0] != values[1]):
            gotRule =  False
            break
        else:
            gotRule =  True


def getRuleList(tree):
    global myrulelist
    # l = []
    # finallist = []
    if type(tree) == str:
        l = list()
        l.append(tree)
        myrulelist.append(l)
        return [l]
    else:
        nodename = list(tree.keys())[0]
        childdict = tree[nodename]
        finallist = []
        for vvalue in childdict:
            childnode = childdict[vvalue]
            lst = getRuleList(childnode)
            for indilist in lst:
                indilist.append(vvalue)
                indilist.append(nodename)
                finallist.append(indilist)
    return finallist

def newRule(expList):
    # Returns in the concatenated version of rough rules created during the tree traversing
    finalRule = ""
    for index in range(0, len(expList)):
        temp = "or(" + expList[index] +", False)"
        if index == 0:
            finalRule = temp
        else:
            finalRule = "or(" + finalRule + "," + temp + ")"
    return finalRule

def isattribute(attribute):
    global keyRule
    if attribute in keyRule:
        return True
    else:
        return False

def concatenate(lst):
    result = []
    for hyp in lst:
        hyp = hyp[::-1]
        classification = hyp[-1]
        if classification == 'Legal':
            expression = ""
            for i in range(0, len(hyp) - 1, 2):
                node = str(ruleMap.get(hyp[i]))
                value = str(hyp[i+1])
                if(i == 0):
                    expression =  "and(equal(" + node + "," + value + ") , True)"
                else:
                    temp = "and(equal(" + node + "," + value + ") , True)"
                    expression = "and(" + expression + "," + temp + ")"
            result.append(expression)
    return result

def updateHand(hand, result):
    del hand[hand.index(result)]
    hand.append(generate_random_card())

def scientist(hand,game_ended):
    global cardDeck, firstPlay, safePlay, cards ,correctCard, cardsPlayed, cardSet, attributeMap, storeExpression, gotRule, score, keyRule, playerRule, __boardState
    global godRule
    godRule = god.rule()
    if len( board.__str__()) == 3:
        result = chooseCard(hand)
        updateHand(hand, result)
        return result
    if(len( board.__str__()) > 3):
        # Have board state of lastly played 20 cards
        __boardState = board.__str__()
        attributeTable = {}

        # Creat an attribute table for given board state
        attributeTable = generateTrainingData(__boardState)
        # print("Table: ", len(attributeTable))

        # Populate all the attributes for given attribute table
        tables =  a.getAttributes(attributeTable)

        for attr in tables:
            attributeMap[attr] = a.getUniqueValues(attributeTable, attr)
        # print("*", len(attributeMap))

        dtree = a.decisionTree(attributeTable, a.getAttributes(attributeTable), 'classification')

        hypothesis = getRuleList(dtree)
        # print("hypothesis : " , hypothesis)
        exp = concatenate(hypothesis)
        playerRule = newRule(exp)
        # Didnt handle this previously. Now i have handled.
        # Check if the playerRule is present
        if(len(playerRule) > 0):
            testRule(godRule, playerRule)
            # Was the test successfull
            if gotRule == True:
                game_ended = True
                gotRule = True
                result = playerRule
                return result
            else:
                # Check if we have any hypothesis present
                if len(hypothesis) > 1:
                    game_ended = True
                    # gotRule = True

                    result = playerRule
                    return result
                else:
                    # Check if game has ended
                    if game_ended == True:
                        gotRule = True

                        result = True
                        return True
                    else:
                        result = chooseCard(hand)
                        updateHand(hand, result)
                        return result

        else:
            result = chooseCard(hand)
            updateHand(hand, result)
            return result


def score(player):
    global __score, score1575, score30
    __score = 0

    k = board.__str__()[-20:]
    j = [l.values() for l in k]

    #increments score by +1 or +2
    for val in j:
        if "Legal" in val:
            __score = __score + 1
        elif "Illegal" in val:
            __score = __score + 2

    #increments score by +15
    score1575 = plus15(player)
    if (score1575 == False):
        __score = __score + 15
    # else:
    #     __score = __score - 75

    #increments score by +30
    score30 = plus30()
    if (score30 == False):
        __score = __score + 30

    #bonus decrements by -75 or -25
    if (score1575 == True):
        __score = __score - 75

    if (gotRule == True):
        __score = __score - 25

    print ("Score : " + str(__score))
    # return __score

#Updated for score +30
def plus30():
    global correctValue, playerRule

    validateScientist = []
    validateGod = []
    playerValuesList = []
    godValuesList = []
    godVal = []
    checkvalues = []
    #godVal=Values of all cards in boardState
    #godValuesList= list of values in BS without first 2 cards

    key1 = [list(m.keys()) for m in __boardState]
    compareKeys = [val for sublist in key1 for val in sublist]

    value1 = [list(l.values()) for l in __boardState]
    godVal = [val for sublist in value1 for val in sublist]

    godValuesList = godVal[2:]

    god.setRule(playerRule)
    for i in range(2,len(compareKeys)):
        cardtuple = compareKeys[i-2:i+1]

        if(len(cardtuple) == 3):
            __checkP = god.__validate__(cardtuple)
            if( str(__checkP) == "True"):
                playerValuesList.append("Legal")
            else:
                playerValuesList.append("Illegal")

    checkvalues = [i for i,j in zip(godValuesList, playerValuesList) if i == j]

    if(len(checkvalues) == len(godValuesList)):
        return True
    else:
        return False


#updated for score +15
def plus15(player):
    global correctRule, playerRule, godRule
    __fscore = 0
    __cardScientist = []
    __cardGod = []
    validateScientist = []
    validateGod = []
    deckofCards = []
    godRes = False
    playerRes = False
    # Score for +15 with confidence
    cardTotal = 0.0
    numEquivalent = 0.0
    percentageEqui = 0.0
    output = []
    print ("Anonymous Agents' Player Rule : " + str(player.play()))
    if gotRule == True or player.play() == True:
        percentageEqui = 100.0
    else:
        for i in range(0,52):
            deckofCards.append(generate_random_card())
        for x in deckofCards:
            if x not in output:
                output.append(x)
        cardTotal = math.pow(len(output),3)
        print (".....Loading logical equivalence.....")
        for c1 in output:
            for c2 in output:
                for c3 in output:
                    # print (c1 + c2 + c3)
                    listtuple = [c1,c2,c3]
                    # print (listtuple)
                    god.setRule(godRule)
                    godRes = god.__validate__(listtuple)
                    if godRes == False:
                        godRes = False
                    else:
                        godRes = True
                    god.setRule(playerRule)
                    # god.setRule(str(player.play()))
                    playerRes = god.__validate__((c1,c2,c3))
                    if playerRes == False:
                        playerRes = False
                    else:
                        playerRes = True
                    if godRes == playerRes:
                        numEquivalent += 1
                    # if gotRule == True:
                    #     percentageEqui = 100
                    # else:
                    # print (str(numEquivalent) + '.....' + str(cardTotal))
                    percentageEqui = float(numEquivalent/cardTotal)*100

    print ("Confidence in Players rule is " + str(percentageEqui)[0:7] +'%')

    if percentageEqui == 100 or percentageEqui == 100.0:
        return True
    else:
        return False



# ******************************************** GAME.PY *********************************
# rule = "if(is_royal(current), False)"
# cards = ["10H", "2C", "4S"]
# tree = parse(rule)
# god.setRule(rule)
# godRule = god.rule()
# for card in cards:
#     board.legal(card)
#     cardSet.append(card)
#
# h = [generate_random_card() for i in range(14)]
#
# for i in range(14):
#     print(scientist(h, False))

# ******************************************** END OF GAME.PY *********************************


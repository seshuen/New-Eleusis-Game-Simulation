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
import new_eleusis as func

def generateTrainingData(boardState):
    attributeTable = []
    keysinBS = []
    valuesinBS = []
    for item in boardState:
        keysinBS.extend(list(item.keys()))
        valuesinBS.extend(list(item.values()))
    i = 2
    dict = {}
    for i in range(2,len(keysinBS)):
        # 'card':keysinBS[i],
        dict = {'suitCur':func.suit(keysinBS[i]),
                'suitLsDCur':func.less(func.suit(keysinBS[i]),func.suit('D')),
                'suitLsHCur':func.less(func.suit(keysinBS[i]),func.suit('H')),
                'suitLsSCur':func.less(func.suit(keysinBS[i]),func.suit('S')),
                'suitGrCCur':func.greater(func.suit(keysinBS[i]),func.suit('C')),
                'suitGrDCur':func.greater(func.suit(keysinBS[i]),func.suit('D')),
                'suitGrHCur':func.greater(func.suit(keysinBS[i]),func.suit('H')),
                'colorCur':func.color(keysinBS[i]),'royalCur':func.is_royal(keysinBS[i]),
                'valueEvenCur':func.even(keysinBS[i]),
                'valueEq1Cur':func.equal(func.value(keysinBS[i]),'1'),
                'valueEq2Cur':func.equal(func.value(keysinBS[i]),'2'),
                'valueEq3Cur':func.equal(func.value(keysinBS[i]),'3'),
                'valueEq4Cur':func.equal(func.value(keysinBS[i]),'4'),
                'valueEq5Cur':func.equal(func.value(keysinBS[i]),'5'),
                'valueEq6Cur':func.equal(func.value(keysinBS[i]),'6'),
                'valueEq7Cur':func.equal(func.value(keysinBS[i]),'7'),
                'valueEq8Cur':func.equal(func.value(keysinBS[i]),'8'),
                'valueEq9Cur':func.equal(func.value(keysinBS[i]),'9'),
                'valueEq10Cur':func.equal(func.value(keysinBS[i]),'10'),
                'valueEq11Cur':func.equal(func.value(keysinBS[i]),'11'),
                'valueEq12Cur':func.equal(func.value(keysinBS[i]),'12'),
                'valueEq13Cur':func.equal(func.value(keysinBS[i]),'13'),
                'valueGr1Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'A'),
                'valueGr2Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'2'),
                'valueGr3Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'3'),
                'valueGr4Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'4'),
                'valueGr5Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'5'),
                'valueGr6Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'6'),
                'valueGr7Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'7'),
                'valueGr8Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'8'),
                'valueGr9Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'9'),
                'valueGr10Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'10'),
                'valueGr11Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'J'),
                'valueGr12Cur':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),'Q'),
                'valueLs2Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'2'),
                'valueLs3Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'3'),
                'valueLs4Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'4'),
                'valueLs5Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'5'),
                'valueLs6Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'6'),
                'valueLs7Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'7'),
                'valueLs8Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'8'),
                'valueLs9Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'9'),
                'valueLs10Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'10'),
                'valueLs11Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'J'),
                'valueLs12Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'Q'),
                'valueLs13Cur':func.less(str(func.number_to_value(func.value(keysinBS[i]))),'K'),
                'suitPrev':func.suit(keysinBS[i-1]),
                'suitLsDPrev':func.less(func.suit(keysinBS[i-1]),func.suit('D')),
                'suitLsHPrev':func.less(func.suit(keysinBS[i-1]),func.suit('H')),
                'suitLsSPrev':func.less(func.suit(keysinBS[i-1]),func.suit('S')),
                'suitGrCPrev':func.greater(func.suit(keysinBS[i-1]),func.suit('C')),
                'suitGrDPrev':func.greater(func.suit(keysinBS[i-1]),func.suit('D')),
                'suitGrHPrev':func.greater(func.suit(keysinBS[i-1]),func.suit('H')),
                'colorPrev':func.color(keysinBS[i-1]),'royalPrev':func.is_royal(keysinBS[i-1]),
                'valueEvenPrev':func.even(keysinBS[i-1]),
                'valueEq1Prev':func.equal(func.value(keysinBS[i-1]),'1'),
                'valueEq2Prev':func.equal(func.value(keysinBS[i-1]),'2'),
                'valueEq3Prev':func.equal(func.value(keysinBS[i-1]),'3'),
                'valueEq4Prev':func.equal(func.value(keysinBS[i-1]),'4'),
                'valueEq5Prev':func.equal(func.value(keysinBS[i-1]),'5'),
                'valueEq6Prev':func.equal(func.value(keysinBS[i-1]),'6'),
                'valueEq7Prev':func.equal(func.value(keysinBS[i-1]),'7'),
                'valueEq8Prev':func.equal(func.value(keysinBS[i-1]),'8'),
                'valueEq9Prev':func.equal(func.value(keysinBS[i-1]),'9'),
                'valueEq10Prev':func.equal(func.value(keysinBS[i-1]),'10'),
                'valueEq11Prev':func.equal(func.value(keysinBS[i-1]),'11'),
                'valueEq12Prev':func.equal(func.value(keysinBS[i-1]),'12'),
                'valueEq13Prev':func.equal(func.value(keysinBS[i-1]),'13'),
                'valueGr1Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'A'),
                'valueGr2Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'2'),
                'valueGr3Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'3'),
                'valueGr4Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'4'),
                'valueGr5Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'5'),
                'valueGr6Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'6'),
                'valueGr7Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'7'),
                'valueGr8Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'8'),
                'valueGr9Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'9'),
                'valueGr10Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'10'),
                'valueGr11Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'J'),
                'valueGr12Prev':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),'Q'),
                'valueLs2Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'2'),
                'valueLs3Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'3'),
                'valueLs4Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'4'),
                'valueLs5Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'5'),
                'valueLs6Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'6'),
                'valueLs7Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'7'),
                'valueLs8Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'8'),
                'valueLs9Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'9'),
                'valueLs10Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'10'),
                'valueLs11Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'J'),
                'valueLs12Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'Q'),
                'valueLs13Prev':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),'K'),
                'suitPrev2':func.suit(keysinBS[i-2]),
                'suitLsDPrev2':func.less(func.suit(keysinBS[i-2]),func.suit('D')),
                'suitLsHPrev2':func.less(func.suit(keysinBS[i-2]),func.suit('H')),
                'suitLsSPrev2':func.less(func.suit(keysinBS[i-2]),func.suit('S')),
                'suitGrCPrev2':func.greater(func.suit(keysinBS[i-2]),func.suit('C')),
                'suitGrDPrev2':func.greater(func.suit(keysinBS[i-2]),func.suit('D')),
                'suitGrHPrev2':func.greater(func.suit(keysinBS[i-2]),func.suit('H')),
                'colorPrev2':func.color(keysinBS[i-2]),'royalPrev2':func.is_royal(keysinBS[i-2]),
                'valueEvenPrev2':func.even(keysinBS[i-2]),
                'valueEq1Prev2':func.equal(func.value(keysinBS[i-2]),'1'),
                'valueEq2Prev2':func.equal(func.value(keysinBS[i-2]),'2'),
                'valueEq3Prev2':func.equal(func.value(keysinBS[i-2]),'3'),
                'valueEq4Prev2':func.equal(func.value(keysinBS[i-2]),'4'),
                'valueEq5Prev2':func.equal(func.value(keysinBS[i-2]),'5'),
                'valueEq6Prev2':func.equal(func.value(keysinBS[i-2]),'6'),
                'valueEq7Prev2':func.equal(func.value(keysinBS[i-2]),'7'),
                'valueEq8Prev2':func.equal(func.value(keysinBS[i-2]),'8'),
                'valueEq9Prev2':func.equal(func.value(keysinBS[i-2]),'9'),
                'valueEq10Prev2':func.equal(func.value(keysinBS[i-2]),'10'),
                'valueEq11Prev2':func.equal(func.value(keysinBS[i-2]),'11'),
                'valueEq12Prev2':func.equal(func.value(keysinBS[i-2]),'12'),
                'valueEq13Prev2':func.equal(func.value(keysinBS[i-2]),'13'),
                'valueGr1Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'A'),
                'valueGr2Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'2'),
                'valueGr3Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'3'),
                'valueGr4Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'4'),
                'valueGr5Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'5'),
                'valueGr6Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'6'),
                'valueGr7Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'7'),
                'valueGr8Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'8'),
                'valueGr9Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'9'),
                'valueGr10Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'10'),
                'valueGr11Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'J'),
                'valueGr12Prev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),'Q'),
                'valueLs2Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'2'),
                'valueLs3Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'3'),
                'valueLs4Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'4'),
                'valueLs5Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'5'),
                'valueLs6Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'6'),
                'valueLs7Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'7'),
                'valueLs8Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'8'),
                'valueLs9Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'9'),
                'valueLs10Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'10'),
                'valueLs11Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'J'),
                'valueLs12Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'Q'),
                'valueLs13Prev2':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),'K'),
                'suitCurLsPrev':func.less(func.suit(keysinBS[i]),func.suit(keysinBS[i-1])),
                'suitCurGrPrev':func.greater(func.suit(keysinBS[i]),func.suit(keysinBS[i-1])),
                'suitCurEqPrev':func.equal(func.suit(keysinBS[i]),func.suit(keysinBS[i-1])),
                'valueCurLsPrev':func.less(str(func.number_to_value(func.value(keysinBS[i]))),str(func.number_to_value(func.value(keysinBS[i-1])))),
                'valueCurGrPrev':func.greater(str(func.number_to_value(func.value(keysinBS[i]))),str(func.number_to_value(func.value(keysinBS[i-1])))),
                'valueCurEqPrev':func.equal(str(func.number_to_value(func.value(keysinBS[i]))),str(func.number_to_value(func.value(keysinBS[i-1])))),
                'colorCurLsPrev':func.less(func.color(keysinBS[i]),func.color(keysinBS[i-1])),
                'colorCurGrPrev':func.greater(func.color(keysinBS[i]),func.color(keysinBS[i-1])),
                'colorCurEqPrev':func.equal(func.color(keysinBS[i]),func.color(keysinBS[i-1])),
                'suitPrevLsPrev2':func.less(func.suit(keysinBS[i-1]),func.suit(keysinBS[i-2])),
                'suitPrevGrPrev2':func.greater(func.suit(keysinBS[i-1]),func.suit(keysinBS[i-2])),
                'suitPrevEqPrev2':func.equal(func.suit(keysinBS[i-1]),func.suit(keysinBS[i-2])),
                'valuePrevLsPrev2':func.less(str(func.number_to_value(func.value(keysinBS[i-1]))),str(func.number_to_value(func.value(keysinBS[i-2])))),
                'valuePrevGrPrev2':func.greater(str(func.number_to_value(func.value(keysinBS[i-1]))),str(func.number_to_value(func.value(keysinBS[i-2])))),
                'valuePrevEqPrev2':func.equal(str(func.number_to_value(func.value(keysinBS[i-1]))),str(func.number_to_value(func.value(keysinBS[i-2])))),
                'colorPrevLsPrev2':func.less(func.color(keysinBS[i-1]),func.color(keysinBS[i-2])),
                'colorPrevGrPrev2':func.greater(func.color(keysinBS[i-1]),func.color(keysinBS[i-2])),
                'colorPrevEqPrev2':func.equal(func.color(keysinBS[i-1]),func.color(keysinBS[i-2])),
                'suitPrev2LsCur':func.less(func.suit(keysinBS[i-2]),func.suit(keysinBS[i])),
                'suitPrev2GrCur':func.greater(func.suit(keysinBS[i-2]),func.suit(keysinBS[i])),
                'suitPrev2EqCur':func.equal(func.suit(keysinBS[i-2]),func.suit(keysinBS[i])),
                'valuePrev2LsCur':func.less(str(func.number_to_value(func.value(keysinBS[i-2]))),str(func.number_to_value(func.value(keysinBS[i])))),
                'valuePrev2GrCur':func.greater(str(func.number_to_value(func.value(keysinBS[i-2]))),str(func.number_to_value(func.value(keysinBS[i])))),
                'valuePrev2EqCur':func.equal(str(func.number_to_value(func.value(keysinBS[i-2]))),str(func.number_to_value(func.value(keysinBS[i])))),
                'colorPrev2LsCur':func.less(func.color(keysinBS[i-2]),func.color(keysinBS[i])),
                'colorPrev2GrCur':func.greater(func.color(keysinBS[i-2]),func.color(keysinBS[i])),
                'colorPrev2EqCur':func.equal(func.color(keysinBS[i-2]),func.color(keysinBS[i])),
                'classification':valuesinBS[i]}
        attributeTable.append(dict)
    return attributeTable

#
def getMap():
    ruleMap = {
        'suitCur':'suit(current)',
    	'suitLsDCur':'less(suit(current),suit(D))',
    	'suitLsHCur':'less(suit(current),suit(H))',
    	'suitLsSCur':'less(suit(current),suit(S))',
    	'suitGrCCur':'greater(suit(current),suit(C))',
    	'suitGrDCur':'greater(suit(current),suit(D))',
    	'suitGrHCur':'greater(suit(current),suit(H))',
    	'colorCur':'color(current)',
    	'royalCur':'is_royal(current)',
    	'valueEvenCur':'even(current)',
    	'valueEq1Cur':'equal(value(current),1)',
    	'valueEq2Cur':'equal(value(current),2)',
    	'valueEq3Cur':'equal(value(current),3)',
    	'valueEq4Cur':'equal(value(current),4)',
    	'valueEq5Cur':'equal(value(current),5)',
    	'valueEq6Cur':'equal(value(current),6)',
    	'valueEq7Cur':'equal(value(current),7)',
    	'valueEq8Cur':'equal(value(current),8)',
    	'valueEq9Cur':'equal(value(current),9)',
    	'valueEq10Cur':'equal(value(current),10)',
    	'valueEq11Cur':'equal(value(current),11)',
    	'valueEq12Cur':'equal(value(current),12)',
    	'valueEq13Cur':'equal(value(current),13)',
    	'valueGr1Cur':'greater(value(current),A)',
    	'valueGr2Cur':'greater(value(current),2)',
    	'valueGr3Cur':'greater(value(current),3)',
    	'valueGr4Cur':'greater(value(current),4)',
    	'valueGr5Cur':'greater(value(current),5)',
    	'valueGr6Cur':'greater(value(current),6)',
    	'valueGr7Cur':'greater(value(current),7)',
    	'valueGr8Cur':'greater(value(current),8)',
    	'valueGr9Cur':'greater(value(current),9)',
    	'valueGr10Cur':'greater(value(current),10)',
    	'valueGr11Cur':'greater(value(current),J)',
    	'valueGr12Cur':'greater(value(current),Q)',
    	'valueLs2Cur':'less(value(current),2)',
    	'valueLs3Cur':'less(value(current),3)',
    	'valueLs4Cur':'less(value(current),4)',
    	'valueLs5Cur':'less(value(current),5)',
    	'valueLs6Cur':'less(value(current),6)',
    	'valueLs7Cur':'less(value(current),7)',
    	'valueLs8Cur':'less(value(current),8)',
    	'valueLs9Cur':'less(value(current),9)',
    	'valueLs10Cur':'less(value(current),10)',
    	'valueLs11Cur':'less(value(current),J)',
    	'valueLs12Cur':'less(value(current),Q)',
    	'valueLs13Cur':'less(value(current),K)',
    	'suitPrev':'suit(previous)',
    	'suitLsDPrev':'less(suit(previous),suit(D))',
    	'suitLsHPrev':'less(suit(previous),suit(H))',
    	'suitLsSPrev':'less(suit(previous),suit(S))',
    	'suitGrCPrev':'greater(suit(previous),suit(C))',
    	'suitGrDPrev':'greater(suit(previous),suit(D))',
    	'suitGrHPrev':'greater(suit(previous),suit(H))',
    	'colorPrev':'color(previous)',
    	'royalPrev':'is_royal(previous)',
    	'valueEvenPrev':'even(previous)',
    	'valueEq1Prev':'equal(value(previous),1)',
    	'valueEq2Prev':'equal(value(previous),2)',
    	'valueEq3Prev':'equal(value(previous),3)',
    	'valueEq4Prev':'equal(value(previous),4)',
    	'valueEq5Prev':'equal(value(previous),5)',
    	'valueEq6Prev':'equal(value(previous),6)',
    	'valueEq7Prev':'equal(value(previous),7)',
    	'valueEq8Prev':'equal(value(previous),8)',
    	'valueEq9Prev':'equal(value(previous),9)',
    	'valueEq10Prev':'equal(value(previous),10)',
    	'valueEq11Prev':'equal(value(previous),11)',
    	'valueEq12Prev':'equal(value(previous),12)',
    	'valueEq13Prev':'equal(value(previous),13)',
    	'valueGr1Prev':'greater(value(previous),A)',
    	'valueGr2Prev':'greater(value(previous),2)',
    	'valueGr3Prev':'greater(value(previous),3)',
    	'valueGr4Prev':'greater(value(previous),4)',
    	'valueGr5Prev':'greater(value(previous),5)',
    	'valueGr6Prev':'greater(value(previous),6)',
    	'valueGr7Prev':'greater(value(previous),7)',
    	'valueGr8Prev':'greater(value(previous),8)',
    	'valueGr9Prev':'greater(value(previous),9)',
    	'valueGr10Prev':'greater(value(previous),10)',
    	'valueGr11Prev':'greater(value(previous),J)',
    	'valueGr12Prev':'greater(value(previous),Q)',
    	'valueLs2Prev':'less(value(previous),2)',
    	'valueLs3Prev':'less(value(previous),3)',
    	'valueLs4Prev':'less(value(previous),4)',
    	'valueLs5Prev':'less(value(previous),5)',
    	'valueLs6Prev':'less(value(previous),6)',
    	'valueLs7Prev':'less(value(previous),7)',
    	'valueLs8Prev':'less(value(previous),8)',
    	'valueLs9Prev':'less(value(previous),9)',
    	'valueLs10Prev':'less(value(previous),10)',
    	'valueLs11Prev':'less(value(previous),J)',
    	'valueLs12Prev':'less(value(previous),Q)',
    	'valueLs13Prev':'less(value(previous),K)',
    	'suitPrev2':'suit(previous2)',
    	'suitLsDPrev2':'less(suit(previous2),suit(D))',
    	'suitLsHPrev2':'less(suit(previous2),suit(H))',
    	'suitLsSPrev2':'less(suit(previous2),suit(S))',
    	'suitGrCPrev2':'greater(suit(previous2),suit(C))',
    	'suitGrDPrev2':'greater(suit(previous2),suit(D))',
    	'suitGrHPrev2':'greater(suit(previous2),suit(H))',
    	'colorPrev2':'color(previous2)',
    	'royalPrev2':'is_royal(previous2)',
    	'valueEvenPrev2':'even(previous2)',
    	'valueEq1Prev2':'equal(value(previous2),1)',
    	'valueEq2Prev2':'equal(value(previous2),2)',
    	'valueEq3Prev2':'equal(value(previous2),3)',
    	'valueEq4Prev2':'equal(value(previous2),4)',
    	'valueEq5Prev2':'equal(value(previous2),5)',
    	'valueEq6Prev2':'equal(value(previous2),6)',
    	'valueEq7Prev2':'equal(value(previous2),7)',
    	'valueEq8Prev2':'equal(value(previous2),8)',
    	'valueEq9Prev2':'equal(value(previous2),9)',
    	'valueEq10Prev2':'equal(value(previous2),10)',
    	'valueEq11Prev2':'equal(value(previous2),11)',
    	'valueEq12Prev2':'equal(value(previous2),12)',
    	'valueEq13Prev2':'equal(value(previous2),13)',
    	'valueGr1Prev2':'greater(value(previous2),A)',
    	'valueGr2Prev2':'greater(value(previous2),2)',
    	'valueGr3Prev2':'greater(value(previous2),3)',
    	'valueGr4Prev2':'greater(value(previous2),4)',
    	'valueGr5Prev2':'greater(value(previous2),5)',
    	'valueGr6Prev2':'greater(value(previous2),6)',
    	'valueGr7Prev2':'greater(value(previous2),7)',
    	'valueGr8Prev2':'greater(value(previous2),8)',
    	'valueGr9Prev2':'greater(value(previous2),9)',
    	'valueGr10Prev2':'greater(value(previous2),10)',
    	'valueGr11Prev2':'greater(value(previous2),J)',
    	'valueGr12Prev2':'greater(value(previous2),Q)',
    	'valueLs2Prev2':'less(value(previous2),2)',
    	'valueLs3Prev2':'less(value(previous2),3)',
    	'valueLs4Prev2':'less(value(previous2),4)',
    	'valueLs5Prev2':'less(value(previous2),5)',
    	'valueLs6Prev2':'less(value(previous2),6)',
    	'valueLs7Prev2':'less(value(previous2),7)',
    	'valueLs8Prev2':'less(value(previous2),8)',
    	'valueLs9Prev2':'less(value(previous2),9)',
    	'valueLs10Prev2':'less(value(previous2),10)',
    	'valueLs11Prev2':'less(value(previous2),J)',
    	'valueLs12Prev2':'less(value(previous2),Q)',
    	'valueLs13Prev2':'less(value(previous2),K)',
    	'suitCurLsPrev':'less(suit(current),suit(previous))',
    	'suitCurGrPrev':'greater(suit(current),suit(previous))',
    	'suitCurEqPrev':'equal(suit(current),suit(previous))',
    	'valueCurLsPrev':'less(value(current),value(previous))',
    	'valueCurGrPrev':'greater(value(current),value(previous))',
    	'valueCurEqPrev':'equal(value(current),value(previous))',
    	'colorCurLsPrev':'less(color(current),color(previous))',
    	'colorCurGrPrev':'greater(color(current),color(previous))',
    	'colorCurEqPrev':'equal(color(current),color(previous))',
    	'suitPrevLsPrev2':'less(suit(previous),suit(previous2))',
    	'suitPrevGrPrev2':'greater(suit(previous),suit(previous2))',
    	'suitPrevEqPrev2':'equal(suit(previous),suit(previous2))',
    	'valuePrevLsPrev2':'less(value(previous),value(previous2))',
    	'valuePrevGrPrev2':'greater(value(previous),value(previous2))',
    	'valuePrevEqPrev2':'equal(value(previous),value(previous2))',
    	'colorPrevLsPrev2':'less(color(previous),color(previous2))',
    	'colorPrevGrPrev2':'greater(color(previous),color(previous2))',
    	'colorPrevEqPrev2':'equal(color(previous),color(previous2))',
    	'suitPrev2LsCur':'less(suit(previous2),suit(current))',
    	'suitPrev2GrCur':'greater(suit(previous2),suit(current))',
    	'suitPrev2EqCur':'equal(suit(previous2),suit(current))',
    	'valuePrev2LsCur':'less(value(previous2),value(current))',
    	'valuePrev2GrCur':'greater(value(previous2),value(current))',
    	'valuePrev2EqCur':'equal(value(previous2),value(current))',
    	'colorPrev2LsCur':'less(color(previous2),color(current))',
    	'colorPrev2GrCur':'greater(color(previous2),color(current))',
    	'colorPrev2EqCur':'equal(color(previous2),color(current))'}
    return ruleMap

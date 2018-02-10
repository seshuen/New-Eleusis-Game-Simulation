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

from collections import defaultdict as default
import new_eleusis as func
import math

# boardState = [{'8D': 'Legal'}, {'10S': 'Legal'}, {'10C': 'Legal'}, {'3C': 'Legal'}, {'7S': 'Legal'}, {'7D': 'Illegal'}, {'2D': 'Illegal'}, {'4D': 'Illegal'}, {'2D': 'Illegal'}, {'10H': 'Illegal'}, {'JC': 'Legal'}, {'9C': 'Legal'}, {'3S': 'Legal'}, {'KC': 'Legal'}, {'2H': 'Illegal'}, {'QH': 'Illegal'}, {'7C': 'Legal'}, {'3S': 'Legal'}, {'6C': 'Legal'}, {'3C': 'Legal'}, {'4S': 'Legal'}, {'AC': 'Legal'}]

class attribute:
    attributeTable = []
    attributeMap = {}

    def getAttributes(self, table):
        totalAttributes = []
        for tuple in table:
            totalAttributes.extend(tuple.keys())
        self.attributesCount = set(totalAttributes)
        return self.attributesCount

    def getUniqueValues(self, table, attr):
        totalValues = []
        for tuple in table:
            totalValues.append(tuple[attr])
        return set(totalValues)

    def getAttributeValue(self, attributeTable, attribute):
        highestCount = 0
        attr = None
        record = [tuple[attribute] for tuple in attributeTable]
        for value in set(record):
            if record.count(value) > highestCount:
                attr =  value
                highestCount = record.count(value)
        return attr

    def generateTable(self, attribute, value ,attributeTable):
        table = []
        for tuple in attributeTable:
            if tuple[attribute] == value:
                table.append(tuple)
        return table

    def entropy(self, attributeTable, attribute = None, value = None ):
        table = attributeTable
        if attribute != None:
            table = self.generateTable(attribute, value ,attributeTable)

        counter = [tuple['classification'] for tuple in table]

        p = float(counter.count('Legal'))
        n = float(counter.count('Illegal'))
        total = float(p + n)
        if total == 0 :
            return 0
        setp = p / total
        setn =  n / total
        logp = math.log(setp, 2) if setp != 0 else 0
        logn = math.log(setn, 2) if setn != 0 else 0
        entropy = -(setp * logp) - (setn * logn)
        return entropy

    def remainder(self, attr, attributeTable):
        entropy = []
        values = self.getUniqueValues(attributeTable, attr)
        for val in values:
            table = self.generateTable(attr, val ,attributeTable)
            classifier = [tuple['classification'] for tuple in table]
            __uniquevalue = float(len(classifier))
            pk = float(float(len(classifier)) / float(len(attributeTable)))
            _entp = self.entropy(table, attr, val)
            entropy.append(pk * _entp)
        return sum(entropy)

    def splitRatio(self, attr, attributeTable):
        table = attributeTable
        valList = []
        pList = []
        spList = []
        logpList = []
        #finalList = []
        splitratio = 0
        #counter = [tuple['classification'] for tuple in table]
        valList = self.getUniqueValues(attributeTable ,attr)
        counter = [tuple[attr] for tuple in table]
        for val in valList:
            p = float(counter.count(val))
            pList.append(p)
        total = float(len(attributeTable))
        if total == 0:
            return 0
        for i in pList:
            setp = float(i / total)
            spList.append(setp)
        for j in spList:
            logp = math.log(j, 2) if setp != 0 else 0
            logpList.append(logp)

        for k in list(zip(spList,logpList)):
            splitratio += k[0] * k[1]

        return (-float(splitratio))


    def __gain(self, entropy, remainder):
        gain = entropy - remainder
        return gain

    def gainRatio(self, entropy, remainder, splitratio):
        gain = entropy - remainder
        _ratio = gain / splitratio if splitratio != 0  else 0
        return _ratio

    def getNode(self, attributeTable, attributeList, splitAttribute):
        attributeTable = attributeTable
        fitnessValue = 0.0
        atttributeNode = None

        for attr in attributeList:
            __fitnessValue = self.gainRatio(self.entropy(attributeTable), self.remainder(attr, attributeTable), self.splitRatio(attr, attributeTable))
            if (__fitnessValue >= fitnessValue and attr != splitAttribute):
                fitnessValue = __fitnessValue
                atttributeNode = attr

        return atttributeNode

    def __getNode(self, attributeTable, attributeList, splitAttribute):
        attributeTable = attributeTable
        fitnessValue = 0.0
        atttributeNode = None

        for attr in attributeList:
            __fitnessValue = self.__gain(self.entropy(attributeTable), self.remainder(attr, attributeTable))
            if (__fitnessValue >= fitnessValue and attr != splitAttribute):
                fitnessValue = __fitnessValue
                atttributeNode = attr

        return atttributeNode
#decision tree based on gain ratio
    def decisionTree(self, attributeTable, attribute, splitAttribute):
        table = attributeTable
        defaultValue = self.getAttributeValue(table, splitAttribute)
        valueSet = [attributeSet[splitAttribute] for attributeSet in table]
        if len(table) - 1 <= 0 or len(attribute) - 1 <= 0:
            return defaultValue
        elif valueSet.count(valueSet[0]) == len(valueSet):
            return valueSet[0]
        else:
            node = self.getNode(table, attribute, splitAttribute)
            decTree = {node: default(lambda: defaultValue)}

            for value in self.getUniqueValues(table, node):
                nTable = self.generateTable(node, value, table)
                nAttr = [attr for attr in attribute if attr != node]
                subNode = self.decisionTree(nTable, nAttr, splitAttribute)
                decTree[node][value] = subNode
        return decTree
#decision tree based on information gain
    def decisionTree2(self, attributeTable, attribute, splitAttribute):
        table = attributeTable
        defaultValue = self.getAttributeValue(table, splitAttribute)
        valueSet = [attributeSet[splitAttribute] for attributeSet in table]
        if len(table) - 1 <= 0 or len(attribute) - 1 <= 0:
            return defaultValue
        elif valueSet.count(valueSet[0]) == len(valueSet):
            return valueSet[0]
        else:
            node = self.__getNode(table, attribute, splitAttribute)
            decTree = {node: default(lambda: defaultValue)}

            for value in self.getUniqueValues(table, node):
                nTable = self.generateTable(node, value, table)
                nAttr = [attr for attr in attribute if attr != node]
                subNode = self.decisionTree(nTable, nAttr, splitAttribute)
                decTree[node][value] = subNode
        return decTree

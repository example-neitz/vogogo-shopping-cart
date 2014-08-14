
""" Module that contains the main elements used to checkout items
    at the Supermarket """

from decimal import *
import copy

def createInventoryList(pricingRules):
    """ Creates the pricing list to use by the Scanner """
    inventoryList = {}
    for name, rules in pricingRules.iteritems():
        inventoryList[name] = Item(name,rules)
    return inventoryList

class Item:
    """ Represents an Item for sale in the supermarket
        tracks the number of items and can calculate the
        final price based on the rules passed in """
    def __init__(self,name,rules):
        self.name = name
        self.multiPriceRules = []
        self.rules = rules
        self.singlePrice = Decimal(rules[1])

        for num, price in rules.items():
            self.multiPriceRules.append(num)
            
        self.multiPriceRules.sort(reverse=True)

        self.numberOfItems = 0

    def finalCost(self):
        numItemsLeft = self.numberOfItems
        rules = copy.deepcopy(self.multiPriceRules)
        if rules:
            multiRuleTotal = Decimal('0')
            
            while rules:
                rule = rules.pop(0)
                
                if numItemsLeft / rule > 0 :
                    leftOverItems = numItemsLeft % rule
                    multiRuleTotal += Decimal((numItemsLeft - leftOverItems) / rule) * Decimal(self.rules[rule])
                    numItemsLeft = leftOverItems;

            return multiRuleTotal + Decimal(numItemsLeft) * self.singlePrice
        return Decimal('0')


class Scanner:
    """ Supermarket scanner scans individual items
        keeping track of all items and can calculate
        and print the bill """
    def __init__(self, itemList):
        self.itemList = itemList
    
    def scanItem(self,item):
        if isinstance(item,basestring) and item in self.itemList:
            self.itemList[item].numberOfItems += 1

    def scanItems(self,itemList):
        for item in itemList:
            self.scanItem(item)

    def totalPrice(self):
        total = Decimal('0')
        for name,item in self.itemList.items():
            total += item.finalCost();
        return total

            
    def printItemizedBill(self):
        print "Vogogo Grocery"
        print "-----------------"
        total = Decimal('0')
        for name,item in self.itemList.items():
            if item.numberOfItems > 0:
                print str(item.numberOfItems).ljust(3) + name.ljust(10) + " at $" + str(item.finalCost()).ljust(4)
            total += item.finalCost()
        print "-----------------"
        print "Balance Due: ".ljust(17) + "$" + str(total)    


        

#!/usr/bin/python

""" This is the main file for SuperMarket Checkout System
    It takes two arguments:
    A dictionary containing the supermarket item and sub dictionary containing price by x (key) for price y (value)
    A list containing the list of items to be checked out
"""

# Still Todo
# Readme.txt describing how to use the program
# Load up to github

import unittest
from decimal import *
import sys, getopt
import ast
import copy

from ShoppingCart import *
import Checkout_unittests

suite = unittest.TestLoader().loadTestsFromModule(Checkout_unittests)
alltests = unittest.TestSuite([suite])

def areRulesValid(rules):
    """ Makes sure we have at least one item and that every item
        has at least a price for one item defined """

    if not isinstance(rules,dict) and not dict:
        return False

    for name, ruleList in rules.items():
        if not name:
            return False

        if not isinstance(ruleList,dict):
            return False

        if not ruleList and 1 not in ruleList:
            return False

        for number, price in ruleList.items():
            if not isinstance(number,int):
                return False

            if not isinstance(price,basestring):
                return False
    
    return True

def printHelp():
    print 'Checkout.py -r <pricingRules> -g <groceryList>'
    
    print """\nexample: Checkout.py \n
\t--rules="{'Apple' : { 1 : '0.30', 3 : '0.80' },'Tomato' : { 1 : '0.70' } }"
\n\t--groceryList="['Apple','Tomato','Tomato']" """
     
def main_test():
    runner=unittest.TextTestRunner()
    runner.run(alltests)

def main(argv):
   rules = {}
   groceryList = []
   try:
      opts, args = getopt.getopt(argv,"htr:g:",["rules=","groceryList=","test"])
   except getopt.GetoptError:
      printHelp()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printHelp()
         sys.exit()
      elif opt in ("-r", "--rules"):
          try:
              rules = ast.literal_eval(arg)
          except:
              printHelp()
              sys.exit()
      elif opt in ("-g", "--groceryList"):
          try:
              groceryList = ast.literal_eval(arg)
          except:
              printHelp()
              sys.exit()
      elif opt in ("-t", "--test"):
         main_test()
         sys.exit()
 

   if not isinstance(groceryList,list):
       printHelp()
       sys.exit()

   if not areRulesValid(rules):
       printHelp()
       sys.exit()

   #print 'Rules ', rules
   #print 'GroceryList ', groceryList

   itemList = createInventoryList(rules)
   scanner = Scanner(itemList)
   scanner.scanItems(groceryList)
   scanner.printItemizedBill()
   

if __name__ == "__main__":
   main(sys.argv[1:])

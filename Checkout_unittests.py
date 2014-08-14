
""" Unit test for the Supermarket checkout exercise """

import unittest
from decimal import *
from ShoppingCart import *

# Unit tests -----

class ScannerTests(unittest.TestCase):
    def setUp(self):

        pricingRulesWithSingleDiscount = { 'Apple': { 1 : '0.50' ,  3 : '1.30' },
                         'Orange': {1 : '0.20'},
                         'Tomato': {1 : '1.25'},
                         'Cucumber': {1 : '0.10'} 
                         }

        pricingRulesWithMultipleDiscounts = { 'Apple': { 1 : '0.50' ,  3 : '1.30' , 5 : '2.00' },
                                              'Orange': {1 : '0.20' , 4 : '.60'},
                                              'Tomato': {1 : '1.25' , 2 : '.62', 5 : '2.50', 10 : '2.00'},
                                              'Cucumber': {1 : '0.10'} 
                                              }

        self.singleItemListOneDiscount = createInventoryList(pricingRulesWithSingleDiscount)
        self.multipleDiscountsItemList = createInventoryList(pricingRulesWithMultipleDiscounts)

    def testScaningItems(self):
        scanner = Scanner(self.singleItemListOneDiscount)
        groceryList = ['Apple','Orange','Tomato', 'Apple', 'Orange','Cucumber']
        scanner.scanItems(groceryList)
        
        self.failIf(self.singleItemListOneDiscount['Apple'].numberOfItems != 2)
        self.failIf(self.singleItemListOneDiscount['Orange'].numberOfItems != 2)
        self.failIf(self.singleItemListOneDiscount['Tomato'].numberOfItems != 1)
        self.failIf(self.singleItemListOneDiscount['Cucumber'].numberOfItems != 1)

    def testPricingZeroItems(self):
        scanner = Scanner(self.singleItemListOneDiscount)

        emptyGroceryList = []
        scanner.scanItems(emptyGroceryList)
        self.assertEqual(Decimal("0"),scanner.totalPrice())
            

    def testPricingSingleItems(self):
        scanner = Scanner(self.singleItemListOneDiscount)

        groceryList = ['Apple','Orange','Tomato', 'Apple', 'Orange','Cucumber']
        scanner.scanItems(groceryList)
        self.assertTrue(self.singleItemListOneDiscount['Apple'].finalCost() == Decimal('1.00'))
        self.assertTrue(self.singleItemListOneDiscount['Orange'].finalCost() == Decimal('0.40'))
        self.assertTrue(self.singleItemListOneDiscount['Tomato'].finalCost() == Decimal('1.25'))
        self.assertTrue(self.singleItemListOneDiscount['Cucumber'].finalCost() == Decimal('0.10'))
        self.assertEqual(Decimal("2.75"),scanner.totalPrice())

    def testPricingSingleItemsWithExactDiscount(self):
        scanner = Scanner(self.singleItemListOneDiscount)

        groceryList = ['Apple','Orange','Orange', 'Apple', 'Orange','Apple']
        scanner.scanItems(groceryList)

        self.assertTrue(self.singleItemListOneDiscount['Apple'].finalCost() == Decimal('1.30'))
        self.assertTrue(self.singleItemListOneDiscount['Orange'].finalCost() == Decimal('0.60'))
        self.assertEqual(Decimal("1.90"),scanner.totalPrice())

    def testPricingMultipleItemsBeyondDiscounts(self):
        scanner = Scanner(self.singleItemListOneDiscount)
        groceryList = ['Apple','Tomato','Cucumber','Apple','Cucumber','Apple','Apple']
        scanner.scanItems(groceryList)
        self.assertTrue(self.singleItemListOneDiscount['Apple'].finalCost() == Decimal('1.80'))
        self.assertTrue(self.singleItemListOneDiscount['Tomato'].finalCost() == Decimal('1.25'))
        self.assertTrue(self.singleItemListOneDiscount['Cucumber'].finalCost() == Decimal('0.20'))
        self.assertEqual(Decimal("3.25"),scanner.totalPrice())

    def testPricingMultipleItemsWithMultipleDiscounts(self):
        scanner = Scanner(self.multipleDiscountsItemList)
        groceryList = ['Orange','Apple','Tomato','Orange','Tomato','Cucumber','Tomato','Tomato','Tomato',
                       'Apple','Cucumber','Apple','Tomato','Tomato','Apple','Tomato','Orange','Apple',
                       'Orange','Apple','Apple','Orange','Apple','Apple']
        scanner.scanItems(groceryList)
        self.assertTrue(self.multipleDiscountsItemList['Apple'].finalCost() == Decimal('3.80'))
        self.assertTrue(self.multipleDiscountsItemList['Tomato'].finalCost() == Decimal('4.37'))
        self.assertTrue(self.multipleDiscountsItemList['Orange'].finalCost() == Decimal('0.80'))
        self.assertTrue(self.multipleDiscountsItemList['Cucumber'].finalCost() == Decimal('0.20'))
        self.assertEqual(Decimal("9.17"),scanner.totalPrice())

    def testPricingMultipleItemsWithMultipleDiscountsOneExact(self):
        scanner = Scanner(self.multipleDiscountsItemList)
        groceryList = ['Orange','Apple','Tomato','Orange','Tomato','Cucumber','Tomato','Tomato','Tomato',
                       'Apple','Cucumber','Apple','Tomato','Tomato','Apple','Tomato','Orange','Apple',
                       'Orange','Apple','Apple','Orange','Apple','Apple','Tomato','Tomato']
        scanner.scanItems(groceryList)
        self.assertTrue(self.multipleDiscountsItemList['Apple'].finalCost() == Decimal('3.80'))
        self.assertTrue(self.multipleDiscountsItemList['Tomato'].finalCost() == Decimal('2.00'))
        self.assertTrue(self.multipleDiscountsItemList['Orange'].finalCost() == Decimal('0.80'))
        self.assertTrue(self.multipleDiscountsItemList['Cucumber'].finalCost() == Decimal('0.20'))
        self.assertEqual(Decimal("6.80"),scanner.totalPrice())


class CheckoutTests(unittest.TestCase):

    def setUp(self):
        pricingRulesWithSingleDiscount = { 'Apple': { 1 : '0.50' ,  3 : '1.30' },
                         'Orange': {1 : '0.20'},
                         'Tomato': {1 : '1.25'},
                         'Cucumber': {1 : '0.10'} 
                         }

        self.itemList = createInventoryList(pricingRulesWithSingleDiscount)
 
    def testCheckout(self):
        scanner = Scanner(self.itemList)
        groceryList = ['Apple','Orange','Tomato', 'Apple', 'Orange','Cucumber']
        scanner.scanItems(groceryList)
        
        self.failIf(self.itemList['Apple'].numberOfItems != 2)
        self.failIf(self.itemList['Orange'].numberOfItems != 2)
        self.failIf(self.itemList['Tomato'].numberOfItems != 1)
        self.failIf(self.itemList['Cucumber'].numberOfItems != 1)


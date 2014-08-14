vogogo-shopping-cart
====================

Vogogo shopping cart exercise

This is the Vogogo shopping cart exercise written in python 2

The main file is called Checkout.py and is run via the command line

It takes the following options

./Checkout.py 

    -r --rules - this specifies the items and pricing rules that are
                 in the inventory of the supermarket
                 
    -g --groceryList - this specifies the list of items in your list
                       that you wish to checkout
                       
    -t --test        - this runs the associated unit tests
                       
                       
  An example usage of the program would be the following
  
  ./Checkout.py --rules="{ 'Apple' : { 1 : '0.30', 3 : '1.00' }, 'Tomato' : { 1:'1.00'}}" --groceryList="['Tomato','Apple']"
  
  Notice the rules are simply just a python dictionary, specified inside a string, with keys describing the item in this
  case an Apple and a Tomato, the sub dictionary (value) describes the pricing rule per number
  of that kind of item. So in this example you can get a single Apple for $0.30 and 3 Apples for a dollar and
  1 Tomato for a dollar.
  
  *Some cavets* when specifying rules you must specify the price for buying 1 of that particular item
  You can however specifiy as many pricing rules as you like. Checkout will look for the price that matches the
  greatest number of items and work down until all items have been accounted for
          
  groceryList is just a python list specified inside a string it should be a list of items that you specified in your rules
  


  Running the following example should result in the following output

```  
Vogogo Grocery
-----------------
1  Tomato     at $1.00
1  Apple      at $0.30
-----------------
Balance Due:     $1.30
```

  An example showing the pricing of multiple rules
  
   ./Checkout.py --rules="{ 'Apple' : { 1 : '0.30', 2: '0.30', 3 : '1.00' }, 'Tomato' : { 1:'1.00'}}" --groceryList="['Tomato','Apple','Tomato','Apple','Apple','Apple','Apple','Apple','Apple']"
   
   Would output the following

```  
Vogogo Grocery
-----------------
2  Tomato     at $2.00
7  Apple      at $2.30
-----------------
Balance Due:     $4.30
```   

The Apples come out to $2.30 because we match the highest number of items to price rule first. In this example that would be 3 for a dollar. This applies to 6 of the 7 Apples. Then we only have one item left which is $0.30.



# Probability of Flipping Coins
[**Flipping Coins.py**](Flipping%20Coins.py) is a collection of functions that deal with **coin flipping**, or **coin tossing**, which is the practice of throwing a coin in the air and checking which side is showing when it lands. An ideal unbiased coin has a **0.5** chance for showing a head and the remaining other **0.5** chance for showing a tail with **each coin flip**. In contrast, biased coins tend to favor one side over the other. A biased coin, for example, might have a **0.8** probability of landing on its head, or its tail. 

# Installation  
    Simply, copy the codes and paste them to your workplace. 

# Documentation 
#### Right now, **Flipping Coins.py** contains the following four functions:

## allPossibilities(N)
#### This function takes a single parameter **N** and returns all the possible patterns that might result from throwing coins **N** times.

####  Example 1: writing all the possible patterns in tossing one coins
     In: allPossibilities(1)
     Out: ['H', 'T']
     
####  Example 2: writing all the possible patterns in tossing three coins
     In: allPossibilities(3)
     Out: ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
 
 
## probabilityXcoinsYheads(x,y,headChance=0.5)
#### This function takes two main parameters **x** and **y** and returns the probability of getting **y** heads on throwing **x** coins. 

####   Example 1: calculating the probability of one head showing after flipping 2 fair coins 
     In: probabilityXcoinsYheads(2,1,headChance=0.5)[3]
     Out: 0.5 

##### Explanation: ['HT,'TH'] out of ['HH','HT','TH','TT] so 2 out 4 which is 0.5
####   Example 2: calculating the probability of one head showing after flipping 2 unfair coins with the head chance of 1
     In: probabilityXcoinsYheads(2,1,headChance=1)[3]
     Out: 0
##### Explanation: there is a 0 chance of getting 'HT' or 'TH' because the chance of getting a head is 1
   
   
## probability(sequence,coinPickChance,headChance)
#####   Example: calcuating the chance of getting 'HH' on flibbing a coin twice from a set of 2 coins each with a differet picking chance and head chance
      In: probability("HH",[0.75,0.25],[0.5,1])
      Out: 0.4375
##### Explanation: the chance of picking the first coin is 0.75 with 0.25 chance of getting 'HH'. For the second coin, the picking chance is 0.25 with 1 chance of getting 'HH' (result = 0.75x0.25 + 0.25x1 = 0.4375)


## simulatingFlippingCoins(success=[1], size=1, coins=[1,0], probability=[0.5,0.5], tests=1000000)
##### Example 1: simulating 1 million tests of two fair coin flips and obtaining the proportion of tests that produced 2 heads
      In: simulatingFlippingCoins([2],2)
      Out: 0.250262
      Comparison probabilityXcoinsYheads(2,2)[3]
      Output of Comparsion (real probability): 0.25
##### Example 2: simulating 1 million tests of five fair coin flips and obtaining the proportion of tests that produced 1 head 
      In: simulatingFlippingCoins([1],5)
      Out: 0.156261
      Comparison: probability("HTTTT",[1],[0.5])*5
      Output of Comparsion (real probability): 0.15625
##### Example 3: simulating 1 million tests of ten biased coin flips and obtaining the proportion of tests that produced 5 heads 
      In: simulatingFlippingCoins(success=[5],size=5,probability=[0.8,0.2])
      Out: 0.32793
      Comparison: probabilityXcoinsYheads(5,5,0.8)[3]
      Output of Comparison (real probability): 0.32768
##### Example 4: simulating 1 million tests of ten biased coin flips and obtaining the proportion of tests that produced at least 3 heads 
      In: simulatingFlippingCoins(success=list(range(3,11)),size=10,probability=[0.15,0.85])
      Out: 0.179899
      Comparison: sum([probabilityXcoinsYheads(10,x,0.15)[3] for x in range(3,11)])
      Output of Comparison (real probability): 0.17980351963242186

# Dependencies
* [NumPy](https://www.numpy.org/)

# Contributing
The project is open for contribution.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

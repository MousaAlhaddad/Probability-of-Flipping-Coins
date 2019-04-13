# Probability-of-Flipping-Coins

The script contains four functions: 
1. allPossibilities(coins)
   - Example: 
     - allPossibilities(3)
     - Aim: writing all the possible patterns in tossing 3 coins 
     - Output: ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
 
 
2. probabilityXcoinsYheads(x,y,headChance=0.5)
   - Example1: 
     - probabilityXcoinsYheads(2,1,headChance=0.5)[3]
     - Aim: calculating the probability of one head showing after flipping 2 fair coins 
     - Output: 0.5 
     - Explanation: ['HT','TH'] out of ['HH','HT','TH','TT]
   - Example2:
     - probabilityXcoinsYheads(2,1,headChance=1)[3]
     - Aim: calculating the probability of one head showing after flipping 2 unfair coins with the head chance of 1
     - Output: 0
     - Explanation: there is a 0 chance of getting 'HT' or 'TH' because the head chance is 1
   
   
3. probability(sequence,coinPickChance,headChance)
   - Example: 
      - probability("HH",[0.75,0.25],[0.5,1])
      - Aim: calcuating the chance of getting 'HH' on flibbing a coin twice from a set of 2 coins each with a differet picking chance and head chance
      - Output: 0.4375
      - Explanation: the chance of picking the first coin is 0.75 with 0.25 chance of getting 'HH'. For the second coin, the picking chance is 0.25 with 1 chance of getting 'HH' (result = 0.75x0.25 + 0.25x1 = 0.4375)


4. simulatingFlippingCoins(success=[1], size=1, coins=[1,0], probability=[0.5,0.5], tests=1000000):
   - Example1: 
      - simulatingFlippingCoins([2],2)
      - Aim: simulating 1 million tests of two fair coin flips and obtaining the proportion of tests that produced 2 heads
      - Output: 0.250262
      - Comparison: probabilityXcoinsYheads(2,2)[3]
      - Output of Comparsion (real probability): 0.25
   - Example2: 
      - simulatingFlippingCoins([1],5)
      - Aim: simulating 1 million tests of five fair coin flips and obtaining the proportion of tests that produced 1 head
      - Output: 0.156261
      - Comparison: probability("HTTTT",[1],[0.5])*5 
      - Output of Comparsion (real probability): 0.15625
   - Example3:
      - simulatingFlippingCoins(success=[5],size=5,probability=[0.8,0.2])
      - Aim: simulating 1 million tests of ten biased coin flips and obtaining the proportion of tests that produced 5 heads
      - Output: 0.32793
      - Comparison:probabilityXcoinsYheads(5,5,0.8)[3]
      - Output of Comparison (real probability): 0.32768
   - Example4: 
      - simulatingFlippingCoins(success=list(range(3,11)),size=10,probability=[0.15,0.85])
      - Aim: simulating 1 million tests of ten biased coin flips and obtaining the proportion of tests that produced at least 3 heads
      - Output: 0.179899
      - Comparison: sum([probabilityXcoinsYheads(10,x,0.15)[3] for x in range(3,11)])
      - Output of Comparison (real probability): 0.17980351963242186


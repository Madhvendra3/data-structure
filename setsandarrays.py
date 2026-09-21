basket1 = {"apple","banana","grape","mango"}
basket2 = {"mango","cherry","apple","peach"}
print("basket1: ",basket1)
print("basket2: ",basket2)

basket1.add("watermelon")
print("basket 1 after addding watermelon: ",basket1)

common = basket1.intersection(basket2)
print("Fruits in both baskets are ",common)

import array as arr
fruitcount = arr.array('i',[1,2,3,4,5])
print("fruit counts array: ",fruitcount)

fruitcount.insert(1,2)
fruitcount.append(10)
print("fruit counts after adding items: ",fruitcount)

count2 = fruitcount.count(2)
print("number of times 2 appears is ",count2)

fruitcount.reverse()
print("reversed array fruit count: ",fruitcount)
 #final class fruit basket organiser summary
 #basket1,basket2,common,fruitcount.
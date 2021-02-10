"""
10 min
Implement the IceCreamMachine's scoops method so that it returns all
combinations of one ingredient and one topping. If there are no ingredients or
toppings, the method should return an empty list.
For example,
IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
should return
[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
    class IceCreamMachine:
        def __init__(self, ingredients, toppings):
            self.ingredients = ingredients
            self.toppings = toppings
        def scoops(self):
            pass
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
"""


```
# code without library
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        arr = []
        for i in range(len(self.ingredients)):
            for j in range(len(self.toppings)):
                arr.append([self.ingredients[i],self.toppings[j]])
        return arr

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
```

from itertools import product


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        return list(product(self.ingredients, self.toppings))


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

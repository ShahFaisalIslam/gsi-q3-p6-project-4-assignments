# Pop up shop
# Obtain total cost of fruits given the prices of each fruit as well as amount
# of each fruit to be bought

class Shop:
    def __init__(self):
        # Initiate prices
        self.prices :dict = {}
        self.prices["apple"] = 3.5
        self.prices["durian"] = 2.0
        self.prices["jackfruit"] = 1.0
        self.prices["kiwi"] = 2.5
        self.prices["rambutan"] = 12.0
        self.prices["mango"] = 0.98

        # Initiate count
        self.count :dict = {}
        self.count["apple"] = 0
        self.count["durian"] = 0
        self.count["jackfruit"] = 0
        self.count["kiwi"] = 0
        self.count["rambutan"] = 0
        self.count["mango"] = 0

    def get_total_cost(self) -> float:
        total : float = 0

        # Accumulate total for each fruit
        for fruit in self.count.keys():
            total += self.prices[fruit] * self.count[fruit]

        return total

def main():
    shop : Shop = Shop()

    # Prompt the user for amounts
    for fruit in shop.count.keys():
        shop.count[fruit] = float(input(f"How many ({fruit}) do you want? "))
    
    # Calculate the total
    total_cost : float = shop.get_total_cost()

    # Display the total
    print(f"Your total is ${round(total_cost,2)}")

if __name__ == '__main__':
    main()
class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550

    def total_supplies(self):
        print(f'''The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.coffee_beans} g of coffee beans
        {self.disposable_cups} of disposable cups
        ${self.money} of money''')

    def __init__(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit) : ')
            if action == 'buy':
                coffee_type = input('What do you want to buy? (1 - espresso, 2 - latte, 3 - cappuccino, back) : ')
                if coffee_type == '1':
                    if self.water < 250:
                        print('Sorry, not enough water!')
                    elif self.coffee_beans < 16:
                        print('Sorry, not enough coffee beans!')
                    elif self.disposable_cups < 1:
                        print('Sorry, not enough disposable cups!')
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.coffee_beans -= 16
                        self.disposable_cups -= 1
                        self.money += 4
                elif coffee_type == '2':
                    if self.water < 350:
                        print('Sorry, not enough water!')
                    elif self.milk < 75:
                        print('Sorry, not enough milk!')
                    elif self.coffee_beans < 20:
                        print('Sorry, not enough coffee beans!')
                    elif self.disposable_cups < 1:
                        print('Sorry, not enough disposable cups!')
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350
                        self.milk -= 75
                        self.coffee_beans -= 20
                        self.disposable_cups -= 1
                        self.money += 7
                elif coffee_type == '3':
                    if self.water < 200:
                        print('Sorry, not enough water!')
                    elif self.milk < 100:
                        print('Sorry, not enough milk!')
                    elif self.coffee_beans < 12:
                        print('Sorry, not enough coffee beans!')
                    elif self.disposable_cups < 1:
                        print('Sorry, not enough disposable cups!')
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200
                        self.milk -= 100
                        self.coffee_beans -= 12
                        self.disposable_cups -= 1
                        self.money += 6
                elif coffee_type == 'back':
                    continue
            elif action == 'fill':
                fill_water = int(input('Write how many ml of water you want to add : '))
                fill_milk = int(input('Write how many ml of milk you want to add : '))
                fill_coffee_beans = int(input('Write how many grams of coffee beans you want to add : '))
                fill_disposable_cups = int(input('Write how many disposable coffee cups you want to add : '))
                self.water += fill_water
                self.milk += fill_milk
                self.coffee_beans += fill_coffee_beans
                self.disposable_cups += fill_disposable_cups
            elif action == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
            elif action == 'remaining':
                CoffeeMachine.total_supplies(self)
            elif action == 'exit':
                break


CoffeeMachine()
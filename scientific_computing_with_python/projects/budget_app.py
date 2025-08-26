class Category:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def __str__(self):
        num_stars = 30 - len(self.name)
        first_half_stars = num_stars // 2
        title_line = (first_half_stars) * '*' + self.name + (num_stars - first_half_stars) * '*' + '\n'
        item_list = ''
        total = 0
        for item in self.ledger:
            total += item['amount']
            description = item['description']
            amount = f"{item['amount']:.2f}"
            item_list += (des := description[:min(len(description), 23)])
            item_list += (((23 - len(des)) + (7 - len(amount))) * ' ') + amount + '\n'

        return title_line + item_list + f"Total: {total:.2f}"
    
    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount


def create_spend_chart(categories):
    expenditures = [
        round (
            sum([transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0]), 2
        )
        for category in categories
    ]
    total_spent = round(sum(expenditures), 2)
    bar_max_list = [int(expenditure / total_spent * 100) // 10 for expenditure in expenditures]
    chart = 'Percentage spent by category\n'

    for i in range(100, 0, -10):
        if i == 100:
            chart += f'100| '
        else:
            chart += f' {i}| '
        
        for bar_max in bar_max_list:
            chart += 'o  ' if bar_max*10 >= i else 3 * ' '
        chart += '\n'

    x_length = 5 + len(categories) + 2 * len(categories)
    chart += '  0| ' + len(categories) * 'o  ' + '\n' + 4 * ' ' + (x_length - 4) * '-'  + '\n'

    max_length = max([len(category.name) for category in categories])

    for i in range(max_length):
        chart += 5 * ' '
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  '
            else:
                chart += 3 * ' '
        chart += '\n' if i != max_length - 1 else ''

    return chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10.15)
clothing.withdraw(15.89)
import random


class Order:
    def __init__(self, product_name, deadline):
        self.product_name = product_name
        self.deadline = deadline
        self.product_id = random.randint(0, 100)


class QuickOrder(Order):
    def __init__(self, product_name, deadline, extra_dime):
        super().__init__(product_name, deadline)
        self.delivery_type = 'QuickOrder'

        if extra_dime < 40000:
            raise ValueError('Extra dime should be more than 40000')
        if deadline > 24:
            raise ValueError('Deadline should be less than 24 hrs')
        self.extra_dime = extra_dime

    # add function to change delivery time
    def change_time(self, new_deadline):
        self.deadline = new_deadline
        return self.deadline
        

class StandardOrder(Order):
    def __init__(self, product_name, deadline):
        super().__init__(product_name, deadline)
        self.delivery_type = 'StandardOrder'


delivered = []


def create_quick_order(product_name, deadline, extra_dime):
    quick_order = QuickOrder(product_name, deadline, extra_dime)
    delivered.append(quick_order)


def create_standard_order(product_name, deadline):
    standard_order = StandardOrder(product_name, deadline)
    delivered.append(standard_order)

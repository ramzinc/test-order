import unittest
from order import create_quick_order, delivered, QuickOrder, StandardOrder, create_standard_order


class TestOrder(unittest.TestCase):
#    def setUp(self):
 #       create_standard_order("Lungs",12)

    def test_create_quick_order(self):
        create_quick_order('Bag', 21, 50000)
        order = delivered[-1]
        self.assertIsInstance(order, QuickOrder)
        self.assertEqual(order.product_name, 'Bag')
        self.assertLess(order.deadline, 24)

    def test_create_quick_order_with_wrong_deadline(self):
        with self.assertRaises(ValueError):
            create_quick_order('Bag',45, 50000)
            order = delivered[-1]
            self.assertIsInstance(order, QuickOrder)

    def test_create_standard_order(self):
        create_standard_order("Lungs",21)
        order = delivered[-1]
        print(order.product_name)
        self.assertEqual(order.product_name, 'Lungs')

    def test_is_instance_of_standard_order(self):
        order = delivered[-1]
        self.assertIsInstance(order,StandardOrder)
    
    def test_create_quick_order_with_little_extra_dime(self):
        create_quick_order('Dog',10,40001)
        order = delivered[-1]
        self.assertEqual(order.extra_dime,40001)
    
    def test_create_quick_order_with_exceeded_deadline(self):
        with self.assertRaises(ValueError):
            create_quick_order('Dog',30,40001)
    
    def test_create_quick_order_with_amount_in_words(self):
        # wrong input
        pass

    def test_create_quick_order_with_deadline_in_words(self):
        # wrong input
        pass

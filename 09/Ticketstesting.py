'''Jesse Higgins
    CS5001
    Testing for Tickets Application
    3/9/2024
'''

from Tickets import tickets
from Tickets import tickets_seed

import unittest

class TestTicketsFunction(unittest.TestCase):

    def test_tickets_random(self):

        min_customers_served = 0
        max_customers_served = 101
        min_customers_queued = 0
        max_customers_queued = 101
        customers_served, customers_queued = tickets()

        self.assertIn(customers_served, range(min_customers_served, max_customers_served))
        self.assertIn(customers_queued, range(min_customers_queued, max_customers_queued))

    def test_tickets_seed_0(self):

        customers_served, customers_queued = tickets_seed(0)

        self.assertEqual(customers_served, 0)
        self.assertEqual(customers_queued, 0)


    def test_tickets_seed_1(self):

        customers_served, customers_queued = tickets_seed(1)

        self.assertEqual(customers_served, 100)
        self.assertEqual(customers_queued, 0)

    def test_tickets_seed_2(self):

        customers_served, customers_queued = tickets_seed(2)

        self.assertEqual(customers_served, 100)
        self.assertEqual(customers_queued, 100)

    def test_tickets_invalid(self):

        customers_served, customers_queued = tickets_seed(1000)

        self.assertEqual(customers_served, 0)
        self.assertEqual(customers_queued, 0)


def main():

    unittest.main()

if __name__ == "__main__":
    main()
#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        """Test stealability() and explode()
         methods function as they should."""
        prod = Product('Test Product')
        explode = Product.explode(prod)
        steal = Product.stealability(prod)
        self.assertEqual(explode, '...boom!')
        self.assertEqual(steal, 'Very stealable!')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Test length of product list being 30."""
        products_len = len(generate_products())
        self.assertEqual(products_len, 30)

#   def test_legal_names():


if __name__ == '__main__':
    unittest.main()

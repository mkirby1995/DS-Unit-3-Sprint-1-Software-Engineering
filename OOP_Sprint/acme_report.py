#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for _ in range(num_products):
        rand_name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]

        random_product = Product(name=rand_name,
                                 price=randint(5, 100),
                                 weight=randint(5, 100),
                                 flammability=uniform(0, 2.5))

        products.append((random_product.name, random_product.price,
                         random_product.weight, random_product.flammability,
                         random_product.identifier))

    return products


def inventory_report(products):

    names = []
    prices = []
    weights = []
    flammabilities = []

    for _ in range(len(products)):
        names.append(products[_][0])
        prices.append(products[_][1])
        weights.append(products[_][2])
        flammabilities.append(products[_][3])

    unique_product_names = len(set(names))
    average_price = sum(prices)/len(prices)
    average_weight = sum(weights)/len(weights)
    average_flammability = sum(flammabilities)/len(flammabilities)

    return print('ACME CORPORATION OFFICIAL INVENTORY REPORT', '\n',
                 'Unique product names:', unique_product_names, '\n',
                 'Average price:', average_price, '\n',
                 'Average weight:', average_weight, '\n',
                 'Average flammability:', average_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())

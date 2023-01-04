#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'priceCheck' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_LIST products
#  2. FLOAT_LIST productPrices
#  3. STRING_LIST productSold
#  4. FLOAT_LIST soldPrice
#

def priceCheck(products, productPrices, productSold, soldPrice):
    l = 10 ** 5
    n = len(products)
    m = len(productSold)
    w = 0
    d = {}
    if n >= 1 and n <= l and m >= 1 and m <= l:
        for i in range (n):
            d[products[i]] = productPrices[i]
        for j in range(m):
            if productSold[j] in d:
                if soldPrice[j] != d[productSold[j]]:
                    w += 1
        return w
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    products_count = int(input().strip())

    products = []

    for _ in range(products_count):
        products_item = input()
        products.append(products_item)

    productPrices_count = int(input().strip())

    productPrices = []

    for _ in range(productPrices_count):
        productPrices_item = float(input().strip())
        productPrices.append(productPrices_item)

    productSold_count = int(input().strip())

    productSold = []

    for _ in range(productSold_count):
        productSold_item = input()
        productSold.append(productSold_item)

    soldPrice_count = int(input().strip())

    soldPrice = []

    for _ in range(soldPrice_count):
        soldPrice_item = float(input().strip())
        soldPrice.append(soldPrice_item)

    result = priceCheck(products, productPrices, productSold, soldPrice)

    fptr.write(str(result) + '\n')

    fptr.close()

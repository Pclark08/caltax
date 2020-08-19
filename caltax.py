"""Based on maryland tax laws"""

stand_tax_rate = 0.06

print("What is the price of the item?:")

""" User input is saved to tax variable"""
tax = float(input()) 

"""tax calculation"""

def get_price_tax(t):
	return t * (1 + stand_tax_rate)

final_price = get_price_tax(tax)

print('Cost after tax')

"""Formats variable final_price two decimal places"""

print("${:.2f}".format(final_price))


	


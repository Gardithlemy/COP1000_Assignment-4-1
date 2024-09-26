"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.

charge=0
numChars=8.
color="gold"
woodType="oak"

minPay=35
# Write assignment and if statements here as appropriate.
if numChars>5:
    charge += (numChars-5)*4
if woodType =="oak":
    charge+=20
if color=="gold":
      charge+=15
charge+=minPay
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))

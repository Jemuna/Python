#🛒 Bitcoin and Basket Cost Calculator
##Project Overview

This project includes two mini Python programs:
Shopping Basket Cost Calculator
Calculates the total basket cost including shipping.
If the basket total is over $100, shipping is free.
If under $100, shipping is charged at $1.20 per kg.
Bitcoin Investment Tracker
Calculates your Bitcoin investment value in USD.
Warns you if the investment falls below $30,000.

##How It Works
🛍 Basket Cost Calculation
##User inputs:

Total basket cost ($)
Total basket weight (kg)

##Logic:

If basket cost ≥ $100 → Free shipping.

If basket cost < $100 → Shipping = $1.20 × weight.

##Output:

Final basket cost including shipping.
₿ Bitcoin Investment Tracker

##User inputs:

Investment in Bitcoin.

##Logic:

Bitcoin value is fixed at $40,000 per Bitcoin.
Investment = Bitcoin amount × $40,000.
If investment ≤ $30,000 → Warn user to sell.

##Technologies Used

Python 3
Command-line Interface (CLI)

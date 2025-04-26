shipping_cost_per_kg = 1.20

customer_basket_cost = float(input("Enter your basket total cost ($): "))
customer_basket_weight = float(input("Enter your basket total weight (kg): "))

if customer_basket_cost >= 100:
    print('Free shipping!')
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_basket_cost += shipping_cost

print(f"Total basket cost including shipping is: ${customer_basket_cost:.2f}")

investment_in_bitcoin = float(input("\nEnter your Bitcoin investment amount: "))
bitcoin_to_usd = 40000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)

if investment_in_usd <= 30000:
    print("Investment below $30,000! SELL!")
else:
    print("Investment above $30,000!")

from datetime import datetime
DISCOUNT_DAYS=[2,3]
DISCOUNT_RATE=.1
TAX_RATE=.06
today=datetime.now()
dow=today.weekday()
subtotal=0
quantity=1
while quantity !=0:
   quantity=int(input("enter the quantity: "))
   if quantity !=0:
      price=float(input("enter the price: "))
      subtotal+=quantity * price

print(f"Total order {subtotal: .2f} ")
discount=0
if dow in [2,3]:
  if subtotal > 50:
    discount=round(subtotal * DISCOUNT_RATE,2)
    print(f"Discount {discount: .2f} ")
  else:
    short=50-subtotal
    print(f"you get a discount by ordering {short} more.")
subtotal -= discount
tax=round(subtotal * TAX_RATE,2)
total=subtotal + tax

print(f"Tax {tax:.2f}")
print(f"Total due {total: .2f} ")
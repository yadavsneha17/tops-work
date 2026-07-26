sales_data = [
    {"product": "Pen", "price": 10, "units_sold": 150},
    {"product": "Notebook", "price": 50, "units_sold": 90},
    {"product": "Pencil", "price": 5, "units_sold": 300}
]
total = 0
#Income = Price × Units Sold
#Total Income = Sum of incomes where Units Sold > 100
for i in sales_data:
    if i["units_sold"] > 100:
        total = total + (i["price"] * i["units_sold"])
print("Total Income =", total)


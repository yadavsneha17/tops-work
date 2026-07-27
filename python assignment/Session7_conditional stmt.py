# SESSION 7 - Conditional Statements

# Task 1
print("===== Task 1 =====")
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for IPL ticket booking")
else:
    print("Not eligible")


# Task 2
print("\n===== Task 2 =====")
followers = int(input("Enter number of followers: "))
if followers < 10000:
    print("Micro Influencer")
elif followers <= 100000:
    print("Rising Star")
else:
    print("Celebrity")


# Task 3
print("\n===== Task 3 =====")
order_total = int(input("Enter Zomato order total: ₹"))
if order_total > 299:
    print("Apply Free Delivery")
elif order_total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")


# Task 4
print("\n===== Task 4 =====")
cart_value = float(input("Enter Flipkart cart value: ₹"))
payment = input("Enter payment method (UPI/Card/Cash): ")
if cart_value > 1000:
    if payment.lower() == "upi":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")
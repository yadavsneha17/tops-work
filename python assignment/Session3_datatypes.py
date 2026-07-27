# SESSION 3 - Data Types in Python

# Task 1
print("===== Task 1 =====")

followers = 2500
average_rating = 4.7
favorite_app = "Instagram"
is_premium_user = True

print("Followers:", followers, "-", type(followers))
print("Average Rating:", average_rating, "-", type(average_rating))
print("Favorite App:", favorite_app, "-", type(favorite_app))
print("Premium User:", is_premium_user, "-", type(is_premium_user))

# Task 2
print("\n===== Task 2 =====")
price = input("Enter Zomato Order Price: ")
price = float(price)
gst = price * 0.18
final_bill = price + gst
print("GST (18%): ", gst)
print("Final Bill Amount: ", final_bill)

# Task 3
print("\n===== Task 3 =====")
prices = ['199.99', '299.50', '150']
float_prices = []
for price in prices:
    float_prices.append(float(price))
total = sum(float_prices)
print("Converted Prices:", float_prices)
print("Total Cart Value: ₹", total)


# Task 4
print("\n===== Task 4 =====")
def is_discount_applicable(order_amount):
    return order_amount > 500
print("Order Amount: 450 ->", is_discount_applicable(450))
print("Order Amount: 750 ->", is_discount_applicable(750))

# Task 5
print("\n===== Task 5 =====")
ratings = ['4.5', '3.0', '5', '4.2']
float_ratings = []
for rating in ratings:
    float_ratings.append(float(rating))
highest_rating = max(float_ratings)
print("Converted Ratings:", float_ratings)
print("Highest Rating:", highest_rating)
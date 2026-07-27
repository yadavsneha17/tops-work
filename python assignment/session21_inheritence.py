#==========================================
# SESSION 21 - Inheritance & Polymorphism
# ==========================================

# -------------------------------
# Task 1
# -------------------------------

class Product:
    def get_discount(self):
        return 0


class Electronics(Product):
    def get_discount(self):
        return 10


e = Electronics()
print("Task 1")
print("Discount:", e.get_discount(), "%")


# -------------------------------
# Task 2
# -------------------------------

class FoodOrder:
    def __init__(self, price):
        self.price = price

class ZomatoOrder(FoodOrder):
    def calculate_total(self):
        delivery_charge = self.price * 0.05
        return self.price + delivery_charge

a = ZomatoOrder(500)

print("\nTask 2")
print("Total Bill:", a.calculate_total())



# -------------------------------
# Task 3
# -------------------------------

class Influencer:
    def bonus(self):
        return 2000


class BrandManager:
    def bonus(self):
        return 5000


def show_bonus(employee):
    print("Bonus:", employee.bonus())


print("\nTask 3")
show_bonus(Influencer())
show_bonus(BrandManager())


# -------------------------------
# Task 4
# -------------------------------

class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


user = User()
premium = PremiumUser()

print("\nTask 4")
print("User Status:", user.get_status())
print("Premium User Status:", premium.get_status())
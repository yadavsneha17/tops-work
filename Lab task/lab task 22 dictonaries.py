dict1 = {
    "india": ["Delhi", "INR", "+91"],
    "france": ["paris","euro","+33"],
    "USA": ["new york", "USD", "+1"]
}
print(dict1)
detail = input("enter a code,currency,capital: ")
for country, details in dict1.items():
    if detail in details:
        print("Country:",country)
        break
else:
    print("Not found in dictionary")



# dict2 = {
#     "+91": "india",
#     "inr": "india",
#     "delhi": "india",
#     "+1": "usa",
#     "usd": "
#     "new york": "usa",
#     "+33": "france",
#     "eur": "france",
#     "paris": "france"
# }
# country_code_capital = input("Enter a country code , capital, currency : ")
# if country_code_capital in dict2:
#     print("Country:", dict2[country_code_capital])
# else:
#     print("Not found in dictionary")
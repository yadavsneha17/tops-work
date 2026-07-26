city_data = {
    "Ahmedabad": (
        ("Ambawadi", 380006),
        ("Bodakdev", 380054),
        ("Gandhi Ashram", 380027)
    ),
    "Mumbai": (
        ("Mandvi", 400003),
        ("Mumbai Central", 400008),
        ("Worli", 400018)
    )
}
def data(value):
    if value in city_data:
        print("Areas in", value)
        for area, pin in city_data[value]:
            print(area, "-->", pin)
        return
   
   
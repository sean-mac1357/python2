# dictionary inside of a dictionary
digitalcrafts = {
    "US": {
        "Georgia": {
            "Atlanta": "3442 Piedmont Rd NE #420"
        },
        "Texas": {
            "Houston": "1334 Brittmore Rd #1327"
        }
    }
}
print(digitalcrafts["US"])
print(digitalcrafts["US"]["Georgia"])
print(digitalcrafts["US"]["Georgia"]["Atlanta"])

digitalcrafts["US"]["South Carolina"] = {
    "Bluffton": "123 Sesame Street"
}
print(digitalcrafts["US"])


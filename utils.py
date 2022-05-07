import json


def get_users_data():
    with open("data_json/users.json", "r", encoding="utf8") as file:
        data = json.load(file)
        return data


def get_orders_data():
    with open("data_json/orders.json", "r", encoding="utf8") as file:
        data = json.load(file)
        return data


def get_offers_data():
    with open("data_json/offers.json", "r", encoding="utf8") as file:
        data = json.load(file)
        return data

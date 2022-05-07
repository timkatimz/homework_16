from models import User, Order, Offer, db
from utils import get_users_data, get_orders_data, get_offers_data


users = get_users_data()
for i in users:
    user = User(
        id=i["id"],
        first_name=i["first_name"],
        last_name=i["last_name"],
        age=i["age"],
        email=i["email"],
        role=i["role"],
        phone=i["phone"]
    )
    db.session.add(user)


orders = get_orders_data()
for i in orders:
    order = Order(
        id=i["ide"],
        name=i["name"],
        description=i["description"],
        start_date=i["start_date"],
        end_date=i["end_date"],
        address=i["address"],
        price=i["price"],
        customer_id=i["customer_id"],
        executor_id=i["executor_id"],
    )
    db.session.add(order)


offers = get_offers_data()
for i in offers:
    offer = Offer(
        id=i["id"],
        order_id=i["order_id"],
        executor_id=i["executor_id"]
    )
    db.session.add(offer)
db.session.commit()

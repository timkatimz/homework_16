from flask import jsonify, request
from models import app, db
from models import User, Order, Offer
import sqlalchemy.exc


@app.route("/users", methods=["GET", "POST"])
def show_all_users():
    if request.method == "GET":
        resp = db.session.query(User).all()
        all_users = []
        for user in resp:
            data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            }
            all_users.append(data)
        return jsonify(all_users)
    if request.method == "POST":
        try:
            new_user = request.get_json()
            for i in new_user:
                user = User(
                    first_name=i["first_name"],
                    last_name=i["last_name"],
                    age=i["age"],
                    email=i["email"],
                    role=i["role"],
                    phone=i["phone"]
                )
            db.session.add(user)
            db.session.commit()
            return "New user successful added"
        except Exception:
            return "Something went wrong"


@app.route("/users/<int:gid>", methods=["GET", "PUT", "DELETE"])
def show_user_by_id(gid):
    if request.method == "GET":
        try:
            user = db.session.query(User).filter(User.id == gid).one()
            data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            }
            return jsonify(data)
        except sqlalchemy.exc.NoResultFound:
            return "No row was found when one was required"

    if request.method == "PUT":
        try:
            update_user = request.get_json()
            user_by_id = User.query.get(gid)
            for i in update_user:
                user_by_id.first_name = i["first_name"]
                user_by_id.last_name = i["last_name"]
                user_by_id.age = i["age"]
                user_by_id.email = i["email"]
                user_by_id.role = i["role"]
                user_by_id.phone = i["phone"]

            db.session.add(user_by_id)
            db.session.commit()
            return "Users data successful updated"
        except Exception:
            return "Something went wrong"

    if request.method == "DELETE":
        try:
            delete_user = User.query.get(gid)
            db.session.delete(delete_user)
            db.session.commit()
            return "Users data successful deleted"
        except Exception:
            return "Something went wrong"


@app.route("/orders/", methods=["GET", "POST"])
def show_all_orders():
    if request.method == "GET":
        orders = db.session.query(Order).all()
        all_orders = []
        for order in orders:
            data = {
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price,
                "customer_id": order.customer_id,
                "executor_id": order.executor_id
            }
            all_orders.append(data)
        return jsonify(all_orders)

    if request.method == "POST":
        try:
            new_order = request.get_json()
            for i in new_order:
                order = Order(
                    name=i["name"],
                    description=i["description"],
                    start_date=i["start_date"],
                    end_date=i["end_date"],
                    address=i["address"],
                    price=i["price"],
                    customer_id=i["customer_id"],
                    executor_id=i["executor_id"]
                )
                db.session.add(order)
                db.session.commit()
            return "New user successful added"
        except Exception:
            return "Something went wrong"


@app.route("/orders/<int:gid>", methods=["GET", "PUT", "DELETE"])
def show_order_by_id(gid):
    if request.method == "GET":
        try:
            order = db.session.query(Order).filter(Order.id == gid).one()
            data = {
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price,
                "customer_id": order.customer_id,
                "executor_id": order.executor_id
            }
            return jsonify(data)
        except sqlalchemy.exc.NoResultFound:
            return "No row was found when one was required"

    if request.method == "PUT":
        try:
            update_order = request.get_json()
            order_by_id = Order.query.get(gid)
            for i in update_order:
                order_by_id.name = i["name"]
                order_by_id.description = i["description"]
                order_by_id.start_date = i["start_date"]
                order_by_id.end_date = i["end_date"]
                order_by_id.address = i["address"]
                order_by_id.price = i["price"]
                order_by_id.customer_id = i["customer_id"]
                order_by_id.executor_id = i["executor_id"]

                db.session.add(order_by_id)
                db.session.commit()
            return "Orders data successful updated"
        except Exception:
            return "Something went wrong"

    if request.method == "DELETE":
        try:
            delete_order = Order.query.get(gid)
            db.session.delete(delete_order)
            db.session.commit()
            return "Orders data successful deleted"
        except Exception:
            return "Something went wrong"


@app.route("/offers/", methods=["GET", "POST"])
def show_all_offers():
    if request.method == "GET":
        try:
            offers = db.session.query(Offer.id,
                                      Order.name,
                                      Order.description,
                                      Order.start_date,
                                      Order.end_date,
                                      User.first_name,
                                      User.last_name,
                                      User.phone
                                      ).join(Offer.order).join(Offer.executor).all()
            all_offers = []
            for offer in offers:
                data = {
                    "offer_id": offer.id,
                    "order_name": offer.name,
                    "description": offer.description,
                    "start_date": offer.start_date,
                    "end_date": offer.end_date,
                    "first_name": offer.first_name,
                    "last_name": offer.last_name,
                    "phone": offer.phone
                }
                all_offers.append(data)
            return jsonify(all_offers)
        except sqlalchemy.exc.NoResultFound:
            return "No row was found when one was required"

    if request.method == "POST":
        try:
            new_offer = request.get_json()
            for i in new_offer:
                offer = Offer(
                    order_id=i["order_id"],
                    executor_id=i["executor_id"]
                )
                db.session.add(offer)
                db.session.commit()
            return "New offer successful added"
        except Exception:
            return "Something went wrong"


@app.route("/offers/<int:gid>", methods=["GET", "PUT", "DELETE"])
def show_offer_by_id(gid):
    if request.method == "GET":
        try:
            offer = db.session.query(Offer.id,
                                     Order.name,
                                     Order.description,
                                     Order.start_date,
                                     Order.end_date,
                                     User.first_name,
                                     User.last_name,
                                     User.phone
                                     ).join(Offer.order).join(Offer.executor) \
                .filter(Offer.id == gid).one()

            data = {
                "offer_id": offer.id,
                "order_name": offer.name,
                "description": offer.description,
                "start_date": offer.start_date,
                "end_date": offer.end_date,
                "first_name": offer.first_name,
                "last_name": offer.last_name,
                "phone": offer.phone
            }
            return jsonify(data)
        except sqlalchemy.exc.NoResultFound:
            return "No row was found when one was required"

    if request.method == "PUT":
        try:
            update_offer = request.get_json()
            offer_by_id = Offer.query.get(gid)
            for i in update_offer:
                offer_by_id.order_id = i["order_id"]
                offer_by_id.executor_id = i["executor_id"]

                db.session.add(offer_by_id)
                db.session.commit()
            return "Offers data successful updated"
        except Exception:
            return "Something went wrong"

    if request.method == "DELETE":
        try:
            delete_offer = Offer.query.get(gid)
            db.session.delete(delete_offer)
            db.session.commit()
            return "Offers data successful deleted"
        except Exception:
            return "Something went wrong"


if __name__ == "__main__":
    app.run()

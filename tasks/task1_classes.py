"""Classes for the shop management system: products, customers and orders."""

from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class for a product with a name, price and stock amount."""

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def change_price(self, new_price):
        """Set a new price for the product."""
        self.price = new_price

    def change_amount(self, new_amount):
        """Set a new stock amount for the product."""
        self.amount = new_amount

    def __repr__(self):
        return f"{self.name} ({self.apply_category()}): {self.price} hr. Available: {self.amount}"

    @abstractmethod
    def apply_category(self):
        """Return the product's category name; implemented by each subclass."""


class Electronics(Product):
    """Product in the electronics category."""

    def apply_category(self):
        """Return the category name."""
        return "Electronics"


class Sport(Product):
    """Product in the sport category."""

    def apply_category(self):
        """Return the category name."""
        return "Sport"


class Car(Product):
    """Product in the car category."""

    def apply_category(self):
        """Return the category name."""
        return "Car"


class Customer:
    """A customer with a name, email and a list of their orders."""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders_list = []

    def add_order(self, order):
        """Add an order to the customer's order list."""
        self.orders_list.append(order)

    def __repr__(self):
        return f"Customer: {self.name} with email: {self.email}"


class Order:
    """An order holding a list of products and their total amount."""

    def __init__(self):
        self.goods_list = []
        self.total_amount = 0

    def add_goods(self, *items):
        """Add one or more products to the order and recalculate the total."""
        self.goods_list.extend(items)
        self.calculate_total_amount()

    def calculate_total_amount(self):
        """Calculate and store the total amount as the sum of product prices."""
        self.total_amount = sum(item.price for item in self.goods_list)

    def __repr__(self):
        goods = ", ".join(good.name for good in self.goods_list)
        return f"Goods in order: {goods} with total amount: {self.total_amount} hr"


if __name__ == "__main__":
    tv = Electronics("Samsung", 30000, 12)
    laptop = Electronics("Lenovo", 50000, 9)
    wheel = Car("Debica", 5000, 42)
    soccer_ball = Sport("Select", 4000, 22)
    soccer_shoes = Sport("Nike Mercurial", 8000, 22)

    print(
        f"list of Products: \n {tv.name}, {laptop.name}, {wheel.name}, {soccer_ball.name}, {soccer_shoes.name}"
    )

    ihor_horobets = Customer("Ihor Horobets", "ihor.horobets@python.com")
    artem_milevskyi = Customer("Artem Milevskyi", "artem.milevskyi@dynamo.com")
    print(f"List of customers: {ihor_horobets.name}, {artem_milevskyi.name}")

    first_order = Order()
    first_order.add_goods(laptop, soccer_ball)
    second_order = Order()
    second_order.add_goods(wheel, tv, soccer_shoes)
    print(f"List of orders: \n Order 1: {first_order} \n Order 2: {second_order}")

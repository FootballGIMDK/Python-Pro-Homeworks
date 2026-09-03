"""Reading the shop's initial state from a text file and saving orders to disk."""

from datetime import datetime
from pathlib import Path

from tasks.task1_classes import Car, Customer, Electronics, Sport

CATEGORY_MAP = {"Car": Car, "Electronics": Electronics, "Sport": Sport}


def get_shop_items(path):
    """Read products and customers from a text file.

    Args:
        path: Path to the source text file.

    Returns:
        A tuple ``(goods_list, customer_list)`` of Product and Customer objects.
    """
    goods_list = []
    customer_list = []
    header = str
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.endswith(":"):
                header = line[:-1].lower()
                continue

            if header == "products":
                name, category, price, amount = line.split(",")
                product = CATEGORY_MAP[category](name, int(price), int(amount))
                goods_list.append(product)

            if header == "customers":
                name, email = line.split(",")
                name, email = name.strip(), email.strip()
                customer_list.append(Customer(name, email))

    return goods_list, customer_list


def save_new_order(customer, order):
    """Save a customer's order to the text file with unique name.

    Args:
        customer: The Customer who placed the order.
        order: The Order to save.
    """
    customer_order = customer.name.replace(" ", "_")
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"new_order_{customer_order}_{timestamp}.txt"
    orders_dir = Path("tasks/mocks/orders")
    orders_dir.mkdir(parents=True, exist_ok=True)
    file_path = orders_dir / filename
    goods_names = ", ".join(product.name for product in order.goods_list)
    order.calculate_total_amount()

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Customer {customer.name} with {customer.email} make a new order\n")
        file.write(
            f"Product(s): {goods_names} with total amount: {order.total_amount}\n"
        )

    print(f"Saved order to {file_path}")

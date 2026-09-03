"""Entry point that runs the interactive shop and saves a new order."""

from tasks.task1_classes import Customer, Order
from tasks.task2_txt import get_shop_items, save_new_order


def main():
    """List the shop's items, register a new customer and save their order."""
    products, customers = get_shop_items("tasks/mocks/data.txt")
    print("Available Products")
    for product in products:
        print(product)
    print("Existing customers:")
    for customer in customers:
        print(customer)

    customer_name = input("Enter your full name: ")
    customer_email = input("Enter your email: ")

    new_customer = Customer(customer_name, customer_email)
    new_order = Order()
    new_order.add_goods(products[2], products[3])
    new_customer.add_order(new_order)

    save_new_order(new_customer, new_order)


if __name__ == "__main__":
    main()

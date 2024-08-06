"""Create a base class Order with attributes like items (list) and total_price. Define a method calculate_subtotal that sums the prices of all items. Create subclasses OnlineOrder and InStoreOrder inheriting from Order. In OnlineOrder, implement a method apply_discount that reduces the total price by a fixed percentage. In InStoreOrder, implement a method apply_coupon that takes a coupon code and applies a discount based on pre-defined rules."""
# Base class Order
class Order:
    def __init__(self, items):
        self.items = items
        self.total_price = 0

    def calculate_subtotal(self):
        self.total_price = sum(item['price'] * item['quantity'] for item in self.items)
        return self.total_price


# Subclass OnlineOrder inheriting from Order
class OnlineOrder(Order):
    def __init__(self, items):
        super().__init__(items)

    def apply_discount(self, discount_percentage):
        discount_amount = self.total_price * (discount_percentage / 100)
        self.total_price -= discount_amount
        return self.total_price


# Subclass InStoreOrder inheriting from Order
class InStoreOrder(Order):
    def __init__(self, items):
        super().__init__(items)
        self.coupon_rules = {
            '10OFF': 10,
            '20OFF': 20,
            '30OFF': 30
        }

    def apply_coupon(self, coupon_code):
        if coupon_code in self.coupon_rules:
            discount_percentage = self.coupon_rules[coupon_code]
            discount_amount = self.total_price * (discount_percentage / 100)
            self.total_price -= discount_amount
        else:
            print("Invalid coupon code")
        return self.total_price


# Example usage
if __name__ == "__main__":
    items = [
        {'name': 'Item 1', 'price': 10.99, 'quantity': 2},
        {'name': 'Item 2', 'price': 5.99, 'quantity': 3}
    ]

    online_order = OnlineOrder(items)
    online_order.calculate_subtotal()
    print("Online Order Subtotal:", online_order.total_price)
    online_order.apply_discount(10)
    print("Online Order Total after discount:", online_order.total_price)

    in_store_order = InStoreOrder(items)
    in_store_order.calculate_subtotal()
    print("In-Store Order Subtotal:", in_store_order.total_price)
    in_store_order.apply_coupon('10OFF')
    print("In-Store Order Total after coupon:", in_store_order.total_price)

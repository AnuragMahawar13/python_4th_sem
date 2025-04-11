#Q47.Program to create a class representing a shopping cart.Includes methods for adding and removing items and calculating total price.
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price, quantity=1):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} x {item} to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            if self.cart[item]['quantity'] > quantity:
                self.cart[item]['quantity'] -= quantity
                print(f"Removed {quantity} x {item} from the cart.")
            else:
                del self.cart[item]
                print(f"Removed {item} completely from the cart.")
        else:
            print(f"{item} not found in cart.")

    def calculate_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        return total

    def display_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("Items in Cart:")
        for item, details in self.cart.items():
            print(f"{item} - rupee{details['price']} x {details['quantity']}")

# Example usage
cart_1 = ShoppingCart()
cart_1.add_item("watermelon", 30, 5)
cart_1.add_item("Banana", 20, 5)
cart_1.remove_item("watermelon", 2)
cart_1.display_cart()
print("Total Price: $", cart_1.calculate_total())
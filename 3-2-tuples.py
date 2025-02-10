def format_itineraries(itineraries):
    """
    Takes a list of tuples containing flight itineraries and returns a formatted string.
    
    Args:
    itineraries (list of tuples): Each tuple contains (traveler_name, origin, destination).
    
    Returns:
    str: A formatted string listing each itinerary.
    """
    formatted_str = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        formatted_str += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_str.strip()

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(itineraries))

def add_book(library, new_book):
    if new_book not in library:
        library.append(new_book)
    else:
        print("This book is already in the library.")

# Example usage
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library, ("Fahrenheit 451", "Ray Bradbury"))
add_book(library, ("1984", "George Orwell"))
print(library)
def display_orders(orders):
    for customer_name, product_ordered, quantity in orders:
        print(f"Customer: {customer_name}, Product: {product_ordered}, Quantity: {quantity}")

# Example usage
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]
display_orders(orders)


# coffee-shop

A Python OOP mini-project focused on object relationships and class design using three core models: `Customer`, `Coffee`, and `Order`. This challenge helps reinforce principles like aggregation, encapsulation, and data validation.

---

##  Project Structure

coffee-shop/
├── Pipfile # Pipenv dependencies
├── Pipfile.lock
├── debug.py # Manual test runner / output viewer
├── customer.py # Customer model
├── coffee.py # Coffee model
├── order.py # Order model
└── tests/ # Unit tests
├── customer_test.py
├── coffee_test.py
└── order_test.py

markdown
Copy
Edit

---

##  Domain Overview

**Model Relationships:**
- A `Customer` has many `Orders`
- A `Coffee` has many `Orders`
- An `Order` belongs to one `Customer` and one `Coffee`
- **Many-to-many** relationship between `Customer` and `Coffee` through `Order`

---

## Requirements

### `Customer`
- `__init__(self, name)` — `name` must be a string (1–15 characters)
- `name` property (getter/setter with validation)
- `orders()` → List of that customer's `Order` instances
- `coffees()` → Unique list of `Coffee` instances the customer has ordered
- `create_order(coffee, price)` → Creates a new `Order` instance
- `@classmethod most_aficionado(cls, coffee)` → Returns the customer who spent the most on a specific coffee (Bonus)

### `Coffee`
- `__init__(self, name)` — `name` must be a string (min 3 characters)
- `name` property (getter only; immutable)
- `orders()` → List of all `Order` instances for that coffee
- `customers()` → Unique list of `Customer` instances who’ve ordered it
- `num_orders()` → Returns total number of orders
- `average_price()` → Returns average price across all orders

### `Order`
- `__init__(self, customer, coffee, price)` — Requires valid `Customer`, `Coffee`, and a float `price` (1.0–10.0)
- `customer` property (getter)
- `coffee` property (getter)
- `price` property (getter, immutable)

---

##  Running the Project

### 1. Clone the repository
```bash
git clone git@github.com:christine-muigai/coffee-shop.git
cd coffee-shop



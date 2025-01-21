def supermarket():
  """
  Simulates a simple supermarket checkout.
  """
  product_prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
  total_sum = 0

  print("Supermarket")
  print("===========")

  while True:
    product_number = int(input("Please select product (1-10) 0 to Quit: "))
    if product_number == 0:
      break
    if 1 <= product_number <= 10:
      price = product_prices[product_number - 1]  # Adjust for zero-based indexing
      print(f"Product: {product_number} Price: {price}")
      total_sum += price
    else:
      print("Invalid product number.")

  print(f"Total: {total_sum}")
  payment = float(input("Payment: "))
  change = payment - total_sum
  print(f"Change: {change}")

if _name_ == "_main_":
  supermarket()
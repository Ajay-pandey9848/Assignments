def main():
  """
  Manages the grocery shopping list.
  """
  shopping_list = []

  while True:
    choice = input("Would you like to (1)Add or (2)Remove items or (3)Quit?: ")
    if choice == '1':  # Add item
      item = input("What will be added?: ")
      shopping_list.append(item)
    elif choice == '2':  # Remove item
      if len(shopping_list) == 0:
        print("The list is empty.")
      else:
        print("There are", len(shopping_list), "items in the list.")
        try:
          remove_index = int(input("Which item is deleted?: ")) - 1
          if 0 <= remove_index < len(shopping_list):
            del shopping_list[remove_index]
          else:
            print("Incorrect selection.")
        except ValueError:
          print("Incorrect selection.")
    elif choice == '3':  # Quit
      print("The following items remain in the list:")
      for item in shopping_list:
        print(item)
      break
    else:
      print("Incorrect selection.")

if _name_ == "_main_":
  main()
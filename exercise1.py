def tester(givenstring="Too short"):
  """
  Prints the given string. If the string is shorter than 10 characters,
  it prints the default value "Too short".

  Args:
    givenstring: The string to be printed. Defaults to "Too short".
  """
  if len(givenstring) < 10:
    print("Too short")
  else:
    print(givenstring)

def main():
  """ Prompts the user for input and calls the tester function."""
  while True:
    user_input = input("Write something (quit ends): ")
    if user_input.lower() == "quit":
      break
    tester(user_input)

if _name_ == "_main_":
  main()
  
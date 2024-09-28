import Main

def start():
  # list of skin gradation colors
  variables = {
      1: "Hello",
      2: "World",
      3: "Python",
      4: "Programming",
      5: "is Fun"
  }

  # Display option to the user

  print("List of gradation skin")
  for key, value in variables.items():
      print(f"{key}. {value}")

  choices = input("Select your option, can choose more than one. Ex:123): ") # Ask the user to choose a skin gradation color
  choices = [int(choice.strip()) for choice in choices] # Casting to integer value
  result = "".join([variables[choice] for choice in choices if choice in variables]) # combine the gradation option

  # Output
  print("\nHere is your gradation skin code!")
  print(result)


if __name__ == '__main__':
  start()
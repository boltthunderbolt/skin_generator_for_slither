def start():
  countries_skin_list = [
    ['india', india_skins],
    ['indonesia', indonesia_skins],
    ['malaysia', malaysia_skins],
    ['vietnam', vietnam_skins],
    ['singapore', singapore_skins],
    ['pakistan', pakistan_skins],
    ['bangladesh', bangladesh_skins],
    ]
  countries_skin_list.sort()
  for option, skin_option in enumerate(countries_skin_list, start = 1):
    print(f"{option}. {skin_option[0].capitalize()}");

  global characters_length
  while True:
    try:
      user_input = int(input("\nChoose your snake skins: "))
      characters_length = int(input("Set the length characters of skin code (minimum 5 characters): "))
      if characters_length < 5:
        print("Please set more than equal 5 characters!");
      else:
        user_input -= 1
        print(f"{countries_skin_list[user_input][0].capitalize()} selected");
        user_input = countries_skin_list[user_input][1]() # call the value of function from array
        break
    except ValueError:
      print(f"Please select by number!");

def india_skins():
  print('y' * characters_length + 's' * int(characters_length / 2) + '4' * int(characters_length / 4) + 's' * int(characters_length / 2) + 'o' * characters_length)
def indonesia_skins():
  print('5' * characters_length + 's' * characters_length)
def malaysia_skins():
  print('s' * int(characters_length / 2) + '4' * int(characters_length / 2) + 'w' * int(characters_length / 2) + '4' * int(characters_length / 2) + ('s' * int(characters_length / 5) + '5' * int(characters_length / 5)) * 7)
def vietnam_skins():
  print(',' * characters_length + 'w' * int(characters_length / 5));
def singapore_skins():
  print(',' * characters_length + ('s' * int(characters_length / 5) + ',' * int(characters_length / 5)) * 5 + 's' * characters_length)
def pakistan_skins():
  print('h' * characters_length + 's' * int(characters_length / 2) + 'h' * int(characters_length / 2) + 's' * int(characters_length / 5) + 'h' * int(characters_length / 2) + 's' * int(characters_length / 1.5) + 'h' * characters_length)
def bangladesh_skins():
  print('h' * int(characters_length / 2.5) + ',' * int(characters_length / 2) + 'h' * characters_length)
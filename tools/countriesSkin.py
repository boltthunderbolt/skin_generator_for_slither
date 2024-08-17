import Main

def start():
  countries_skin_list = [
    ['india', india_skins],
    ['indonesia', indonesia_skins],
    ['malaysia', malaysia_skins],
    ['vietnam', vietnam_skins],
    ['singapore', singapore_skins],
    ['pakistan', pakistan_skins],
    ['bangladesh', bangladesh_skins],
    ['france', france_skins],
    ['finland', finland_skins],
    ['brazil', brazil_skins],
    ['japan', japan_skins],
    ['australia', australia_skins],
    ['new zealand', new_zealand_skins]
    ]
  
  countries_skin_list.sort()
  print()
  for option, skin_option in enumerate(countries_skin_list, start = 1):
    print(f"{option}. {skin_option[0].title()}")

  global characters_length
  while True:
    try:
      user_input = int(input("\nChoose your snake skins: "))
      if 1 < user_input > len(countries_skin_list):
        print(f"Choose from 1 - {len(countries_skin_list)}")
      else: break
    except ValueError:
      print(f"Please select by number!");
  
  while True:
    try:
      characters_length = int(input("Set the length characters of skin code (minimum 5 characters): "))
      if characters_length < 5:
        print("Please set more than equal 5 characters!");
      else:
        user_input -= 1
        print(f"\n{countries_skin_list[user_input][0].capitalize()} selected");
        user_input = countries_skin_list[user_input][1]() # call the value of function from array
        print()

        while True:
          generate_again = input("Want to generate again? [enter / n]: ")
          match generate_again:
            case "n" | "no" | "N" | "No" | "NO":
              print(Main.CLEAR, Main.CLEAR_AND_RETURN)
              Main.menu()
              break
            case _:
              start()
              break
      break
    except ValueError:
      print(f"Please select by number!");

# =======================================================================
def india_skins():
  print('y' * characters_length + 's' * int(characters_length / 2) + '4' * int(characters_length / 4) + 's' * int(characters_length / 2) + 'o' * characters_length)

def indonesia_skins():
  print('5' * characters_length + 's' * characters_length)
  print('2' * characters_length + 's' * characters_length)

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

def france_skins():
  print('4' * characters_length + 's' * characters_length + '2' * characters_length)

def finland_skins():
  print('s' * characters_length + '4' * int(characters_length / 5) + 's' * int(characters_length / 5) + '4' * characters_length)

def brazil_skins():
  print('o' * int(characters_length / 1.5) + 'w' * int(characters_length / 2) + 'e' * int(characters_length / 2) + 's' * int(characters_length / 5) + 'e' * int(characters_length / 2) + 'w' * int(characters_length / 2))

def japan_skins():
  print('s' * characters_length + '5' * int(characters_length / 1.5))
  print('s' * characters_length + '2' * int(characters_length / 1.5))

def australia_skins():
  print(',' * int(characters_length / 1.5) + ('4' * int(characters_length / 2) + 's' * int(characters_length / 5)) * 5 + '4' * characters_length)

def new_zealand_skins():
  print(',' * int(characters_length / 1.5) + ('4' * int(characters_length / 2) + ',' * int(characters_length / 5)) * 4 + '4' * characters_length)
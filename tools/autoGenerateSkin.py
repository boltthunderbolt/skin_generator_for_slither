from libs import skinLibrary
import Main
import random

def start():
  global length
  while True:
    try:
      length = int(input("\nSet the length characters of skin code as you like: "))
      if length < 2:
        print("Length must bigger than 1 characters")
        return start()
      break
    except ValueError:
      print(f"{length} is not an integer, Try again")
  
def show_results():
  while True:
    auto_generate_result = auto_generate_skin_process(length)
    print(f"\nGenerate result: {auto_generate_result}")
    generate_again = input("Generate again? [enter / n] ")
    match generate_again:
      case "n" | "no" | "N" | "No" | "NO":
        print('\n' * 100)
        return Main.menu()
      case _: return show_results()


def auto_generate_skin_process(length):
  # Get characters from tools/skinLibrary
  skin_code_characters = [sublist[1] for sublist in skinLibrary.skin_code_list]

  # Generate random skin
  skin_codes = ''.join(random.choice(skin_code_characters) for _ in range(length))
  return skin_codes
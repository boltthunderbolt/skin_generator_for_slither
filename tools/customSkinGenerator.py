from libs.skinLibrary import show_skin_list
import Main
import random

def start():
  global length, skin_reference_by_user_input
  while True:
    try:
      length = int(input("\nSet the length characters of skin code as you like: "))
    
      print("================================\n")
      show_skin_list()
      print("================================\n")

      while True:
        skin_reference_by_user_input = get_skin_reference_input()
        if len(skin_reference_by_user_input) > length:
          print(f"\nYour skin code more than {length}");
        else : break
      break
    except ValueError:
      print(f"{length} is not an integer. Try again!")

def show_results():
  while True:
    skin_code_generate_result = generate_skin_code_by_user_reference(length, skin_reference_by_user_input)
    print(f"\nGenerate result: {skin_code_generate_result}")
    generate_again = input("Generate again? [enter / n] ")
    match generate_again:
      case "n" | "no" | "N" | "No" | "NO":
        print('\n' * 100);
        return Main.menu()
      case _: return show_results()

# =======================================================================================

def get_skin_reference_input():
  skin_reference_by_user_input = input("Input the skin part of your code: ")
  return skin_reference_by_user_input

def generate_skin_code_by_user_reference(length, skin_reference_by_user_input):
  skin_code = skin_reference_by_user_input
  while len(skin_code) < length:
    skin_code += random.choice(skin_code)
  
  skin_code = ''.join(random.sample(skin_code, len(skin_code)))
  return skin_code

if __name__ == '__main__':
  start()
  show_results()
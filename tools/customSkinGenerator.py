from libs.skinLibrary import show_skin_list
from Main import main
import random

def start():
  global length, skin_reference_by_user_input
  try:
    length = int(input("\nSet the length characters of skin code as you like: "))
    if length < 1:
      print("Length must bigger than 0")
      return start()
    
    print("================================\n")
    show_skin_list()
    print("================================\n")

    while True:
      skin_reference_by_user_input = get_skin_reference_input()
      if len(skin_reference_by_user_input) > length:
        print(f"\nYour skin code more than {length}");
      else : break
  except ValueError:
    raise ValueError

def show_results():
  while True:
    skin_code_generate_result = generate_skin_code_by_user_reference(length, skin_reference_by_user_input)
    print(f"\nGenerate result: {skin_code_generate_result}")
    generate_again = input("Generate again? [y/n] ")
    match generate_again:
      case "n" | "no" | "N" | "No" | "NO":
        return main()
        break
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
  reference_user_input_and_process()
  show_results()
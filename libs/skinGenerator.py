from libs.skinLibrary import get_skin_reference_input, generate_skin_code
import random

def reference_user_input_and_process():
  global length, skin_reference_by_user_input
  try:
    length = int(input("\nSet the length characters of skin code as you like: "))
    if length < 1:
      print("Length must bigger than 0")
      return
    
    while True:
      skin_reference_by_user_input = get_skin_reference_input()
      if len(skin_reference_by_user_input) > length:
        print(f"\nYour skin code more than {length}");
      else : break
  except ValueError:
    raise ValueError

def show_results():
  while True:
    skin_code_generate_result = generate_skin_code(length, skin_reference_by_user_input)
    print(f"\nGenerate result: {skin_code_generate_result}")
    generate_again = input("Generate again? [y/n] ")
    match generate_again:
      case "y" | "yes" | "Y" | "Yes" | "YES": return show_results()
      case _: break

if __name__ == '__main__':
  reference_user_input_and_process()
  show_results()
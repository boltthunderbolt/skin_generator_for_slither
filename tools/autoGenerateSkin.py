from libs import skinLibrary
import random

def start():
  global length
  length = int(input("\nSet the length characters of skin code as you like: "))
  if length < 1:
    print("Length must bigger than 0")
    return start()
  
def show_results():
  auto_generate_result = auto_generate_skin_process(length)
  print(f"Generate Result : {auto_generate_result}")


def auto_generate_skin_process(length):
  # Get characters from tools/skinLibrary
  skin_code_characters = [skinLibrary.skin_code_list[0][0]]

  # Generate random skin
  while skin_code_characters == length:
    length = random.choice(skin_code_characters)

  # Generate x2
  length = ''.join(random.sample(skin_code_characters, len(skin_code_characters)))
  return length
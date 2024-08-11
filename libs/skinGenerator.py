from libs import skinLibrary
import random
skin_code = skinLibrary.skin_code_list

def show_skin_list():
  for number, show_list in enumerate(skin_code, start = 1):
    print(f"{number}. {show_list[0].capitalize}");

def user_input():
  pass

if __name__ == '__main__':
  show_skin_list()
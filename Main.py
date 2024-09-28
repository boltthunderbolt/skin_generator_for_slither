from time import sleep
from tools import autoGenerateSkin, customSelectionSkin, customSkinGenerator, countriesSkin, gradationSkin
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def main():
  menu()

def menu():
  generator_option = ["auto generator skin", "custom skin generator", "countries skin", "custom skin selection", "gradation skin generator" ,"exit program"]
  print()
  print("Select your generator!\n======================")
  for option, list_option in enumerate(generator_option, start = 1):
    print(f"{option}. {list_option.capitalize()}")
  print()

  while True:
    try:
      generator_option_selected = int(input("\nSelect your generator by number: "))
      if 1 < generator_option_selected > len(generator_option):
        print(f"Select from 1 - {len(generator_option)}")
      else:
        generator_option_selected -= 1
        print(f"{generator_option[generator_option_selected].capitalize()} selected")
        break
    except ValueError:
      print("Please select by number")


  match generator_option_selected:
    case 0:
      autoGenerateSkin.start()
      autoGenerateSkin.show_results()
    case 1:
      customSkinGenerator.start()
      customSkinGenerator.show_results()
    case 2:
      countriesSkin.start()
    case 3:
      customSelectionSkin.start()
    case 4:
      gradationSkin.start()
    case 5:
      menu_program = input("\nAre you sure want to exit? [y / n] : ")
      while True:
        match menu_program:
          case "y" | "yes" | "Y" | "Yes" | "YES":
            sleep(3)
            print(CLEAR)
            print(f"{CLEAR_AND_RETURN} Program stopped")
            break
          case _:
            print('\n' * 100);
            return main()

if __name__ == '__main__':
  main()
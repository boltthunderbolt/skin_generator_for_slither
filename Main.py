from time import sleep
from tools import autoGenerateSkin, customSkinGenerator

def main():
  menu()

def menu():
  generator_option = ["auto generator skin", "custom generator skin", "exit program"]
  print()
  print("Select your generator!\n======================")
  for option, list_option in enumerate(generator_option, start = 1):
    print(f"{option}. {list_option.capitalize()}")
  print()

  while True:
    try:
      generator_option_selected = int(input("\nSelect your generator by number: "))
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
      menu_program = input("\nAre you sure want to exit? [y / n] : ")
      while True:
        match menu_program:
          case "y" | "yes" | "Y" | "Yes" | "YES":
            sleep(3)
            print('\n' * 100, "Program stopped")
            break
          case _:
            print('\n' * 100);
            return main()

if __name__ == '__main__':
  main()
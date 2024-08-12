from libs import skinGenerator, skinLibrary
from time import sleep

def main():
  skinLibrary.show_skin_list()
  skinGenerator.reference_user_input_and_process()
  skinGenerator.show_results()
  menu()

def menu():
  menu_program = input("\nWant to generate another password? [y / n] : ")
  while True:
    match menu_program:
      case "y" | "yes" | "Y" | "Yes" | "YES":
        print('\n' * 100);
        return main()
      case "n" | "no" | "N" | "No" | "NO":
        sleep(3)
        print('\n' * 100, "Program stopped")
        break
      case _:
        return menu()

if __name__ == '__main__':
  main()
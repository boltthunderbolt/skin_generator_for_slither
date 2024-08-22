import Main


def start():
  gradation_skin = [
    ["Green Fire", green_fire],
    ["Nuclear Type", nuclear_type],
    ["Rainbow Skin", rainbow_skin],
    ["New Year Fireworks", new_year_fireworks],
    ["Birthday Funfetti Cake", birthday_funfetti_cake],
    ["Birthday Ice Cream Cake", birthday_ice_cream_cake],
    ["Birthday Blue Velvet Cake", birthday_blue_velvet_cake],
    ["Green White", green_white],
    ["Yellow Brown", yellow_brown]
  ]
  gradation_skin.sort()

  print()
  for option, showList in enumerate(gradation_skin, start = 1):
    print(f"{option}. {showList[0].title()}")
  print()

  while True:
    try:
      user_input = int(input("\nChoose your snake skins: "))
      if 1 < user_input > len(gradation_skin):
        print(f"Choose from 1 - {len(gradation_skin)}")
      else:
        user_input -= 1
        print(f"{gradation_skin[user_input][0].title()} selected\n")
        gradation_skin[user_input][1]()
        while True:
          generate_again = input("\nWant to generate again? [enter / n]: ")
          match generate_again:
            case "n" | "no" | "N" | "No" | "NO":
              print(Main.CLEAR, Main.CLEAR_AND_RETURN);
              Main.menu()
              break
            case _:
              start()
              break
        break
    except ValueError:
      print(f"Please select by number!");

# ======================================================================================

def green_fire():
  print("pvohfs3333333pfp3333333sfhov")

def nuclear_type():
  print("pppvttvpppvcuxxucv")

def rainbow_skin():
  print("zzzzzzzzzzzzxzxzxxxxzxzxxxxzxxxxxxxxxzxxxxzzzxxxxxxxxxxcxcxcccccccxccccxxxcccxcxccccccccccccccxcxcxcccccccvcvcvvvvvccvcvcvvvvvvvvvvvvvvvvbvbbbvbbbbbbbbbbbbbbbbbnbnbnnnnnnnnnnnnnnnmnmmmmnmmnnnmmnnnnnnnnnnnmnmmmmm,m,m,,,mmmm,,m,mmm,,,,,,,,,,,,,,,,,,,,,"[::-1])

def new_year_fireworks():
  print("sbsbgmzddxd0jlretbsdtflrbsdtflrbsddtflre4336de444ed633sddxk0jlrettfbsdrttfbsdrtftbsdtfrelj0kxdd336dr444rd633sdrt36sdr36sdr36sdr36sdrt36sdrt36sdrt36sdrt36sdrt36sdr36sdr36sdrt336dr444rd633sddxk0jlrettfbsdrttfbsdrtftbsdttfrelj0kxdd336dr444rd633")

def birthday_funfetti_cake():
  print("bwbsvcuxdsusqszscsdxucssbwbsuxszaqsswgsszaqsuxssbwbbsvcuxd6678a8766ducvssbw678a2a876wbssvcuxd6678a8766duccdssvsvbsdxuszaqsswgsszaqsuxdsbvsvssducud6678a8766ducvssbw678a2a876wbssvcuxd6678a8766dxucvsbwbssuxszaqsswgsszaqsuxsssb")

def birthday_ice_cream_cake():
  print("smzdszuzgzmzczxsdxzwsswz88z88zwsswzxdxzmsbscxzxcsbsmzxdxzwsswz788z887zwsswzxdxcsswmzszmwbsscxdxz6788qzq8876dxzmzxdcssswmzdssdzmwbssscdxzmzxd6788qzq8876zxdxcsswmzszmwbsscxdxzwsswz788z887zwsswzxdxzmsbscxzxcsbsmzxdxzwsswz88z88zws")

def birthday_blue_velvet_cake():
  print("sbsdxzxujzszjuucbssdxzljdjlzxdssbcudxjlzd44jxj44dzljxducbssdxucuxjlzszljxucuxdssbxjld44jxj44dljxbssdzxjl44bsdjljdsb44ljzxzjdxjljxdjlzxzjl44bsdjljdsb44ljxzdssbxjld44jxj44dljxbssdxucuxjlzszljxucuxdssbcudxjlzd44jxj44dzljxducbssdxzljdjlzxdssbcudxjlzv")

def green_white():
  print("ihiihhihhhhhhhhohoohhoohohhooohooovooohvovvoooovvhohovvvovvovovvvvovvvvvsvvvsvosvvsvsvvvosvvvvvvvsvssvsvvvvsvssssssssssssssssvsvvvvsvssvsvvvvvvvsovvvsvsvvsovsvvvsvvvvvovvvvovovvovvvohohvvoooovvovhooovooohooohhohoohhoohohhhhhhhhihhiihi")

def yellow_brown():
  print("wgnmmngw")
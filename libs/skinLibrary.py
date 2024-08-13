skin_code_list = [
  ["glassy light red", '1'],
  ["dark red", '2'],
  ["glassy gray", '3'],
  ["glassy blue", '4'],
  ["glassy red", '5'],
  ["glassy yellow", '6'],
  ["glassy brown", '7'],
  ["glassy pink", '8'],
  ["glassy green", '9'],
  ["dark skylish blue", '0'],
  ["dark purple", '-'],
  ["light purple", 'q'],
  ["yellow", 'w'],
  ["dark blue with 5 stars", 'e'],
  ["dark blue with 4 stars", 'r'],
  ["super dark purple blueish", 't'],
  ["dark orange", 'y'],
  ["sky blue", 'u'],
  ["slug color", 'i'],
  ["dark green", 'o'],
  ["glassy light green", 'p'],
  ["pink", 'a'],
  ["white", 's'],
  ["light blue with stars", 'd'],
  ["black", 'f'],
  ["golden", 'g'],
  ["dark green", 'h'],
  ["light dark blue", 'j'],
  ["a bit dark blue", 'k'],
  ["dark blue", 'l'],
  ["regular purple", 'z'],
  ["blue", 'x'],
  ["light blue", 'c'],
  ["green", 'v'],
  ["light yellow", 'b'],
  ["brown", 'n'],
  ["light pink", 'm'],
  ["red", ',']
]

def show_skin_list():
  print("CODE|\tSKIN COLOR")
  print("----|-----------------")
  for show_list in skin_code_list:
    print(f"({show_list[1]}) | {show_list[0].capitalize()}");
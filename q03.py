from pkg.modu import read_json,print_json,process_data,write_json

MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'
Menu_dict = read_json(MENU_FILE)
print_json(Menu_dict)
discount = input("請輸入折扣率(0.0 ~ 1.0):")
processed_menu = process_data(Menu_dict, discount)
write_json(processed_menu, OUTPUT_FILE)
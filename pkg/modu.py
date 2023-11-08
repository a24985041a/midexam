import json

def triangle_zhonxin(a:tuple,b:tuple,c:tuple) -> tuple:
    x=int(round(float((int(a[0])+int(b[0])+int(c[0]))/3),0))
    y=int(round(float((int(a[1])+int(b[1])+int(c[1]))/3),0))
    """return abc zhonxin"""
    return x,y

def read_json(MENU_FILE:str) -> dict:
    with open(MENU_FILE,'r',encoding="UTF-8") as f:
        Menu_dict = json.load(f)
    return Menu_dict

def print_json(Menu_dict:dict) -> str:
    newmenustr = json.dumps(Menu_dict,indent = 4,ensure_ascii = False)
    print(newmenustr)

def process_data(Menu_dict: dict, discount: float) -> dict:
    for category in Menu_dict["categories"]:
        for item in category["items"]:
            item["price"] = int(round(float(item["price"]) * float(discount)))
    newmenustr = json.dumps(Menu_dict,indent = 4,ensure_ascii = False)
    print(newmenustr)
    return Menu_dict
    
def write_json(Menu_dict: dict,OUTPUT_FILE:str) -> None:
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
        json.dump(Menu_dict, f, ensure_ascii=False, indent=4)
    return 
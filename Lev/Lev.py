import os.path, json
path = "C:/Users/re-in/source/repos/Lev/Lev/data.json"	
def check():
    os.path.isfile(path)
    result = bool
    if os.path.isfile(path):
        print("file exist")
        result = "1"
        return result
    else:
        print("file not exist, creating...")
        open("data.json", "w+")
        result = "2"
    return result

def create():
        model = input('Type model name: ')
        serial_number = input('Type serial number: ')
        #exec branchs and give chouse
        
        with open('data.json', encoding='utf8') as f:
            data = json.load(f)
            formatted_obj = json.dumps(data['branch'], indent=4, separators=(',', ': '))
            print(formatted_obj)

        net_link = input('Type net_link: ')
        brech = input('Type brech: ')
        new_data = { "model": model, "serial_number": serial_number, "net_link": net_link, "brench": brech }

        with open('data.json', encoding='utf8') as f:
            data = json.load(f)
            data['objects'].append(new_data)

        with open("data.json", "w", encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

        print("Success create object")


def find():
    type_request = input("Net link - 1 / Serial number - 2: ")
    if type_request == "1":
        net_link = input("Type net link: ")
        with open('data.json', encoding='utf8') as f:
            data = json.load(f)
        #print(data['objects']['net_link'])
        for y in data['objects']:
            if y.get('net_link') == net_link:
                print(y)
    else:
        serial_number = input("Type serial number: ")
        with open('data.json', encoding='utf8') as f:
            data = json.load(f)
        #print(data['objects']['net_link'])
        for y in data['objects']:
            if y.get('serial_number') == serial_number:
                print(y)
    

def get_all():
    with open('data.json', 'r', encoding='utf8') as j:
        json_data = json.load(j)
        formatted_obj = json.dumps(json_data, indent=4, separators=(',', ': '))
        print("Success get objects")
        print(formatted_obj)

def start():
    check()
    print("What need?")
    selected = input('Get All - 1 or Create - 2 or Find - 3: ')
    if selected == "1":
        get_all()
    elif selected == "2":
        create()
    else:
        find()

start()
while True:
    flag = input('Again? [Y/n]: ')

    if flag == 'Y':
        start()
    elif flag == 'y':
        start()
    else:
        break
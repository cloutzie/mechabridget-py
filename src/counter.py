import json

def addr(cmd):
    with open('cmdcounter.json', 'r') as f:
        json_data = json.load(f)

    json_data[cmd]['runs'] += 1

    with open('cmdcounter.json', 'w') as f:
        json.dump(json_data, f, indent=4)


def resetcounter():
    with open('cmdcounter.json', 'r') as f:
        json_data = json.load(f)

    for i in json_data:
        json_data[i]['runs'] = 0

    with open('cmdcounter.json', 'w') as f:
        json.dump(json_data, f, indent=4)


def display():
    string=""

    with open('cmdcounter.json', 'r') as f:
        json_data = json.load(f)
    
    for i in json_data:
        string += f"{i} has been used {json_data[i]['runs']} times!\n"
    return string


# resetcounter()
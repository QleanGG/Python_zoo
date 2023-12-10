import json

def save_data(my_data_file,my_zoo):
    json_string = json.dumps(my_zoo)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)

def load_data(my_data_file , my_zoo):# load a list from a file
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
        my_zoo = json.loads(json_string)
        if my_zoo == None:
            return []
        return my_zoo
    except: return my_zoo
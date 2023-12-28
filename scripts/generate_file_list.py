import os
import json

def create_file_list(folder_path):
    # Get the list of items in the current folder
    items = os.listdir(folder_path)

    # Create an array list from the items
    item_list = [item for item in items]

    # Save the array list to a JSON file
    with open('file_list.json', 'w') as json_file:
        json.dump(item_list, json_file)

# Specify the current folder path
current_folder_path = '.'

# Call the function with the folder path
create_file_list(current_folder_path)

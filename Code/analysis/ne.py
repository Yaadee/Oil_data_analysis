import os

def generate_project_tree(directory, indent=''):
    print(indent + os.path.basename(directory) + '/')
    indent += '    '
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            generate_project_tree(item_path, indent)
        else:
            print(indent + item)

# Example usage:
project_directory = '/Desktop/Oil_Price_Impact '

generate_project_tree(project_directory)

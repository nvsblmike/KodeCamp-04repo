import os
import subprocess

# Define users and their groups
users = {
    'Andrew': 'System Administrator',
    'Julius': 'Legal',
    'Chizi': 'Human Resource Manager',
    'Jeniffer': 'Sales Manager',
    'Adeola': 'Business Strategist',
    'Bach': 'CEO',
    'Gozie': 'IT intern',
    'Ogochukwu': 'Finance Manager'
}

# Define company directories
directories = [
    'Finance Budgets',
    'Contract Documents',
    'Business Projections',
    'Business Models',
    'Employee Data',
    'Company Vision and Mission Statement',
    'Server Configuration Script'
]

def create_user(username, group):
    try:
        subprocess.run(['sudo', 'groupadd', group], check=True)
    except subprocess.CalledProcessError:
        print(f"Group {group} already exists.")
    try:
        subprocess.run(['sudo', 'useradd', '-m', '-G', group, username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

def create_directory(directory):
    path = os.path.join('/path/to/company/documents', directory)  # Specify the base path
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}")

def main():
    # Create users and assign them to groups
    for username, group in users.items():
        create_user(username, group)

    # Create directories
    for directory in directories:
        create_directory(directory)

    # User input for creating a file
    file_name = input("Enter the name of the file: ")
    dir_name = input("Enter the directory to create the file in: ")

    if dir_name in directories:
        create_file(file_name, dir_name)
    else:
        print("Invalid directory name.")

def create_file(file_name, directory):
    base_path = '/path/to/company/documents'  # Specify the base path
    path = os.path.join(base_path, directory, file_name)
    try:
        with open(path, 'w') as f:
            f.write("")  # Create an empty file
        print(f"File {file_name} created in {directory} directory.")
    except OSError as e:
        print(f"Error creating file {file_name}: {e}")

if _name_ == '_main_':
    main()
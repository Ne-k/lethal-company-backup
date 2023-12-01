import json
import shutil
import os
import time


def backup_save_data(save_data_path, backup_folder_path):
    shutil.copytree(save_data_path, backup_folder_path, dirs_exist_ok=True)


def restore_save_data(save_data_path, backup_folder_path):
    if not os.path.exists(backup_folder_path):
        print('Error: No backup found to restore.')
        return

    shutil.rmtree(save_data_path)

    shutil.copytree(backup_folder_path, save_data_path)


def main():
    config_file_path = 'config.json'
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}

    if 'save_data_path' not in config:
        config['save_data_path'] = input('Enter the full path to the save game data (usually located at ' + '\033[94m\AppData\LocalLow\ZeekerssRBLX\Lethal Company)\033[0m:')
    if 'backup_folder_path' not in config:
        config['backup_folder_path'] = input('Enter the full path to a folder you want to backup the save data '
                                             'contents to:')

    with open(config_file_path, 'w') as f:
        json.dump(config, f, indent=4)

    action = input('Do you want to (b)ackup or (r)estore? ')
    if action.lower() == 'b':
        backup_save_data(config['save_data_path'], config['backup_folder_path'])
        print("Save data saved!")
        time.sleep(5)
    elif action.lower() == 'r':
        restore_save_data(config['save_data_path'], config['backup_folder_path'])
        print("Backup Restored!")
        time.sleep(5)
    else:
        print('Invalid option. Please enter either "b" for backup or "r" for restore.')
        time.sleep(5)


if __name__ == "__main__":
    main()

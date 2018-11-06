import os, shutil

FILE_TO_COPY = 'main.exe' # change later to antivirus

def find_folder(folder_name, startpath):
    results = []

    for root, _, _ in os.walk(startpath):
        base_root = os.path.basename(root)
        if folder_name == base_root.lower():
            results.append(root)

    return results

def add_to_startup(startup_path='C:\\Users\\DePauw\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'):
    try:
        shutil.copy(os.path.join(os.getcwd(), FILE_TO_COPY),
            os.path.join(startup_path, FILE_TO_COPY))
    except Exception as e:
        print('An exception occured.')
        print(e)

if __name__ == '__main__':
    #print(find_folder('python', 'C:\\Users\\DePauw\\Documents\\'))
    #startup_paths = find_folder('startup', 'C:\\')
    #print(startup_paths)

    add_to_startup()

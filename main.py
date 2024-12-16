from vars import get_variables
import dropbox
import os

DEFAULT_PATH = "/"
DROPBOX_TOKEN = ""
DOWNLOAD_PATH = ""

def init():
    if os.path.exists('.env'):
        return get_variables()

    print("To get started, please enter your Dropbox API key:")
    key = input()
    print("\nPlease enter the path where you would like to download files to:")
    path = input()

    with open('.env', 'w') as f:
        f.write(f'DROPBOX_TOKEN = "{key}"\n')
        f.write(f'DOWNLOAD_PATH = "{path}"')

    print("\nYour Dropbox API key and download path have been saved successfully! You will not have to enter these again")
    print("These values can be found in file .env and edited from there in future.")

    return get_variables()

def setup_dropbox():
    return dropbox.Dropbox(DROPBOX_TOKEN)

def validate_input(inp, entries):
    return (inp.isdigit() and (int(inp) <= len(entries))) or any([entry.name == inp for entry in entries]) or (inp == "..") or (inp == "exit")

def get_temp_link(dbx, path):
    try:
        return dbx.files_get_temporary_link(path)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

def main():
    print('*------------------ Welcome to Python Dropbox Explorer ------------------*')
    global DROPBOX_TOKEN, DOWNLOAD_PATH
    DROPBOX_TOKEN, DOWNLOAD_PATH = init()
    dbx = setup_dropbox()

    curr_path = ""
    while True:
        print(f"\nCurrent path: {curr_path or DEFAULT_PATH}")
        print("\n=------------------ Files / Folders ------------------=")

        entries = dbx.files_list_folder(curr_path).entries
        
        for i, entry in enumerate(entries):
            print(f"{i+1}: {entry.name}") if not isinstance(entry, dropbox.files.FolderMetadata) else print(f"{i+1}: {entry.name}/")

        print("\n=------------------ Options ------------------=")
        print("To open a folder, type in the name or number")
        print("To download a file, type in the name or number")
        print("To go back a level, type '..'")
        print("To exit, type 'exit'")

        valid_inp = False
        while not valid_inp:
            inp = input("\n")
            valid_inp = validate_input(inp, entries)
            if not valid_inp:
                print("Invalid input. Please try again.")

        if inp == "exit":
            break

        if inp == "..":
            curr_path = "/".join(curr_path.split("/")[:-1])
            continue

        if inp.isdigit() and (int(inp) <= len(entries)):
            inp = int(inp) - 1
            inp = entries[inp].name

        path = f"{curr_path}/{inp}" if curr_path != "" else f"{DEFAULT_PATH}{inp}"

        if isinstance(dbx.files_get_metadata(path), dropbox.files.FolderMetadata):
            curr_path = path
            continue

        try:
            _, res = dbx.files_download(path)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("The file could not be downloaded.")
            link = get_temp_link(dbx, path)
            print(f"Temporary link: {link.link}") if link else print("Temporary link could not be generated.")
            continue
        with open(f"{DOWNLOAD_PATH}/{inp}", "wb") as f:
            f.write(res.content)
        print(f"\nFile {inp} has been downloaded successfully!")

if __name__ == "__main__":
    main()


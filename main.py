from vars import DOWNLOAD_PATH, DROPBOX_TOKEN
import dropbox

DEFAULT_PATH = "/"

def setup_dropbox():
    if not DROPBOX_TOKEN:
        print("To get started, please enter your Dropbox API key:")
        key = input()

        with open('.env', 'x') as f:
            f.write(f"DROPBOX_TOKEN={key}")
            print("Your Dropbox API key has been saved successfully! You will not have to enter this again")
            print("Your token can be found in .env and edited from there in future.")

    if not DOWNLOAD_PATH:
        print("Please enter the path where you would like to download files to:")
        path = input()

        with open('.env', 'x') as f:
            f.write(f"DOWNLOAD_PATH={path}")
            print("Your download path has been saved successfully! You will not have to enter this again")
            print("Your path can be found in .env and edited from there in future.")
    
    return dropbox.Dropbox(DROPBOX_TOKEN or key)

def main():
    print('*------------------ Welcome to Python Dropbox Explorer ------------------*')
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
        print("To exit, type in 'exit'")
        print("To go back a level, type '..'")

        inp = input("\n")

        if inp == "exit":
            break

        if inp == "..":
            curr_path = "/".join(curr_path.split("/")[:-1])
            continue

        if inp.isdigit():
            inp = int(inp) - 1
            if inp >= len(entries):
                print("Invalid input. Please try again.")
                continue
            inp = entries[inp].name

        path = f"{curr_path}/{inp}" if curr_path != "" else f"{DEFAULT_PATH}{inp}"

        if not any([entry.name == inp for entry in dbx.files_list_folder(curr_path).entries]):
            print("Invalid input. Please try again.")
            continue

        if isinstance(dbx.files_get_metadata(path), dropbox.files.FolderMetadata):
            curr_path = path
            continue

        _, res = dbx.files_download(path)
        with open(f"{DOWNLOAD_PATH}/{inp}", "wb") as f:
            f.write(res.content)
        print(f"\nFile {inp} has been downloaded successfully!")

if __name__ == "__main__":
    main()

import os
import threading

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path}: \n{content}\n")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        
def read_main():
    directory = r"C:\Users\DELL\github-classroom\PUP-BSIT\individual-playground-ynion-mabeamae\File-handling"
    
    threads = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            thread = threading.Thread(target=read_file, args=[file_path])
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()
        
read_main()
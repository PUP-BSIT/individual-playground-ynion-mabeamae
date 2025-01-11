import os
import threading
from collections import defaultdict

word_count = defaultdict(int)
lock = threading.Lock()

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()  
            local_count = defaultdict(int)

            for word in words:
                local_count[word] += 1

            with lock:
                for word, count in local_count.items():
                    word_count[word] += count

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def count_words():
    directory = r'C:\Users\DELL\github-classroom\PUP-BSIT\individual-playground-ynion-mabeamae\File-handling'  

    threads = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  
            file_path = os.path.join(directory, filename)
            thread = threading.Thread(target=count_words_in_file, 
                                      args=(file_path,))
            threads.append(thread)
            thread.start() 

    for thread in threads:
        thread.join()

    print("Word Frequency Count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

count_words()

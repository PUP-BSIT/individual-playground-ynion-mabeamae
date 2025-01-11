import threading
import os
import csv

def process_csv(file_name, processed_data):
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader) 
        for row in reader:
            processed_data.append(row)

def process_csv_files_with_threads(file_names, output_file):
    processed_data = []
    threads = []
    
    lock = threading.Lock()

    def thread_task(file_name):
        temp_data = []
        process_csv(file_name, temp_data)
        with lock:
            processed_data.extend(temp_data)

    for file_name in file_names:
        thread = threading.Thread(target=thread_task, args=(file_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if processed_data:
        with open(output_file, "w", newline="") as csv_output:
            writer = csv.writer(csv_output)
            writer.writerow(["Column1", "Column2", "Column3"])  
            writer.writerows(processed_data)

csv_file_names = ["file1.csv", "file2.csv", "file3.csv"]
output_csv_file = "combined_output.csv"

def create_sample_csv(file_name, rows):
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Column1", "Column2", "Column3"])
        for i in range(rows):
            writer.writerow([f"Data{i+1}_1", f"Data{i+1}_2", f"Data{i+1}_3"])

for i, file_name in enumerate(csv_file_names):
    create_sample_csv(file_name, 10 * (i + 1)) 

process_csv_files_with_threads(csv_file_names, output_csv_file)

print(f"Combined data has been written to {output_csv_file}.")

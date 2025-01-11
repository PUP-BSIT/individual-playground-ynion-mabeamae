import threading
import time
import random

def create_log_file(filename, num_entries=100):
    log_levels = ['INFO', 'WARNING', 'ERROR']
    with open(filename, 'w') as f:
        for i in range(num_entries):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_level = random.choice(log_levels)
            message = f"This is a {log_level} message number {i+1}"
            f.write(f"{timestamp} {log_level} {message}\n")

def extract_error_logs(filename, start_line, end_line, result, lock):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if start_line <= i < end_line:
                if "ERROR" in line:
                    with lock:
                        result.append(line.strip())

def process_logs(filename, num_threads=4):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    lines_per_thread = total_lines // num_threads
    threads = []
    result = []
    lock = threading.Lock()

    for i in range(num_threads):
        start_line = i * lines_per_thread
        end_line = (i + 1) * lines_per_thread if i < num_threads - 1 else total_lines
        thread = threading.Thread(target=extract_error_logs, args=(filename, 
                                            start_line, end_line, result, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

log_filename = "logfile.txt"
create_log_file(log_filename)

error_logs = process_logs(log_filename)

print("Extracted ERROR logs:")
for log in error_logs:
    print(log)
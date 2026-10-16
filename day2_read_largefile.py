import os
import psutil # Optional library to check RAM usage

def read_logs_lazily(file_path):
    """Yields lines one by one without caching them in RAM."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line

# 1. Process the 50MB file line by line
error_count = 0
for log_entry in read_logs_lazily("large_sample_log.txt"):
    if "[ERROR]" in log_entry:
        error_count += 1

print(f"Scan complete! Found {error_count:,} errors in the file.")

# 2. Verify memory safety
process = psutil.Process(os.getpid())
print(f"Current script RAM footprint: {process.memory_info().rss / (1024 * 1024):.2f} MB")

# TODO: The yield keyword is used to create generator functions which produce a sequence of values lazily, 
#       one at a time, instead of returning them all at once.
#       The yield temporarily pauses the function, saves its entire state, and outputs a value. 
#       When the generator is called again, it resumes execution immediately after the last yield statement.
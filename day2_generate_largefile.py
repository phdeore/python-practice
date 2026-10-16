import random
import time

def generate_huge_log(filename="large_sample_log.txt", target_size_mb=50):
    levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "User logged in successfully.",
        "Database connection timeout. Retrying...",
        "Failed to upload image asset.",
        "API request processed in 45ms.",
        "Disk space running low on volume /dev/sda1.",
        "Cache cleared for session tokens."
    ]
    
    # Calculate bytes (1 MB = 1,024 * 1,024 bytes)
    target_bytes = target_size_mb * 1024 * 1024
    bytes_written = 0
    
    print(f"Generating a {target_size_mb}MB log file...")
    
    with open(filename, "w", encoding="utf-8") as f:
        while bytes_written < target_bytes:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(levels)
            msg = random.choice(messages)
            
            # Construct a realistic log line
            log_line = f"[{timestamp}] [{level}] {msg}\n"
            f.write(log_line)
            
            # Keep track of file size
            bytes_written += len(log_line.encode("utf-8"))
            
    print(f"Success! Created '{filename}' ({bytes_written / (1024*1024):.2f} MB)")

# Run the generator
generate_huge_log()

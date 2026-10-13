from collections import Counter
import re

def extract_device_log(filePath):
    error_pattern = re.compile(r"ERROR\s+\[(.*?)\]")
    error_counter = Counter()
    with open(filePath,"r", encoding = "utf-8") as file:
        
        for line in file:
            match = error_pattern.search(line)
            if match:
                error_message = match.group(1)
                error_counter[error_message] += 1
        return error_counter

print(extract_device_log("/Users/aditi/Desktop/log.rtf"))

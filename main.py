import os
import hashlib

#Validate files
def scanDirectory(directory):
    if os.path.exists(directory):
        print(f"This directory ' {directory}' exists")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Skip hidden or system files like desktop.ini
                if file.lower() in ['desktop.ini', '$recycle.bin', 'thumbs.db']:
                    continue
                hash = calculate_hash(file_path)
                print(f"File:   {file_path} | Hash:  {hash}")
    else:
        print(f"This directory '" + directory + "' does not exist! Skipping directory...")

#Calculate file hash
def calculate_hash(filename):
    sha256 = hashlib.sha256()  # Create a sha256 hash object
    try:   
        with open(filename, 'rb') as f:  # Open file in binary read mode
            while chunk := f.read(8192):  # Read the file in chunks
                sha256.update(chunk)  # Update the hash with the chunk of data
    except Exception as e:
        print(f"Error processing the file {filename}: {e}")
        return None
    
    return sha256.hexdigest()  # Return the final hash as a hexadecimal string

    

def main():
    directoriesToScan = r"C:\Program Files (x86)"
    scanDirectory(directoriesToScan)

if __name__ == "__main__":
    main()
    
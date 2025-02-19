import os
import hashlib
import requests
import json
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#Get the API Key from environmentvariables
api_key = os.getenv("VIRUSTOTAL_API")

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
                scanMalware(hash)
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

#Scan for malware
def scanMalware(dbHashes):
    virus_count = 0
    flags = []

    for dbHash in dbHashes:
        url = f"https://www.virustotal.com/api/v3/files/{dbHash}"
        headers = {'accept': 'application/json', 'x-apikey': api_key}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:

                #Extract only the needed data
                data = response.json()

                #Retrieve data, Id, attributes
                file_info = data['data']

                # Get the results from the analysis
                analysis_results = file_info['attributes']['last_analysis_results']

                # Check if any engine flagged the file as malicious
                flagged_engines = [engine for engine, result in analysis_results.items() if result['category'] == 'malicious']

                if flagged_engines:
                    flags.append(flagged_engines)
                    virus_count+=1

        except Exception as e:
            print(f"Error during API request: {e}")

def main():
    directoriesToScan = r"C:\Program Files (x86)"
    scanDirectory(directoriesToScan)

if __name__ == "__main__":
    main()
    
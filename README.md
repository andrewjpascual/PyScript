# PyScript
My personal Python scripts and projects

### 2/10/25
The changes on this branch includes the initial build of the security script within main.py

### 2/11/25
Introduce checks on specific Window directories to identify potential vulnerabilities

### 2/12/25
Continue checks from yesterday

### 2/17/25 Changes
Updated Directory to Scan
- Removed my local directory and replaced with the Program File x86 path

Added Hashing for Files
- First validate the x86 path
- Within each file in this path, generate a SHA256 hash
- With the generated hash, output this along with the file
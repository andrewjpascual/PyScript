import os

#Specify path
path1 = r'C:\Users\andre\OneDrive\Desktop'
if os.path.exists(path1):
    print ("This directory " +path1+  " exists")
else:
    print ("This directory " +path1+ " does not exist! Skipping directory...")
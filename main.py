import os

#Specify path
path1 = r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols'
if os.path.exists(path1):
    print ("This directory " +path1+  " exists")
else:
    print ("This directory " +path1+ " does not exist! Skipping directory....")
import uuid
import os
# import exiftool
import xml.etree.ElementTree as ET
import subprocess

exiftool = "/opt/homebrew/bin/exiftool"
path = "../Pictures"
files = os.listdir(path)

code = ""
out = ""
err = ""

totalfiles = len(files)

def run(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

for i in range(len(files)):

    print("- [" + str(i) +  "/" + str(totalfiles) + "] - Creating XML metadata for file: " + files[i] )

    # Save UUID to RAW Filename EXIF tag
    xml = ""
    try:
        code, out, err = run(["/opt/homebrew/bin/exiftool", "-X", path+"/"+files[i]])
    except:
        print("Cannot create XML for file: "+files[i])
        exit

    output = "{}".format(out)
    output =  "<"+output.strip("b\"")
    file = open("./output/"+files[i]+".xml", 'w')
    file.write(output[2:].replace("\\n", "\n"))
    file.close()
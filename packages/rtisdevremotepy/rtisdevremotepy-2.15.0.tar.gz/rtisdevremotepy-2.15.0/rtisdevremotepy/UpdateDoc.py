from shutil import copyfile
import os

rtisdevFile = "C:\\Users\\woute\\Projects\\rtisdev\\rtisdev\\rtisdev.py"
copyfile('RTISDevRemotePy.py', 'RTISDevRemotePy2.py')

fileROG = open(rtisdevFile, 'r')
LinesOG = fileROG.readlines()
fileROG.close()

docs = {}
doc_started = False
public_code_started = False
method_started = False
methodName = ""
for index, line in enumerate(LinesOG):
    line = line.replace("import rtisdev", "import rtisdevremotepy")
    line = line.replace("settings : RTISSettings", "settings : RTISSettings object as dict")
    line = line.replace("measurement : RTISMeasurement", "measurement : RTISMeasurement object as dict")
    if "def open_connection(" in line:
        public_code_started = True
    if "def " in line and public_code_started and not method_started:
        method_started = True
        methodName = line.split("def ")[1].split("(")[0]
        docs[methodName] = []
    if public_code_started and method_started:
        if doc_started:
            docs[methodName].append(line)
            if "    \"\"\"" in line:
                doc_started = False
                method_started = False
        else:
            if "    \"\"\"" in line:
                doc_started = True
                docs[methodName].append(line)

fileR = open('RTISDevRemotePy2.py', 'r')
Lines = fileR.readlines()
fileR.close()

doc_started = False
public_code_started = False
method_started = False
methodName = ""
fileW = open('RTISDevRemotePy2.py', 'w')
for index, line in enumerate(Lines):
    if "def open_connection(" in line:
        public_code_started = True
    if "def " in line and public_code_started and not method_started:
        method_started = True
        methodName = line.split("def ")[1].split("(")[0]
    if public_code_started and method_started:
        if doc_started:
            if "    \"\"\"" in line:
                doc_started = False
                method_started = False
        else:
            if "    \"\"\"" in line:
                doc_started = True
                if methodName in docs:
                    for doc_line in docs[methodName]:
                        fileW.writelines("    " + doc_line)
        if not doc_started and "    \"\"\"" not in line:
            fileW.writelines(line)
    else:
        fileW.writelines(line)

fileW.close()


from datetime import datetime

filename = r"C:\Temp\python_project\hello.txt"
currenttime = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
content = "Hello World!" + " Github Timestamp is: " + currenttime
with open(filename, "a+") as f:
    f.writelines("\n" + content)
f.close()

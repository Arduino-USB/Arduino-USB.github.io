import time
import os
def retry():
    try:
        pass
        os.system("del ip.txt")
    except Exception as e:
        pass
    try:
        os.system("curl.exe -o ip.txt https://sockter-py.github.io/ip.txt")
    except Exception as e:
        time.sleep(300)
        retry()
retry()

with open('ip.txt', 'r') as c:
     ips = c.read()
     ips.strip()
print(ips)
with open("web.py", 'r') as e:
    script = e.read()


def startApp():
    os.system("python web.py")

os.system("del web.py")


nps = ips.replace("\n" , '')
with open("web.py", 'w') as e:
    ipscript = script.replace("ips", f"\"{nps}\"")
    e.write(ipscript)
startApp()

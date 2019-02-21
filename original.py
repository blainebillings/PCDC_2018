import os
import time

lines = os.popen('sudo cat /etc/shells').readlines()[1:]
possible_shells = []

for line in lines:
    while "/" in line:
   	 line = line[line.index("/") + 1:]
    possible_shells.append(line[:-1])

lines = os.popen('sudo ps aux').readlines()[1:]
beginning_shells = []

for line in lines:
    keep = False

    while " " in line:
   	 line = line[line.index(" ") + 1:]
   	 if " " in line:
   		 if line.index(" ") != 0 and not keep:
   			 pid = line[:line.index(" ")]
   			 keep = True

    line = line[:-1]
    if line in possible_shells:
   	 beginning_shells.append(pid)

reported_and_running = {}

while True:
    time.sleep(1)
    lines = os.popen('sudo ps aux').readlines()[1:]
    
    for x in reported_and_running.keys():
   	 reported_and_running[x] = False

    for line in lines:
   	 original = line
   	 keep = False

   	 while " " in line:
   		 line = line[line.index(" ") + 1:]
   		 if " " in line:
   			 if line.index(" ") != 0 and not keep:
   				 pid = line[:line.index(" ")]
   				 keep = True
    
   	 line = line[:-1]
   	 if line in possible_shells and pid not in beginning_shells and pid not in reported_and_running.keys():
   		 print("\nSHELL SPAWNED: shell = " + line + ", pid = " + pid)
   		 print(original)
   		 reported_and_running[pid] = True
   	 if line in possible_shells and pid not in beginning_shells and pid in reported_and_running.keys():
   		 reported_and_running[pid] = True

    for x in reported_and_running.keys():
   	 if reported_and_running[x] == False:
   		 reported_and_running.pop(x, None)
import os
import time

lines = os.popen('sudo service --status-all').readlines()
current = {}

for line in lines:
    sign = line[line.index("[") + 2]
    name = line[line.index("]") + 3:-1]
    current[name] = sign
    print(name + ": " + sign)

while True:
    time.sleep(1)
    lines = os.popen('sudo service --status-all').readlines()
    
    for line in lines:
   	 sign = line[line.index("[") + 2]
   	 name = line[line.index("]") + 3:-1]

   	 if name not in current.keys():
   		 print("Service Added! " + name + ":" + sign)
   		 current[name] = sign
   	 elif current[name] != sign:
   		 print("Service Status Changed! " + name + " now " + sign)
   		 current[name] = sign

    for line in current.keys():
   	 if line not in lines:
   		 print("Service Deleted! " + line[line.index("]") + 3:-1])

initial_passwd = []
initial_shadow = []

lines = os.popen('sudo cat /etc/passwd').readlines()

for line in lines:
    initial_passwd.append(line)

lines = os.popen('sudo cat /etc/shadow').readlines()

for line in lines:
    initial_shadow.append(line)

while True:
    time.sleep(1)
    lines = os.popen('sudo cat /etc/passwd').readlines()

    process = {}

    for line in lines:
   	 process[line] = False

    for line in initial_passwd:
   	 if line not in process.keys():
   		 print('Passwd Deletion: \n' + line)
   		 initial_passwd.remove(line)
   	 else:
   		 process[line] = True

    for line in process.keys():
   	 if process[line] is False:
   		 print('Passwd Addition: \n' + line)
   		 initial_passwd.append(line)

    lines = os.popen('sudo cat /etc/shadow').readlines()

    process = {}

    for line in lines:
   	 process[line] = False

    for line in initial_shadow:
   	 if line not in process.keys():
   		 print('Shadow Deletion: \n' + line)
   		 initial_shadow.remove(line)
   	 else:
   		 process[line] = True

    for line in process.keys():
   	 if process[line] is False:
   		 print('Shadow Addition: \n' + line)
   		 initial_shadow.append(line)

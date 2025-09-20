# connect.py
import paramiko

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
    
def run(self): # Connection via SSH. Run command / upload / download file
    try:
        key = paramiko.RSAKey.from_private_key_file(self.key_path) # Load SSH Key - Private
        
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, port=self.port, username=self.user, pkey=key)
        
        print(f"Connected to {self.host}")
        
        # Run Command when given
        if self.remote_command:
            stdin, stdout, stderr = ssh.exec_command(self.remote_command)
            print("Output:\n", stdout.read().decode())
            print("Errors:\n", stderr.read().decode())
            
        # File upload when provided
        if self.local_file and self.remote_path:
            sftp = ssh.open_sftp()
            sftp.put(self.local_file, self.remote.path)
            print(f"Uploaded {self.local_file} -> {self.remote_path}")
            sftp.close()
            
    except Exception as e:
        print(f"Connection failed: {e}")
    
    finally:
        if ssh:
            ssh.close()
            print("Connection Closed")
            
    ssh.close()
    
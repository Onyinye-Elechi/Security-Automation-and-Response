print("CSN Script for generating system report for an Ubuntu instance!\n")
import paramiko

host = "34.221.201.59"
username = "ubuntu"
key_filename = "csn-key.pem"

# commands = [
#     "ip addr",
#     "ls -l"
# ]

commands = [
    "top -bn1 | grep 'Swap'",
    "free -h",
    "df -h"
]


def ssh_connect(host, username, key_filename, commands):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, key_filename=key_filename)
    
    # stdin, stdout, stderr = client.exec_command("ip addr")
    # print("stdin", stdin)
    # print("stdout", stdout)
    # print("stderr", stderr)

    results = {}

    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode("utf-8").strip()
        results[command] = output
        # print(command, ">>", output)

    client.close()
    return results

results = ssh_connect(host, username, key_filename, commands)

print("CPU Usage:")
print(results[commands[0]], "\n")
print("Memory Usage:")
print(results[commands[1]], "\n")
print("Disk Usage")
print(results[commands[2]], "\n")

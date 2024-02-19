#!/usr/bin/python3
import os
import re
import sys

def create_user(username, gecos):
    print(f"==> Creating account for {username}...")
    cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
    os.system(cmd)

def set_password(username, password):
    print(f"==> Setting the password for {username}...")
    cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
    os.system(cmd)

def assign_to_group(username, group):
    if group != '-':
        print(f"==> Assigning {username} to the {group} group...")
        cmd = f"/usr/sbin/usermod -aG {group} {username}"
        os.system(cmd)

def main():
    for line in sys.stdin:
        match = re.match(r'^\s*#', line)
        if match:
            continue

        fields = line.strip().split(':')

        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = f"{fields[3]} {fields[2]},,,"

        groups = fields[4].split(',')

        create_user(username, gecos)
        set_password(username, password)

        for group in groups:
            assign_to_group(username, group)

if __name__ == '__main__':
    main()


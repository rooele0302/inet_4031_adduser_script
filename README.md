# inet_4031_adduser_script

## Description

This repository contains a Python script for creating users, setting passwords, and assigning them to groups. It's designed for use in an INET 4031 (Networking) course context.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/inet_4031_adduser_script.git
   cd inet_4031_adduser_script

1. Run the Script:
- Ensure you have Python 3 installed on your system.
- Create an input file named create-users.input with user details.
- Run the script with elevated privileges:
  sudo ./create-users.py < create-users.input

## Example Input
user01:password01:Last01:First01:group01
user02:password02:Last02:First02:group02

## Example Output
==> Creating account for user01...
==> Setting the password for user01...
==> Assigning user01 to the group01 group...
==> Creating account for user02...
==> Setting the password for user02...
==> Assigning user02 to the group02 group...





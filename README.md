# SICARIO - SSH Brute Force Script

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.x-green.svg)](https://www.python.org/)
![Developed on Kali](https://img.shields.io/badge/Developed%20on-Kali%20Linux-orange.svg)

Python script for performing SSH brute force attacks. It allows you to automate the process of attempting various username and password combinations to gain access to SSH servers.

![SSH Bruteforce](https://github.com/Sic4rio/ssh-bruteforce/blob/main/ssh-brute.png?raw=true)


## Features

- Rainbow-colored banner for a visually appealing interface.
- Asynchronous SSH brute force with progress tracking.
- Supports custom user and password lists.
- Saves successful combinations to a text file.

## Prerequisites

- Python 3.x
- paramiko
- tqdm
- colorama
- prompt_toolkit

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/your-username/sicario-ssh-bruteforce.git
   cd sicario-ssh-bruteforce
   ```
2. Install the required dependencies:

```
pip install paramiko tqdm colorama prompt_toolkit
```
3. Run the script:

```
python ssh.py
```
Follow the on-screen prompts to specify the user and password lists, target IP, and port.

Development

    This script was developed on Kali Linux.

License

This project is licensed under the MIT License - see the LICENSE file for details

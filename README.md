## Features
- **one-step installation**.
- saves a lot of time, **indeed a lot time!**.
- **extremely light-weight and not process intensive.**
- **legends** to help you understand which tests may take longer time, so you can `Ctrl+C` to skip if needed.


---
### FYI:
- _program is still under development._


## Description
HTBHound is a powerful Python-based tool designed to aid in the enumeration of subdomains, directories, and files for web machines on Hack The Box. With HTBHound, you can quickly scan and identify possible vulnerabilities on the target website, making it an essential tool for both ethical hackers and security researchers.

One of the most significant features of HTBHound is its ability to perform fast scans using threading processes. This feature means that HTBHound can enumerate subdomains and files and directories at an accelerated pace compared to other similar tools, making it ideal for time-sensitive tasks.

The tool also makes use of the well-known and trusted gobuster tool as a dependency, ensuring that the scans produced by HTBHound are accurate and reliable. By leveraging the strengths of gobuster, HTBHound can identify a wide range of hidden directories and files, including sensitive data that could be exploited by attackers.

HTBHound is easy to use, with a simple command-line interface that allows you to configure the scan parameters, such as the target URL and the wordlist to be used. It also provides detailed output.

With HTBHound, you can take your web application enumeration to the next level, allowing you to identify possible vulnerabilities and weaknesses that can be exploited by attackers. Whether you are a security researcher or an ethical hacker, HTBHound is an essential tool for your arsenal, helping you to identify potential attack vectors and secure your web applications.

In summary, HTBHound is a fast and reliable web application enumeration tool that is specifically designed for use on Hack The Box web machines. With its threading processes and dependency on gobuster, HTBHound can quickly identify hidden directories and files, making it an invaluable tool for security researchers and ethical hackers.


## Requirements
- **Python 3**
- Kali OS (_**Preferred**, as it is shipped with almost all the tools_).
- gobuster (sudo apt-get install gobuster).
- Tested with Parrot & Ubuntu Operating Systems.
Note: running setup.py will install gobuster for you automatically.


## Installation

you can install the `htbhound` python module with `pip`. This will create a link for `htbhound` in your PATH. 

```
git clone https://github.com/Danny-LLi/HTBHound.git
cd HTBHound
python3 setup.py install
```

## Usage 
 `htbhound 0 http://example.com`
 `htbhound 1 http://example.com`
 `htbhound 2 http://example.com` 



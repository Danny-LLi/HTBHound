#!/usr/bin/env python3
import os
import sys
import subprocess
import concurrent.futures
import argparse

def main():
    cwd = os.getcwd()
    #output_error = os.path.join(cwd, "errors.txt")
    dev_null = "/dev/null"
    s_output_files = os.path.join(cwd, "gobuster_s_files.txt")
    s_output_directories = os.path.join(cwd, "gobuster_s_directories.txt")
    s_output_subdomains = os.path.join(cwd, "gobuster_s_subdomains.txt")
    m_output_files = os.path.join(cwd, "gobuster_m_files.txt")
    m_output_directories = os.path.join(cwd, "gobuster_m_directories.txt")
    m_output_subdomains = os.path.join(cwd, "gobuster_m_subdomains.txt")
    w_output_files = os.path.join(cwd, "gobuster_w_files.txt")
    w_output_directories = os.path.join(cwd, "gobuster_w_directories.txt")
    w_output_subdomains = os.path.join(cwd, "gobuster_w_subdomains.txt")


    gobuster_dir_large_files = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-large-files.txt"
    gobuster_dir_large_dirs = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-large-directories.txt"
    gobuster_vhost_s = "gobuster vhost -u {} -w /usr/share/wordlists/htbhound/lists/sub_domains/subdomains-top1mil-20000.txt"
    gobuster_dir_medium_files = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-medium-files.txt"
    gobuster_dir_medium_dirs = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-medium-directories.txt"
    gobuster_vhost_m = "gobuster vhost -u {} -w /usr/share/wordlists/htbhound/lists/sub_domains/subdomains-top1mil-20000.txt"
    gobuster_dir_small_files = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-small-files.txt"
    gobuster_dir_small_dirs = "gobuster dir -u {} -w /usr/share/wordlists/htbhound/lists/Discovery/Web-Content/raft-small-directories.txt"
    gobuster_vhost_w = "gobuster vhost -u {} -w /usr/share/wordlists/htbhound/lists/sub_domains/subdomains-top1mil-5000.txt"
   



    if len(sys.argv) < 3 or not sys.argv[2]:
        print("Please provide two arguments: an integer and a URL")
    else:
        param1 = int(sys.argv[1])
        url = sys.argv[2]
    

        


        if param1 == 2:
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    futures = [
                    executor.submit(subprocess.run, gobuster_dir_large_files.format(url), shell=True, stdout=open(s_output_files, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_dir_large_dirs.format(url), shell=True, stdout=open(s_output_directories, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_vhost_s.format(url), shell=True, stdout=open(s_output_subdomains, "w"), stderr=open(dev_null, "w"))]
                concurrent.futures.wait(futures)
                print("\nFiles written to\n" + s_output_files + "\n" + s_output_directories + "\n" + s_output_subdomains)
            except KeyboardInterrupt:
                pass
                print("\nFiles written to\n" + s_output_files + "\n" + s_output_directories + "\n" + s_output_subdomains)
        elif param1 == 1:
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    futures = [
                    executor.submit(subprocess.run, gobuster_dir_medium_files.format(url), shell=True, stdout=open(m_output_files, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_dir_medium_dirs.format(url), shell=True, stdout=open(m_output_directories, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_vhost_m.format(url), shell=True, stdout=open(m_output_subdomains, "w"), stderr=open(dev_null, "w"))]
                concurrent.futures.wait(futures)
                print("\nFiles written to\n" + m_output_files + "\n" + m_output_directories + "\n" + m_output_subdomains)
            except KeyboardInterrupt:
                pass
                print("\nFiles written to\n" + m_output_files + "\n" + m_output_directories + "\n" + m_output_subdomains)
        elif param1 == 0:
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    futures = [
                    executor.submit(subprocess.run, gobuster_dir_small_files.format(url), shell=True, stdout=open(w_output_files, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_dir_small_dirs.format(url), shell=True, stdout=open(w_output_directories, "w"), stderr=open(dev_null, "w")),
                    executor.submit(subprocess.run, gobuster_vhost_w.format(url), shell=True, stdout=open(w_output_subdomains, "w"), stderr=open(dev_null, "w"))]
                concurrent.futures.wait(futures)
                print("\nFiles written to\n" + w_output_files + "\n" + w_output_directories + "\n" + w_output_subdomains)
            except KeyboardInterrupt:
                pass
                print("\nFiles written to\n" + w_output_files + "\n" + w_output_directories + "\n" + w_output_subdomains)
        else:
            print("Invalid parameter. Valid values are 0, 1, or 2.")




    
if __name__ == "__main__":
    main() 


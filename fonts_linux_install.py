#!/usr/bin/python3
##https://codingfleet.com/code-converter/bash/python/
############################
import os
import subprocess
import getpass
############################
def main():
    thisdir = os.getcwd()
    ttfhsciidir = f"{thisdir}/ttf/hscii"
    print(f"current directory is : {thisdir}. ttfhscii dir is {ttfhsciidir}")    
    key = input("Press 'r' to install/upgrade bigttf/smallttf/hsciittf fonts in this Linux system. It will ask for sudo password.\n")    
    if key == 'r':
        # Remove old hscii in 5 system font directories
        print("Removing hscii in 5 system font directories.")
        try:
            os.system("rm -rf ~/.fonts/hscii ~/.local/share/fonts/hscii")
            os.system("sudo rm -rf /usr/local/share/fonts/hscii /usr/share/fonts/truetype/hscii /root/.local/share/fonts/hscii")
        except Exception as e:
            print(f"Error removing old fonts: {e}")
###########################            
        # Copy new hscii
        print(f"Copying {ttfhsciidir} (hawing hscii fonts ttf files) in 5 share/fonts (linuksmint system fonts dirs).")
        try:
            os.system(f"cp -r {ttfhsciidir} ~/.fonts/")
            os.system(f"cp -r {ttfhsciidir}/*ttf ~/.local/share/fonts/")
            os.system(f"sudo cp -r {ttfhsciidir}/*ttf /usr/local/share/fonts/")
            os.system(f"sudo cp -r {ttfhsciidir}/*ttf /usr/share/fonts/truetype/")
            os.system(f"sudo cp -r {ttfhsciidir}/*ttf /root/.local/share/fonts/")
        except Exception as e:
            print(f"Error copying fonts: {e}")

        # Installing copied fonts
        print(f"Installing copied hscii fonts (from {ttfhsciidir}) in linuksmint system.")
        os.system("fc-cache -fv")
        os.system("sudo fc-cache -fv")
        print(f"Font installation done: now in {thisdir}")
    else:
        print(f"Pressed other key {key}. So not installed/upgraded bigttf/smallttf/hsciittf fonts in this Linux system.")
        print("Stopping script.")

if __name__ == "__main__":
    main()

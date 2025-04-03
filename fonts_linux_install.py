#!/usr/bin/python3
##https://codingfleet.com/code-converter/bash/python/
############################
import os
import subprocess
import getpass
############################
def main():
    thisdir = os.getcwd()
    fontdir = thisdir
	############################
    bigttfdir = os.path.join(fontdir, "bigttf")
    bigwoffdir = os.path.join(fontdir, "bigwoff")
    smallttfdir = os.path.join(fontdir, "smallttf")
    smallwoffdir = os.path.join(fontdir, "smallwoff")
    hsciittfdir = os.path.join(fontdir, "hsciittf")
    hsciiwoffdir = os.path.join(fontdir, "hsciiwoff")
	############################
    print(f"current directory is : {thisdir}")    
    key = input("Press 'r' to install/upgrade bigttf/smallttf/hsciittf fonts in this Linux system. It will ask for sudo password.\n")    
    if key == 'r':
        # Remove old hfont in 5 system font directories
        print("Removing hfont in 5 system font directories.")
        try:
            os.system("rm -rf ~/.fonts/hfont ~/.local/share/fonts/hfont")
            os.system("sudo rm -rf /usr/local/share/fonts/hfont /usr/share/fonts/truetype/hfont /root/.local/share/fonts/hfont")
        except Exception as e:
            print(f"Error removing old fonts: {e}")

        # Create hfont directories in 5 system font directories
        os.makedirs(os.path.expanduser("~/.fonts/hfont"), exist_ok=True)
        os.makedirs(os.path.expanduser("~/.local/share/fonts/hfont"), exist_ok=True)
        os.system("sudo mkdir -p /usr/local/share/fonts/hfont /usr/share/fonts/truetype/hfont /root/.local/share/fonts/hfont")

        # Copy new hfont
        print("Copying bigttf/smallttf/hsciittf fonts in 5 share/fonts.")
        try:
            os.system(f"cp -r {fontdir}/*ttf ~/.fonts/hfont/")
            os.system(f"cp -r {fontdir}/*ttf ~/.local/share/fonts/hfont/")
            os.system(f"sudo cp -r {fontdir}/*ttf /usr/local/share/fonts/hfont/")
            os.system(f"sudo cp -r {fontdir}/*ttf /usr/share/fonts/truetype/hfont/")
            os.system(f"sudo cp -r {fontdir}/*ttf /root/.local/share/fonts/hfont/")
        except Exception as e:
            print(f"Error copying fonts: {e}")

        # Installing copied fonts
        print("Installing copied fonts.")
        os.system("fc-cache -fv")
        os.system("sudo fc-cache -fv")
        print(f"Font installation done: {thisdir}")
    else:
        print(f"Pressed other key {key}. So not installed/upgraded bigttf/smallttf/hsciittf fonts in this Linux system.")
        print("Stopping script.")

if __name__ == "__main__":
    main()

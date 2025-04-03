#!/bin/bash
############################
thisdir="$(pwd)"
fontdir="${thisdir}"
############################
bigttfdir="${fontdir}/bigttf"
bigwoffdir="${fontdir}/bigwoff"
smallttfdir="${fontdir}/smallttf"
smallwoffdir="${fontdir}/smallwoff"
hsciittfdir="${fontdir}/hsciittf"
hsciiwoffdir="${fontdir}/hsciiwoff"
############################
printf "current directory is : $(pwd)\n"
read -n1 -s -r -p $'presskey r to install/upgrade bigttf/smallttf/hsciittf fonts in this linux system. it will ask for sudo password.\n' key
if [ "$key" = 'r' ]; then
	######### remowe old hfont in 5 system font dirs
	printf "remowing hfont in 5 system font dirs .\n"
	rm -rf ~/.fonts/hfont ~/.local/share/fonts/hfont
	sudo rm -rf /usr/local/share/fonts/hfont /usr/share/fonts/truetype/hfont /root/.local/share/fonts/hfont
	########## mkdir hfont in 5 system font dirs
	mkdir -p ~/.fonts/hfont ~/.local/share/fonts/hfont
	sudo mkdir -p /usr/local/share/fonts/hfont /usr/share/fonts/truetype/hfont /root/.local/share/fonts/hfont
	########## copy new hfont
	printf "copying bigttf/smallttf/hsciittf fonts in 5 share/fonts .\n"
	cp -r ${fontdir}/*ttf ~/.fonts/hfont/
	cp -r ${fontdir}/*ttf ~/.local/share/fonts/hfont/
	sudo cp -r ${fontdir}/*ttf /usr/local/share/fonts/hfont/
	sudo cp -r ${fontdir}/*ttf /usr/share/fonts/truetype/hfont/
	sudo cp -r ${fontdir}/*ttf /root/.local/share/fonts/hfont/
	####installing copied hfonts########################
	printf "installing copied fonts.\n"
	fc-cache -fv
	sudo fc-cache -fv
	printf "font instAll done : $(pwd)\n"
	####installed hfonts########################
else
	printf "pressed other key ${key} .  so not installed/upgraded bigttf/smallttf/hsciittf fonts in this linux system\n"
	printf "stoping script.\n"
fi	
############################


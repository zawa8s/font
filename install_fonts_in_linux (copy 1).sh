#!/bin/bash
############################
gitmsz_zw4s="mck82.vercel.app zikis8.vercel.app fb.com/ztrabc"
############################
lifontspath="/home/viml/mg/wrcl/weijunext/components/lifonts/fonts/"
freerepopath="/home/viml/mg/zw8/free/"
hpopfontpath="/home/viml/mg/hpop/app/src/main/res/font"
############################
## repo paths
thispath="/home/viml/mg/zw8/font/"
hfont_path="${thispath}/hfont"
############################
printf "current directory is : $(pwd)\n"
read -n1 -s -r -p $'pressed r to replace old and install new hfonts in linux system. it will ask for sudo password.\n' key
if [ "$key" = 'r' ]; then
	######### remowe old hfont in 5 share/fonts
	printf "remowing hfont in 5 share/fonts .\n"
	rm -rf ~/.fonts/hfont ~/.local/share/fonts/hfont
	sudo rm -rf /usr/local/share/fonts/hfont /usr/share/fonts/truetype/hfont /root/.local/share/fonts/hfont
	########## copy new hfont
	printf "copying hfont in 5 share/fonts .\n"
	cp -r ${hfont_path} ~/.fonts/
	cp -r ${hfont_path} ~/.local/share/fonts
	sudo cp -r ${hfont_path} /usr/local/share/fonts/
	sudo cp -r ${hfont_path} /usr/share/fonts/truetype/
	sudo cp -r ${hfont_path} /root/.local/share/fonts/
	####installing copied hfonts########################
	printf "installing copied fonts.\n"
	fc-cache -fv
	sudo fc-cache -fv
	printf "font instAll done : $(pwd)\n"
	####installed hfonts########################
else
	printf "pressed other key ${key} .  so not deleted old installed hfonts from linux system. \n"
	printf "stoping script.\n"
fi	
############################


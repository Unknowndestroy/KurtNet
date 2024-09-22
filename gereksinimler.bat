echo off
cls
color a
cd files
start gecko.bat
echo 15 Saniye bekleyin. GeckoDev yukleniyor.
timeout 15>nul
start pathadd.py
echo 15 Saniye bekleyin. Pip yukleniyor.
timeout 15>nul
echo 15 Saniye bekleyin. Kaynak kod Yukleniyor.
python gereksinimler2.py
echo off
mode 50
mode 100
mode 150
mode 200
mode 250
mode 300
mode 350
mode 400
mode 450
mode 500
mode 550
mode 600
mode 650
mode 700
mode 750
mode 800
mode 850
mode 900
mode 950
mode 1000
mode 950
mode 900
mode 850
mode 800
mode 750
mode 700
mode 650
mode 600
mode 550
mode 500
color c
tree
driverquery
color a
cls
echo   .d8888b.                           888               d8b          d8b               888                       
echo  d88P  Y88b                          888               Y8P          Y8P               888                       
echo  888    888                          888                                              888                       
echo  888         .d88b.  888d888 .d88b.  888  888 .d8888b  888 88888b.  888 88888b.d88b.  888  .d88b.  888d888      
echo  888  88888 d8P  Y8b 888P"  d8P  Y8b 888 .88P 88K      888 888 "88b 888 888 "888 "88b 888 d8P  Y8b 888P"        
echo  888    888 88888888 888    88888888 888888K  "Y8888b. 888 888  888 888 888  888  888 888 88888888 888          
echo  Y88b  d88P Y8b.     888    Y8b.     888 "88b      X88 888 888  888 888 888  888  888 888 Y8b.     888          
echo   "Y8888P88  "Y8888  888     "Y8888  888  888  88888P' 888 888  888 888 888  888  888 888  "Y8888  888          
echo .                                                                                                               
echo .                                                                                                               
echo .                                                                                                         
echo Y88b   d88P d8b  d8b 888      888                   d8b                                                        
echo  Y88b d88P  Y8P  Y8P 888      888                   Y8P                                                        
echo   Y88o88P            888      888                                                                              
echo    Y888P    888  888 888  888 888  .d88b.  88888b.  888 888  888  .d88b.  888d888                              
echo     888     888  888 888 .88P 888 d8P  Y8b 888 "88b 888 888  888 d88""88b 888P"                                
echo     888     888  888 888888K  888 88888888 888  888 888 888  888 888  888 888                                  
echo     888     Y88b 888 888 "88b 888 Y8b.     888  888 888 Y88b 888 Y88..88P 888                                  
echo     888      "Y88888 888  888 888  "Y8888  888  888 888  "Y88888  "Y88P"  888                                  
echo                                                              888                                               
echo                                                         Y8b d88P                                               
echo                                                          "Y88P"                                                
echo .
echo .

title  Gereksinimler Yukleniyor: PyQtWebEngine
pip install PyQtWebEngine
title  Gereksinimler Yukleniyor: PyQt5
pip install PyQt5
title  Gereksinimler Yukleniyor: requests
pip install requests
title Gereksinimler Yukleniyor: flask
pip install Flask
title  Gereksinimler Yukleniyor: gecko-dev
git clone https://github.com/mozilla/gecko-dev
title  Gereksinimler Yukleniyor: sys
pip install sys
title  Gereksinimler Yukleniyor: json
pip install json
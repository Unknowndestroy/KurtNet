@echo off
setlocal enabledelayedexpansion

:: Ngrok'u indir ve zip dosyasını aç
curl -o ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip
tar -xf ngrok.zip

:: Ngrok'u C:\Program Files\ngrok dizinine taşı
if not exist "C:\Program Files\ngrok" mkdir "C:\Program Files\ngrok"
move ngrok.exe "C:\Program Files\ngrok"

:: PATH değişkenini oku ve Ngrok yolunu ekle
set "NGROK_PATH=C:\Program Files\ngrok"
echo %PATH% | findstr /i "%NGROK_PATH%" >nul
if errorlevel 1 (
    setx PATH "%PATH%;%NGROK_PATH%"
    echo Ngrok PATH'e eklendi.
) else (
    echo Ngrok zaten PATH'te mevcut.
)

:: PATH'i kontrol etmek için %PATH% değişkenini ekrana yazdır
echo %PATH%

pause

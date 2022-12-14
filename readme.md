# HyperPixel 4.0 Square

Examples for Pimoroni's [HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square) high-resolution, 
high-speed, 4.0" display with optional touchscreen for Raspberry Pi written in Python 3.

| Python | Description                  |
|--------|------------------------------|
| 3.7    | development on macos         |
| 3.9    | testing on Raspberry Pi Zero |
| 3.9    | testing on Raspberry Pi 4    |

## Table of contents/examples

- Tkinter
  - [HyperClock](tk_modules/hyperclock.py)
  - [HyperCoin](tk_modules/duinocoin.py)
  - [HyperStream](tk_modules/hyperstream.py) *Raspberry PI 4 only*
  - [HyperWeather](tk_modules/hyperweather.py) *API Key from openweathermap.org needed*
  - [HyperHolidays](tk_modules/hyperholidays.py)
  - [HyperTimeWeather](tk_modules/hypertimeweather.py) *API Key from openweathermap.org needed*
  - [HyperText](tk_modules/hypertext.py)
- Kivy
  - [HyperCarousel](kv_modules/hypercarousel.py)
  - [HyperVideoCarousel](kv_modules/hypervideocarousel.py) *Raspberry PI 4 only*

## Note

> You can adapt, improve and use the code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Usage

### Run application form terminal

> You can run all examples in this form.

```shell
# change into HOME
$ cd ~

# clone repository
$ git clone https://github.com/Lupin3000/HyperPixel-4.0-Square.git

# change into example (eq. clock)
$ cd ~/HyperPixel-4.0-Square/tk_modules/

# execute (stop with <ESCAPE>)
$ python3 hyperclock.py
```

### Install fonts

> Please note that the fonts are only available for private use _(see [www.1001freefonts.com](https://www.1001freefonts.com))_!

```shell
# create directory
$ mkdir ~/.fonts

# copy all fonts
$ cp ~/HyperPixel-4.0-Square/*.ttf ~/.fonts/
```

### Autostart application

```shell
# create directory
$ mkdir -p ~/.config/autostart

# create desktop file
$ touch ~/.config/autostart/display.desktop
```

Example for display.desktop

```
[Desktop Entry]
Type=Application
Name=HyperWeather
Exec=/usr/bin/python3 ~/HyperPixel-4.0-Square/tk_modules/hyperweather.py
```

### Raspberry Bullseye

On bullseye you don't need to install any library/package for Hyperpixel! Also, i2c don't need to be enabled. 
The only thing you need to do, is to add one line in `/boot/config.txt`.

```shell
# start editor
$ sudo vim /boot/config.txt
```

Example of `/boot/config.txt` to enable hyperpixel display:

```
# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

Restart the device and the display should work!

### Install python dependencies

```shell
# install via pip from file
$ pip3 install -r requirements.txt

# verify installed pip packages (optional)
$ pip3 freeze
```

### Install packages for speach recognition

> Depend on API you like to use!!!

```shell
# minimum needed packages
$ sudo apt install espeak python3-pyaudio

# optional or if issues (sphinx)
$ sudo apt install flac pavucontrol libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt install swig libpulse-dev bison libasound2-dev alsa-utils gcc python3-pocketsphinx
```

```shell
# list playback hardware devices
$ aplay -l

# list capture hardware devices
$ arecord -l
```

## Error

If you failed and see error like "No module named cv2"

```shell
# update apt and install needed apt packages
$ sudo apt update && sudo apt install python3-opencv

# verify installation (optional)
$ python3 -c "import cv2"
```

If you failed and see error like "cannot import name ImageTk from PIL"

```shell
# update apt and install needed apt packages
$ sudo apt update && sudo apt install python3-pil python3-pil.imagetk

# verify installation (optional)
$ python3 -c "from PIL import ImageTk"
```

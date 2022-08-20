# HyperPixel 4.0 Square

Examples for Pimoroni's [HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square) high-resolution, 
high-speed, 4.0" display with optional touchscreen for Raspberry Pi written in Python 3.

| Python | Description             |
|--------|-------------------------|
| 3.7    | development on macos    |
| 3.9    | testing on Raspberry Pi |

## Table of contents/examples

- [HyperClock](./clock/hyperclock.py)
- [HyperStream](./rtsp/hyperstream.py) *Note: does not work on Raspberry PI Zero*
- [HyperCarousel](./carousel/hypercarousel.py)
- [HyperVideoCarousel](./carousel/hypervideocarousel.py) *Note: does not work on Raspberry PI Zero*
- [HyperDuinoCoin](./rest/duinocoin.py)

## Note

> You can adapt, improve and use the code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Usage

### Run example clock

> You can run all examples in this form.

```shell
# change into HOME
$ cd ~

# clone repository
$ git clone https://github.com/Lupin3000/HyperPixel-4.0-Square.git

# change into example (eq. clock)
$ cd ~/HyperPixel-4.0-Square/clock/

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

### Raspberry Bullseye

On bullseye you don't need to install any library/package for Hyperpixel! Also, i2c don't need to be enabled. 
The only thing you need to do, is to add one line in `/boot/config.txt`.

```shell
# start editor
$ sudo vim /boot/config.txt
```

Here the example:

```
# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

Restart the device and the display should work!

### Install python dependencies

> Some example directories include also the requirements.txt file.

```shell
# create directory
$ pip3 install -r requirements.txt

# verify installed packages (optional)
$ pip3 freeze
```

If you failed and see error like "No module named cv2"

```shell
# update apt
$ sudo apt update

# install opencv
$ sudo apt install python3-opencv

# verify installation (optional)
$ python3 -c "import cv2"
```

If you failed and see error like "cannot import name ImageTk from PIL"

```shell
# update apt
$ sudo apt update

# install opencv
$ sudo apt install python3-pil python3-pil.imagetk

# verify installation (optional)
$ python3 -c "from PIL import ImageTk"
```


# Waydroid GPS Fixer

## Requirements
- An image file containing the GPS driver. Examples:
  - [LineageOS](https://konstakang.com/devices/rpi4/LineageOS18/)
  - [BlissOS](https://sourceforge.net/projects/blissos-dev/files/Beta/Bliss-v14.10-x86_64-OFFICIAL-opengapps-20230325.iso/)
- Python 3 or higher

## Usage

### Waydroid GPS Fix
```sh
$ sudo python3 waydroid_gps_fix.py [image_path]
```
- `image_path`: Path to the image file with the GPS driver.

### GPS Tunnel
```sh
$ sudo python3 gps_read.py [device]
```
- `device`: Path to the device.

## Example
```sh
sudo python3 waydroid_gps_fix.py /path/to/source_image
sudo python3 gps_read.py /dev/ttyUSB0
```

## Credits
- [kklimianok](https://github.com/kklimianok)
- [mav-](https://github.com/mav-)
- [Waydroid Issues](https://github.com/waydroid/waydroid/issues/226)
- [waydroid_scripts](https://github.com/casualsnek/waydroid_script)



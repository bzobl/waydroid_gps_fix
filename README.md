# Waydroid GPS Fixer

# Requirements:
- An image file that contains the gps driver. (Image that i have used: [LineageOS](https://konstakang.com/devices/rpi4/LineageOS18/), [BlissOS](https://sourceforge.net/projects/blissos-dev/files/Beta/Bliss-v14.10-x86_64-OFFICIAL-opengapps-20230325.iso/))
- Python 3 or higher
# Usage:
- Waydroid gps fix:

```$ python3 waydroid_gps_fix.py [image_path]```

`image_path`: The path to the image file that contains the gps driver.

- GPS tunnel:

`$ python3 gps_read.py [device]`

`device`: The device path.
# Example:

`python3 waydroid_gps_fix.py /path/to/source_image`

`python3 gps_read.py /dev/ttyUSB0`
# Credits:
- [kklimianok](https://github.com/kklimianok)
- [mav-](https://github.com/mav-)
- [Waydroid issues](https://github.com/waydroid/waydroid/issues/226)





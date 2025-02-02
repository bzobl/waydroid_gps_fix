from sys import argv
import serial
import os
import pty
import time
import requests

ublox_configs = { #tested on neo 7m
    "Set_to_10Hz": "B562060806006400010001007A12",
    "full_power_mode": "B562068608000000000000000000945A",
    "odometer_mode": "B562061E14000000000001030000000000000A320000994C00005D2D",
    "10hz_nav_rate": "B562065C04000A00000070F4",
    "Set_to_57kbps": "B5620600140001000000D008000000E100000700070000000000E2E1",
}
def write_hex_data(port, baudrate, hex_datas, timeout=1):
    # print(hex_datas)
    # hex_data_values = list(hex_datas.values())
    # print(hex_data_values)
    for conf_name in list(hex_datas.keys()):
        try:
            # print(hex_data_values[conf_name])
            with serial.Serial(port, baudrate, timeout=timeout) as ser:
                ser.write(bytes.fromhex(hex_datas[conf_name]))
            print("Enabled: ", conf_name)
            time.sleep(0.350)
        except serial.SerialException as e:
            raise e
        except Exception as e:
            print(f"Exception: {e}")
            continue

def read_gps_data(port='/dev/ttyUSB0', baudrate=9600, timeout=1, pty_slave=None, pty_link=None):
    while True:
        try:
            write_hex_data(port, 9600, ublox_configs)
            print("Device found. Reading data...")
            ser = serial.Serial(port, baudrate, timeout=timeout)
            # with serial.Serial(port, baudrate, timeout=timeout) as ser:
            
            current_time = 0
            while True:
                line = ser.read()
                if line:
                    current_time = time.perf_counter()
                    # print(line.decode('ascii').strip())
                    # print(line)
                    os.write(pty_slave, line)
                if time.perf_counter() - current_time > 4:
                    print("Device not sending data. Retrying...")
                    ser.close()
                    break
                    
            
        except serial.SerialException as e:
            print("Device not found. Retrying in 5 seconds...")
            ser.close()
            time.sleep(5)
            pass
        except KeyboardInterrupt:
            os.remove(pty_link)
            break
        except Exception as e:
            print(f"Exception: {e}")
            continue
        # finally:
        #     continue

if __name__ == "__main__":
    # This script support hotplug of the GPS device and run prelaunch command to the gps module (mine is ublox NEO-7M)
    #device = "/dev/ttyUSB0"
    device = argv[1]
    print("Creating pty device")
    pty_master, pty_slave = pty.openpty()
    pty_link = "/dev/ttyGPSD"
    if os.path.exists(pty_link):
        os.remove(pty_link)
    os.symlink(os.ttyname(pty_slave), pty_link)
    os.chmod(pty_link, 0o777)  # Change permissions to be accessible by everyone
    print(f"Created pty device: {pty_link}")
    print("Service started!")
    read_gps_data(port=device, baudrate=57600, pty_slave=pty_master, pty_link=pty_link)
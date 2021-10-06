import serial
import time
import threading

# set serialport
ser = serial.Serial("COM3", 9600)

byte_data_full = b''
n = 0
flag = False


def change_flag():
    global flag
    input()
    flag = True


th = threading.Thread(target=change_flag)
th.start()

i = 0
while True:
    while flag:
        byte_data_full = b''
        print("input:")
        input_text = input()
        ser.write(input_text.encode('utf-8'))
        th.join()
        th = threading.Thread(target=change_flag)
        th.start()
        flag = False

    byte_data = ser.read_all()
    if len(byte_data) > 0:
        byte_data_full += byte_data
        print(byte_data_full)
        time.sleep(1)

th.join()

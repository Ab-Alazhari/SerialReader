import serial
import time
import threading


def print_func( value ):

    val = value
    ser = serial.Serial(value, 9600, timeout=0)

    print_com = 'Serial Print from port :  {0}\n'.format(val)

    fw = open('log.txt', 'a')
    fw.write(print_com)
    fw.close()

    time.sleep(3)

    reads = ser.readline()

    while 1:
        try:
            if len(reads) > 5:

                time_ = 'DateTime ' + time.strftime("%c")
                voltage = '{2}{3}{4}'.format(*reads.decode())
                freq = '{7}{8}'.format(*reads.decode())
                writes = '{0}:\t\tVoltage : {1};\t\t  Frequency : {2}\n'.format(time_, voltage, freq)
                fw = open('log.txt', 'a')
                fw.write(writes)
                fw.close()
                time.sleep(1)

        except ser.SerialTimeoutException:
            print('Data could not be read')
            time.sleep(1)
    return

def startp(port):
     threadw = threading.Thread(target=print_func, args=(port,))
     threadw.start()

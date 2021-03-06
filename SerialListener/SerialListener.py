import serial, time, logging, datetime

#Don't forget to update the serial port location!!
serial_port = serial.Serial('COM6', 9600, timeout=0)

header = ["time", "response"]
start = time.time()

def store(file, info):
    file.write(info + "\n")

def format_and_store(file, data):
    store(file, ",".join(data))


def main(serial_port):
    data_file_string = 'RCRSerialListener{}.dat'.format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M"))
    data_file = open(data_file_string, "w")

    format_and_store(data_file, header)
    print("Data file initialized.")

    try:
        while True:
            try:
                response = serial_port.readline()
                run_time = str(time.time() - start)
                format_and_store(data_file, [run_time, response])
                print("Stored:",run_time,response)
            except serial_port.SerialTimeoutException:
                print('Data could not be read.')
                format_and_store(data_file, [run_time, "No data found."])
    except KeyboardInterrupt:
        data_file.close()
        print("File closed.")

main(serial_port)
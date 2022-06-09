LOG_FILE = "setupapi.dev.log"
DEVICE_USB_STR = "USBSTOR"
DEVICE_START_STR = "[Device Install (Hardware initiated)"

with open(LOG_FILE) as f:
    for line in f:
        if (DEVICE_START_STR in line) and (DEVICE_USB_STR in line):
            data = line.split("#")[1].split("&")
            serial_number = line.split("#")[2].split("&")
            print(data[0], data[1], data[2], data[3], serial_number[0], sep=" ")
            time = next(f).split("/")
            print(
                "Time: ",
                time[2][:2],
                ".",
                time[1],
                ".",
                time[0][-4:],
                time[2][2:],
                sep="",
            )

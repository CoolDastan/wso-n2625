import machine
import sdcard
import uos

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(22, machine.Pin.OUT)

# Initialize SPI peripheral (start with 400 kHz)
spi = machine.SPI(0,
                  baudrate=400000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(23),
                  mosi=machine.Pin(23),
                  miso=machine.Pin(21))

print("SPI initialized")

# Initialize SD card
try:
    sd = sdcard.SDCard(spi, cs)
    print("SD card initialized")
except Exception as e:
    print("Failed to initialize SD card:", e)
    raise

# Mount filesystem
try:
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
    print("Filesystem mounted")
except Exception as e:
    print("Failed to mount filesystem:", e)
    raise

# Create a file and write something to it
try:
    with open("/sd/test01.txt", "w") as file:
        file.write("Hello, SD World!\r\n")
        file.write("This is a test\r\n")
    print("File written")
except Exception as e:
    print("Failed to write file:", e)
    raise

# Open the file we just created and read from it
try:
    with open("/sd/test01.txt", "r") as file:
        data = file.read()
        print("File read")
        print(data)
except Exception as e:
    print("Failed to read file:", e)
    raise

import machine
import utime
import time
import _thread
import ustruct
import sys

import lora as lora

cspin = machine.Pin(7, machine.Pin.OUT)  # NSS changed to Pin 7
dio0 = machine.Pin(9, machine.Pin.IN)    # Dio0 changed to Pin 9
rst = machine.Pin(10, machine.Pin.OUT)   # RST changed to Pin 10
spi = machine.SPI(0,
                  baudrate=2000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(14),   # SCK changed to Pin 14
                  mosi=machine.Pin(15),  # MOSI changed to Pin 15
                  miso=machine.Pin(6))   # MISO changed to Pin 6

lora_init = lora.begin(spi, cspin, rst, dio0, 434)

if lora_init:
    print("LoRa OK")
else:
    print("LoRa Failed!!")

while True:
    if lora_init:
        lora.beginPacket()
        data = "Hello!!"
        enc_data = data.encode()
        packet = bytearray(enc_data)
        es = lora.dataPacket(packet)
        lora.endPacket()
        print("Packet Sent")
    time.sleep(2)

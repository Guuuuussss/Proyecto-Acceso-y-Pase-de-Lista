import time
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print("Lectura finalizada")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

print ("Acercar la tarjeta RFID...")

while continue_reading:

    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK:
        print("Tarjeta detectada")

    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    if status == MIFAREReader.MI_OK:
        print("UID de la tarjeta: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))

    time.sleep(1)
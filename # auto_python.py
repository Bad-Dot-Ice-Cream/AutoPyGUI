# auto_python
import pyautogui as pg
import time, sys
import keyboard

numberCycles = 0

pg.FAILSAFE = True      # Fling mouse to top left to abort
print("Move the mouse to the top left, or press Ctrl+C to abort")


# try:
#     while True:
#         x, y = pg.position()
#         sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d}")
#         sys.stdout.flush()
#         time.sleep(0.05)     # ~ 20 updates per second

# except KeyboardInterrupt:
#     print("\nDone")



# Move mouse to 848, 377
# Auto Clicker
# pg.moveTo(848, 377)
# while True:
#     pg.click()
#     time.sleep(.03)

pg.moveTo(163, 211)

def send_email(numberCycles):
        if numberCycles > 0:
            while True:
                EMAIL_URL = "https://mail.google.com/mail/u/0/#inbox"
                EMAIL_TO = "michael.sekol@mahoningctc.com"
                SUBJECT = "AUTO/GUI Email From Cyruss Maiorana"
                BODY = "Two things I learned by writing this program include how to use programming for automated systems, which I previously thought was much more complicated. Second, I learned how to downlaod systems such as pyautogui and keyboard using 'pip'."
                pg.moveTo(1266, 1052)
                time.sleep(.5)
                pg.click()
                pg.moveTo(545, 64)
                time.sleep(.05)
                pg.click()
                pg.click()
                pg.click()
                pg.press('enter')
                pg.write(EMAIL_URL)
                time.sleep(.3)
                pg.moveTo(163, 211)
                time.sleep(0.4)
                pg.click()
                pg.moveTo(1367, 475)
                time.sleep(.05)
                pg.click()
                pg.write(EMAIL_TO)
                time.sleep(.05)
                pg.moveTo(1439, 524)
                pg.moveTo(1446, 516)
                pg.click()
                time.sleep(.05)
                pg.click()
                pg.moveTo(1406, 532)
                time.sleep(.2)
                pg.click()
                pg.write(SUBJECT)
                pg.moveTo(1506, 661)
                time.sleep(.2)
                pg.click()
                pg.write(BODY)
                pg.moveTo(1308, 998)
                time.sleep(.2)
                pg.click()
                def stop_loop():
                    xProgram = input("Type 0 to cancel the program, type 1 to loop again, or type ## for a multiple cycles: ")
                    if xProgram == "0":
                        print("Done.")
                        sys.exit()
                    elif xProgram == "1":
                        send_email()
                    elif xProgram == "##":
                        numberCycles = int(input("How many cycles would you like to run? "))
                        send_email(numberCycles)
                    else:
                        print("Error, please try again")
                        stop_loop()
                stop_loop()
        elif numberCycles == 0:
             stop_loop()
send_email(numberCycles)
import cv2
import imutils
import threading
import winsound

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)  # blur the flickering and smoothens the image

alarm = False
alarm_mode = False
alarm_counter = 0
no_motion_counter = 0

def beep_alarm():
    global alarm
    while alarm:
        print("!!! SUSPICIOUS ACTIVITY DETECTED !!!")
        winsound.Beep(2500, 2000)

while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        diff = cv2.absdiff(start_frame, gray)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        motion_pixels = cv2.countNonZero(thresh)  # counts the white pixels 

        # ---- MOTION LOGIC ----
        if motion_pixels > 100000:  # if the motion count is more than 100000 pixels it will trigger the alarm
            print("Motion detected:", motion_pixels)
            alarm_counter += 1
            no_motion_counter = 0
        else:
            no_motion_counter += 1

        # ---- START ALARM ----
        if alarm_counter > 10 and not alarm:  # this alerts if motion is detected for long amount of time
            alarm = True
            threading.Thread(target=beep_alarm, daemon=True).start()

        # ---- STOP ALARM ----
        if no_motion_counter > 30:
            alarm = False
            alarm_counter = 0

        cv2.imshow("Threshold Frame", thresh)
    else:
        cv2.imshow("Camera", frame)

    key = cv2.waitKey(30)
    if key == ord('t'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
        no_motion_counter = 0
        print("Alarm mode:", alarm_mode)

    if key == ord('q'):
        alarm = False
        break

cap.release()
cv2.destroyAllWindows()

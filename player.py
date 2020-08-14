import cv2
# cap = cv2.VideoCapture("rtmp://202.69.69.180:443/webcast/bshdlive-pc")
cap = cv2.VideoCapture("rtmp://35.236.192.63:1935/live/test2")
ret,frame = cap.read()

frame_width = int(cap.set(3, 1280))
frame_height = int(cap.set(4, 1024))
frameyowidth = int(cap.get(3))
frameyoheight = int(cap.get(4))

while ret:
    ret,frame = cap.read()
    cv2.imshow("streaming",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

# Closes all the frames
cv2.destroyAllWindows()





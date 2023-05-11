import cv2
from video_classes import IterPerSec
from video_classes import putIterationsPerSec

# Grab and show video frames without multithreading.
def noThreading(source=0):
    cap = cv2.VideoCapture(source)
    itps = IterPerSec().start()

    while True:
        (grabbed, frame) = cap.read()
        if not grabbed or cv2.waitKey(1) == ord("q"):
            break

        frame = putIterationsPerSec(frame, itps.itPerSec())
        cv2.imshow("Video", frame)
        itps.increment()

    print( itps.itPerSec() )

def main():
    source = 'Videos\VideoJorge.mp4' # 'video_recording.avi'
    noThreading(source)

if __name__ == "__main__":
    main()
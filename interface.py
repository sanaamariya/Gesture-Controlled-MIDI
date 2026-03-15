import cv2

def draw_interface(frame, chord, octave):

    h, w, _ = frame.shape

    # octave zones
    cv2.line(frame,(w//3,0),(w//3,h),(255,255,0),2)
    cv2.line(frame,(2*w//3,0),(2*w//3,h),(255,255,0),2)

    # zone labels
    cv2.putText(frame,"LOW",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame,"MID",(w//2-50,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame,"HIGH",(w-120,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    # chord display
    if chord:
        text = f"Chord: {chord}"
        cv2.putText(frame,text,(20,h-60),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    # octave display
    text2 = f"Octave: {octave}"
    cv2.putText(frame,text2,(20,h-20),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
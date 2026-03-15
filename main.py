import cv2
import time

from gesture_detector import GestureDetector
from midi_controller import MIDIController
from chords import get_chord
from interface import draw_interface
import config


cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

detector = GestureDetector()
midi = MIDIController()

current_notes = []
current_chord = None
current_octave = 4

# prevents rapid re-triggering
last_trigger_time = 0
cooldown = 0.3


while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hands = detector.detect(frame)

    h, w, _ = frame.shape

    for hand in hands:

        fingers = hand["fingers"]
        pinch = hand["pinch"]
        x = hand["x"] * w


        # OCTAVE CONTROL
        if x < w/3:
            octave = 2
        elif x < 2*w/3:
            octave = 4
        else:
            octave = 6

        current_octave = octave


        # CHORD CONTROL
        if fingers in config.GESTURE_CHORD_MAP:

            if time.time() - last_trigger_time > cooldown:

                chord = config.GESTURE_CHORD_MAP[fingers]

                if chord != current_chord:

                    notes = get_chord(chord, octave)

                    midi.stop_notes(current_notes)
                    midi.play_notes(notes)

                    current_notes = notes
                    current_chord = chord

                    last_trigger_time = time.time()


        # SUSTAIN CONTROL
        if pinch:
            midi.sustain_on()
        else:
            midi.sustain_off()


    # DRAW UI
    draw_interface(frame, current_chord, current_octave)

    cv2.imshow("Gesture Piano", frame)

    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()
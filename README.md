# Gesture-Controlled MIDI Instrument 🎹✋

A computer vision–based system that allows users to control a MIDI instrument using hand gestures. The application detects hand movements through a webcam and converts gestures into MIDI signals that can control instruments in GarageBand or other Digital Audio Workstations (DAWs).

This project combines **Computer Vision**, **Gesture Recognition**, and **Music Technology** to create a touchless musical interface.

---

## Features

- Hand tracking using MediaPipe
- Gesture recognition for triggering chords
- MIDI output integration
- Control instruments in GarageBand
- Octave control based on hand position
- Two-hand gesture support
- Sustain control using pinch gestures

---

## How It Works

1. The webcam captures real-time video input.
2. MediaPipe detects and tracks hand landmarks.
3. Gestures are interpreted based on finger positions.
4. The system maps gestures to chords and octaves.
5. MIDI messages are sent to GarageBand using a virtual MIDI driver.

Pipeline:

Camera → Hand Detection → Gesture Recognition → MIDI Output → GarageBand Instrument

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Mido (MIDI library)
- Virtual MIDI Driver (IAC Driver on macOS)

---

## Project Structure
Gesture-Controlled-MIDI
│
├── main.py
├── gesture_detector.py
├── midi_controller.py
├── chords.py
├── interface.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/sanaamariya/Gesture-Controlled-MIDI.git

cd Gesture-Controlled-MIDI

### 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Enable MIDI Driver (macOS)

Open **Audio MIDI Setup**

1. Go to **MIDI Studio**
2. Double-click **IAC Driver**
3. Enable **Device is online**

### 5. Run the project
python main.py

---

## Gesture Controls

| Gesture | Action |
|--------|--------|
| 1 Finger | C Chord |
| 2 Fingers | F Chord |
| 3 Fingers | G Chord |
| 4 Fingers | Am Chord |
| Pinch Gesture | Sustain |
| Move hand left/right | Change octave |

---

## Work in Progress 🚧

This project is currently **under active development** and more features will be added. The current implementation demonstrates the core idea of gesture-based MIDI control, but several improvements are planned.

Upcoming additions may include:

- Air piano mode (triggering individual notes instead of chords)
- Improved gesture stability and smoothing
- Velocity control based on hand movement
- Enhanced visual interface
- Multi-instrument support
- Machine learning based gesture recognition

---

## Future Improvements

- Real-time gesture classification using machine learning
- Support for multiple MIDI instruments
- Visual keyboard overlay
- Custom gesture mapping
- Cross-platform MIDI support

---

## License

This project is intended for educational and experimental purposes.

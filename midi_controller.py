import mido

class MIDIController:

    def __init__(self):

        self.port = mido.open_output("IAC Driver Gesture MIDI")

    def play_notes(self, notes):

        for n in notes:
            self.port.send(mido.Message("note_on", note=n, velocity=90))

    def stop_notes(self, notes):

        for n in notes:
            self.port.send(mido.Message("note_off", note=n))

    def sustain_on(self):

        self.port.send(mido.Message("control_change", control=64, value=127))

    def sustain_off(self):

        self.port.send(mido.Message("control_change", control=64, value=0))
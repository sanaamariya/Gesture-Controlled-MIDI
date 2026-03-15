def get_chord(chord, octave):

    base = {
        "C": [0,4,7],
        "F": [5,9,12],
        "G": [7,11,14],
        "Am":[9,12,16]
    }

    root = 12 * octave

    return [root + n for n in base[chord]]
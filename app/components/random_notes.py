from random import choice
from adapt import Note, bracket, get_scale

def RandomNotes(sess, track, root, scale):
    note_interval = 1/4
    piano_scale = get_scale(root, scale)

    if "excitement" in sess.params:
        interval_brackets = bracket({0.1: 1, 0.3: 1/2, 0.5: 1/4, 0.7: 1/8, 0.8: 1/16, 1: 1/32})
        note_interval = interval_brackets(sess.params["excitement"])

    if sess.clock.on_bars(note_interval):
        return Note(
            track=track,
            value=choice(piano_scale),
            velocity=127,
            duration=sess.clock.beats(1)
        )
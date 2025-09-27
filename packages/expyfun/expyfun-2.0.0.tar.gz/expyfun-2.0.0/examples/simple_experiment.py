"""
=======================
Run a simple experiment
=======================

This example demonstrates much of the basic functionality built into
the ExperimentController class.
"""
# Author: Dan McCloy <drmccloy@uw.edu>
#
# License: BSD (3-clause)

print(__doc__)

from os import path as op
import numpy as np
from scipy import io as sio

from expyfun import ExperimentController
from expyfun._utils import set_log_level
import expyfun.analyze as ea


set_log_level('INFO')

# set configuration
ac = 'pyglet'  # change to 'RM1' or 'RP2' for TDT use
fs = 44100
noise_db = 45  # dB for background noise
stim_db = 65  # dB for stimuli
min_resp_time = 0.1
max_resp_time = 2.0
feedback_dur = 0.5
isi = 0.2
running_total = 0

# if the stimuli have not been made, let's make them in examples dir
stimulus_file = 'equally_spaced_sinewaves.mat'
if not op.isfile(stimulus_file):
    from generate_stimuli import generate_stimuli
    generate_stimuli(output_dir='.', fs=fs)

# load stimuli (from a call to generate_stimuli() from generate_stimuli.py)
stims = sio.loadmat('equally_spaced_sinewaves.mat')
orig_rms = stims['rms'][0]
freqs = stims['freqs'][0]
fs = stims['fs'][0][0]
trial_order = stims['trial_order'][0]
num_trials = len(trial_order)
num_freqs = len(freqs)

if num_freqs > 8:
    raise RuntimeError('Too many frequencies, not enough buttons.')

# keep only sinusoids, make stereo, order low-high, convert to list of arrays
wavs = {k: np.r_[stims[k], stims[k]].T for k in stims if 'stim_' in k}
wavs = [np.ascontiguousarray(v) for _, v in sorted(wavs.items())]

# instructions
instructions = ('You will hear tones at {0} different frequencies. Your job is'
                ' to press the button corresponding to that frequency. Please '
                'press buttons 1-{0} now to hear each tone.').format(num_freqs)

instr_finished = ('Okay, now press any of those buttons to start the real '
                  'thing. There will be background noise.')

# select audio controller
if ac != 'pyglet':
    ac = dict(TYPE='tdt', TDT_MODEL=ac)

with ExperimentController('testExp', ac, screen_num=0,
                          window_size=[800, 600], full_screen=False,
                          stim_db=stim_db, noise_db=noise_db, stim_fs=fs,
                          participant='foo', session='001',
                          verbose=True) as ec:

    # define usable buttons / keys
    live_keys = [x + 1 for x in range(num_freqs)]
    not_yet_pressed = live_keys[:]

    # show instructions until all buttons have been pressed at least once
    ec.screen_text(instructions)
    screenshot = ec.screenshot()
    ec.flip()
    while len(not_yet_pressed) > 0:
        pressed, timestamp = ec.wait_one_press(live_keys=live_keys)
        for p in pressed:
            p = int(p)
            ec.load_buffer(wavs[p - 1])
            ec.play()
            ec.wait_secs(len(wavs[p - 1]) / float(ec.fs))
            ec.stop()
            if p in not_yet_pressed:
                not_yet_pressed.pop(not_yet_pressed.index(p))
    ec.clear_buffer()
    ec.flip()  # clears the screen
    ec.wait_secs(isi)

    # show instructions finished screen
    ec.screen_prompt(instr_finished, live_keys=live_keys)
    ec.wait_secs(isi)

    ec.call_on_next_flip(ec.start_noise())
    ec.screen_prompt('<center>OK, here we go!</center>',
                     max_wait=feedback_dur, live_keys=None)
    ec.wait_secs(isi)

    single_trial_order = trial_order[range(len(trial_order) / 2)]
    mass_trial_order = trial_order[len(trial_order) / 2:]
    # run the single-tone trials
    for stim_num in single_trial_order:
        ec.write_data_line('one-tone trial', stim_num + 1)
        ec.clear_buffer()
        ec.load_buffer(wavs[stim_num])
        ec.identify_trial(ec_id=stim_num, ttl_id=[0, 0])
        ec.start_stimulus()
        pressed, timestamp = ec.wait_one_press(max_resp_time, min_resp_time,
                                               live_keys)
        ec.stop()  # will stop stim playback as soon as response logged

        # some feedback
        if pressed is None:
            message = 'Too slow!'
        elif int(pressed) == stim_num + 1:
            running_total += 1
            message = ('Correct! Your reaction time was '
                       '{}').format(round(timestamp, 3))
        else:
            message = ('You pressed {0}, the correct answer was '
                       '{1}.').format(pressed, stim_num + 1)
        ec.screen_prompt(message, max_wait=feedback_dur)
        ec.wait_secs(isi)
        ec.trial_ok()

    # create 100 ms pause to play between stims and concatenate
    pause = np.zeros((int(ec.fs / 10), 2))
    concat_wavs = wavs[mass_trial_order[0]]
    for num in mass_trial_order[1:len(mass_trial_order)]:
        concat_wavs = np.r_[concat_wavs, pause, wavs[num]]
    concat_dur = len(concat_wavs) / float(ec.fs)
    # run mass trial
    ec.screen_prompt('Now you will hear {0} tones in a row. After they stop, '
                     'wait for the "Go!" prompt, then you will have {1} '
                     'seconds to push the buttons in the order that the tones '
                     'played in. Press one of the buttons to begin.'
                     ''.format(len(mass_trial_order), max_resp_time),
                     live_keys=live_keys)
    ec.clear_buffer()
    ec.load_buffer(concat_wavs)
    ec.write_data_line('multi-tone trial', [x + 1 for x in mass_trial_order])
    ec.identify_trial(ec_id='multi-tone', ttl_id=[0, 1])
    ec.start_stimulus()
    ec.wait_secs(len(concat_wavs) / float(ec.stim_fs))
    ec.screen_text('<center>Go!</center>')
    ec.flip()
    pressed = ec.wait_for_presses(max_resp_time + 1, min_resp_time,
                                  live_keys, False)
    answers = [str(x + 1) for x in mass_trial_order]
    correct = [press == ans for press, ans in zip(pressed, answers)]
    running_total += sum(correct)
    ec.call_on_next_flip(ec.stop_noise())
    ec.screen_prompt('You got {0} out of {1} correct.'
                     ''.format(sum(correct), len(answers)),
                     max_wait=feedback_dur)
    ec.trial_ok()

    # end experiment
    ec.screen_prompt('All done! You got {0} correct out of {1} tones. Press '
                     'any key to close.'.format(running_total, num_trials),
                     max_wait=feedback_dur)

import matplotlib.pyplot as plt
plt.ion()
ea.plot_screen(screenshot)

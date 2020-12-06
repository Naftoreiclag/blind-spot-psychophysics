#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.6),
    on Sat Dec  5 11:54:19 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.6'
expName = 'weber'  # from the Builder filename that created this script
expInfo = {'participant': '', 'eye_lr': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/james/Projects/vs260A/blind-spot-psychophysics/experiment/experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='tiffany_laptop', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Calibration"
CalibrationClock = core.Clock()
alignment_rectangle = visual.Rect(
    win=win, name='alignment_rectangle',
    width=(26, 16)[0], height=(26, 16)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixate_vert = visual.Line(
    win=win, name='fixate_vert',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fixate_horiz = visual.Line(
    win=win, name='fixate_horiz',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
confirm_prompt = visual.TextStim(win=win, name='confirm_prompt',
    text='Press Space to confirm calibration.',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
fixate_vert_2 = visual.Line(
    win=win, name='fixate_vert_2',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixate_horiz_2 = visual.Line(
    win=win, name='fixate_horiz_2',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
key_resp_2 = keyboard.Keyboard()
bottom_line = visual.Line(
    win=win, name='bottom_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
middle_line = visual.Line(
    win=win, name='middle_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
top_line = visual.Line(
    win=win, name='top_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
blind_spot = visual.Polygon(
    win=win, name='blind_spot',
    edges=50, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "Done"
DoneClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Hurray you’re done!',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Calibration"-------
continueRoutine = True
# update component parameters for each repeat
fixate_vert.setPos((5*int(expInfo['eye_lr']),0))
fixate_horiz.setPos((5*int(expInfo['eye_lr']),0))
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
CalibrationComponents = [alignment_rectangle, fixate_vert, fixate_horiz, confirm_prompt, key_resp]
for thisComponent in CalibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CalibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Calibration"-------
while continueRoutine:
    # get current time
    t = CalibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CalibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alignment_rectangle* updates
    if alignment_rectangle.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alignment_rectangle.frameNStart = frameN  # exact frame index
        alignment_rectangle.tStart = t  # local t and not account for scr refresh
        alignment_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alignment_rectangle, 'tStartRefresh')  # time at next scr refresh
        alignment_rectangle.setAutoDraw(True)
    
    # *fixate_vert* updates
    if fixate_vert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixate_vert.frameNStart = frameN  # exact frame index
        fixate_vert.tStart = t  # local t and not account for scr refresh
        fixate_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixate_vert, 'tStartRefresh')  # time at next scr refresh
        fixate_vert.setAutoDraw(True)
    
    # *fixate_horiz* updates
    if fixate_horiz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixate_horiz.frameNStart = frameN  # exact frame index
        fixate_horiz.tStart = t  # local t and not account for scr refresh
        fixate_horiz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixate_horiz, 'tStartRefresh')  # time at next scr refresh
        fixate_horiz.setAutoDraw(True)
    
    # *confirm_prompt* updates
    if confirm_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confirm_prompt.frameNStart = frameN  # exact frame index
        confirm_prompt.tStart = t  # local t and not account for scr refresh
        confirm_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confirm_prompt, 'tStartRefresh')  # time at next scr refresh
        confirm_prompt.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CalibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Calibration"-------
for thisComponent in CalibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('alignment_rectangle.started', alignment_rectangle.tStartRefresh)
thisExp.addData('alignment_rectangle.stopped', alignment_rectangle.tStopRefresh)
thisExp.addData('fixate_vert.started', fixate_vert.tStartRefresh)
thisExp.addData('fixate_vert.stopped', fixate_vert.tStopRefresh)
thisExp.addData('fixate_horiz.started', fixate_horiz.tStartRefresh)
thisExp.addData('fixate_horiz.stopped', fixate_horiz.tStopRefresh)
thisExp.addData('confirm_prompt.started', confirm_prompt.tStartRefresh)
thisExp.addData('confirm_prompt.stopped', confirm_prompt.tStopRefresh)
# the Routine "Calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/line_locs.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    fixate_vert_2.setPos((5*int(expInfo['eye_lr']),0))
    fixate_horiz_2.setPos((5*int(expInfo['eye_lr']), 0))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    bottom_line.setPos((blind_x*int(expInfo['eye_lr']), bottom_y))
    middle_line.setPos((blind_x*int(expInfo['eye_lr']), middle_y))
    top_line.setPos((blind_x*int(expInfo['eye_lr']), top_y))
    blind_spot.setPos((int(expInfo['eye_lr'])*blind_x, blind_y))
    blind_spot.setSize((blind_w, blind_h))
    # keep track of which components have finished
    TrialComponents = [fixate_vert_2, fixate_horiz_2, key_resp_2, bottom_line, middle_line, top_line, blind_spot]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixate_vert_2* updates
        if fixate_vert_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixate_vert_2.frameNStart = frameN  # exact frame index
            fixate_vert_2.tStart = t  # local t and not account for scr refresh
            fixate_vert_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixate_vert_2, 'tStartRefresh')  # time at next scr refresh
            fixate_vert_2.setAutoDraw(True)
        
        # *fixate_horiz_2* updates
        if fixate_horiz_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixate_horiz_2.frameNStart = frameN  # exact frame index
            fixate_horiz_2.tStart = t  # local t and not account for scr refresh
            fixate_horiz_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixate_horiz_2, 'tStartRefresh')  # time at next scr refresh
            fixate_horiz_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['w', 's', 'x'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *bottom_line* updates
        if bottom_line.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            bottom_line.frameNStart = frameN  # exact frame index
            bottom_line.tStart = t  # local t and not account for scr refresh
            bottom_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_line, 'tStartRefresh')  # time at next scr refresh
            bottom_line.setAutoDraw(True)
        
        # *middle_line* updates
        if middle_line.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            middle_line.frameNStart = frameN  # exact frame index
            middle_line.tStart = t  # local t and not account for scr refresh
            middle_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(middle_line, 'tStartRefresh')  # time at next scr refresh
            middle_line.setAutoDraw(True)
        
        # *top_line* updates
        if top_line.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            top_line.frameNStart = frameN  # exact frame index
            top_line.tStart = t  # local t and not account for scr refresh
            top_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_line, 'tStartRefresh')  # time at next scr refresh
            top_line.setAutoDraw(True)
        
        # *blind_spot* updates
        if blind_spot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blind_spot.frameNStart = frameN  # exact frame index
            blind_spot.tStart = t  # local t and not account for scr refresh
            blind_spot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blind_spot, 'tStartRefresh')  # time at next scr refresh
            blind_spot.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixate_vert_2.started', fixate_vert_2.tStartRefresh)
    trials.addData('fixate_vert_2.stopped', fixate_vert_2.tStopRefresh)
    trials.addData('fixate_horiz_2.started', fixate_horiz_2.tStartRefresh)
    trials.addData('fixate_horiz_2.stopped', fixate_horiz_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials.addData('bottom_line.started', bottom_line.tStartRefresh)
    trials.addData('bottom_line.stopped', bottom_line.tStopRefresh)
    trials.addData('middle_line.started', middle_line.tStartRefresh)
    trials.addData('middle_line.stopped', middle_line.tStopRefresh)
    trials.addData('top_line.started', top_line.tStartRefresh)
    trials.addData('top_line.stopped', top_line.tStopRefresh)
    trials.addData('blind_spot.started', blind_spot.tStartRefresh)
    trials.addData('blind_spot.stopped', blind_spot.tStopRefresh)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Done"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
DoneComponents = [text]
for thisComponent in DoneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DoneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Done"-------
while continueRoutine:
    # get current time
    t = DoneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DoneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Done"-------
for thisComponent in DoneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "Done" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

# This is a quick EAS Endec for my EAS Mocks. All code is sloppier than spaghetti, which it might be even neatter than this. :P

# 1st Party (Main) Dependecies
import os
import os.path
# 3rd Party Dependecies
from EASGen import *
from EAS2Text import *
from pydub import *

# Code
header1 = input("Insert RAW Header Data to encode here:")
decodedtext = EAS2Text(header1).EASText
confirm = input('Are you sure you want to encode? The decoded text is:' + decodedtext)
if confirm.lower() == "yes":
    emulation = input("What style do you wish the headers to be?")
    if emulation.lower() == "TFT":
        print("Resampling to 8khz...")
    if emulation.lower() == "NWS":
        print("Resampling down to 11Khz...")
    if emulation.lower() == "DAS":
        print("Cranking UP the samplerate to 48000...")
if confirm.lower() == "no":
    print("Abort.")
    exit()
audio = input("Input your path for audio, if you want it, now. Or, input none for no audio. MUST BE A WAV FILE!!")
if audio.lower() == "none":
    if emulation.lower == "DAS":
        print("Generating DASDEC Tones...")
        alerttonesnoaudio = EASGen.genEAS(header=header1, attentionTone=True, mode=emulation, endOfMessage=True)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttonesnoaudio)
        print("Successfully exported! Have fun! Made by miceoroni.")
    exit()
else:
# check if the audio actually exists
    audiocheck = os.path.isfile(audio)
    if audiocheck is True:
        print("Generating tones... Please stand by...")
        audio1 = AudioSegment.from_wav(audio)
        alerttones = EASGen.genEAS(header=header1, attentionTone=True, audio=audio1, mode=emulation, endOfMessage=True)
    EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttones)
    print("Successfully exported! Have fun! Made by miceoroni.")
    exit()
    if audiocheck is False:
        print("The audio file you have specified does not exist. Please try again.")
    exit()


    
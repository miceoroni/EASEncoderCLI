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
confirm = input('Are you sure you want to encode? The decoded text is: ' + decodedtext)
if confirm.lower() == "yes":
    emulation = input("What style do you wish the headers to be?")
    if emulation.lower() == "tft":
        print("Resampling to 8khz...")
    if emulation.lower() == "nws":
        print("Resampling down to 11Khz...")
    if emulation.lower() == "das":
        print("Cranking UP the samplerate to 48000...")
if confirm.lower() == "no":
    print("Abort.")
    exit()
audio = input("Input your path for audio, if you want it, now. Or, input none for no audio. MUST BE A WAV FILE!!")
if audio.lower() == "none":
    print("none")
    if emulation.lower() == "das":
        print("Generating DASDEC Tones...")
        alerttonesnoaudio = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, sampleRate=48000)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttonesnoaudio)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
    if emulation.lower() == "nws":
        print("Generating NWS Tones...")
        alerttonesnoaudio = EASGen.genEAS(header=header1, attentionTone=True, mode=emulation, endOfMessage=True).set_frame_rate(11025)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttonesnoaudio)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
    if emulation.lower() == "tft":
        print("Generating TFT Tones...")
        alerttonesnoaudio = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True).set_frame_rate(8000)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttonesnoaudio)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
    # Just generate the actual headers with nothing
    haha = emulation.lower()
    if "tft" not in haha and "nws" not in haha and "das" not in haha:
        print("Generating tones...")
        alerttonesnoaudio = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, mode=emulation)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttonesnoaudio)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
else:
# check if the audio actually exists
    audiocheck = os.path.isfile(audio)
    if audiocheck is True:
        if emulation.lower() == "das":
            print("Generating DASDEC Tones...")
            audioseg = AudioSegment.from_wav(audio)
            alerttones = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, sampleRate=48000, audio=audioseg)
            EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttones)
            print("Successfully exported! Have fun! Made by miceoroni.")
            exit()
    if emulation.lower() == "nws":
        print("Generating NWS Tones...")
        audioseg = AudioSegment.from_wav(audio)
        alerttones = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, mode=emulation.upper, audio=audioseg).set_frame_rate(11025)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttones)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
    if emulation.lower() == "tft":
        print("Generating TFT Tones...")
        audioseg = AudioSegment.from_wav(audio)
        alerttones = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, audio=audioseg).set_frame_rate(8000)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttones)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()
    # Just generate the actual headers with nothing
    haha = emulation.lower()
    if "tft" not in haha and "nws" not in haha and "das" not in haha:
        print("Generating tones...")
        audioseg = AudioSegment.from_wav(audio)
        alerttones = EASGen.genEAS(header=header1, attentionTone=True, endOfMessage=True, mode=emulation.upper, audio=audioseg)
        EASGen.export_wav("EASEncoderCLIGenTones.wav", alerttones)
        print("Successfully exported! Have fun! Made by miceoroni.")
        exit()

    if audiocheck is False:
        print("The audio file you have specified does not exist. Please try again.")
    exit()


    
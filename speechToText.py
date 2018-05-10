#!/usr/bin/python

import speech_recognition as sr
import sys
import os
import shutil
r = sr.Recognizer()
try:
    shutil.rmtree('./out')
except:
    print("Failed to delete out.")
os.mkdir('./out')
os.system('ffmpeg -i {} -f segment -segment_time 30 -c copy ./out/out%03d.wav'.format(sys.argv[1]))
try:
    os.remove("{}.txt".format(sys.argv[1]))
except:
    print("No such file {}.txt".format(sys.argv[1]))
for filename in sorted(os.listdir('./out')):
    audioFile = sr.AudioFile(os.path.join('./out/',filename))
    with audioFile as source:
        audio = r.record(source)
    outputG = open("{}.txt".format(sys.argv[1]), 'a')

    outputG.write("\n{}\n ".format(filename))
    outputG.write(r.recognize_google(audio))
    outputG.close()


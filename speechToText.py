#!/usr/bin/python

import speech_recognition as sr
import sys
import os
import shutil
import datetime
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
count = 0
print("{} audio files created to process".format(len(os.listdir('./out'))))
for filename in sorted(os.listdir('./out')):
    print("Processing {}".format(filename))
    try:
        audioFile = sr.AudioFile(os.path.join('./out/',filename))
        with audioFile as source:
            audio = r.record(source)
        outputG = open("{}.txt".format(sys.argv[1]), 'a')

        outputG.write("\n{} {} \n ".format(filename,str(datetime.timedelta(seconds=count*30))))
        outputG.write(r.recognize_google(audio))
        outputG.write("\n")
        outputG.close()
        count=count+1
    except:
        outputG = open("{}.txt".format(sys.argv[1]), 'a')
        outputG.write("***Could not recognize audio***\n ")
        outputG.close()
        count=count+1

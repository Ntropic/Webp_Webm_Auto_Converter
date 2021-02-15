# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:16:23 2018

@author: Michael Schilling
"""

from PIL import Image
import ffmpy
import os

import sched
import time

#add_to_startup()

event_schedule = sched.scheduler(time.time, time.sleep)


def transform_media():
    folder = "C:\\Users\\Michael Schilling\\Pictures"
    sub_folder_name = 'Converted_Files'
    os.chdir(folder)
    
    filenames=os.listdir(folder)
    #webp to jpg
    length=0;
    for i in range(0,len(filenames)):
        if filenames[i][len(filenames[i])-4:len(filenames[i])]=='webp':
            length=length+1;
            
    len2=1;
    for i in range(0,len(filenames)):
        if filenames[i][len(filenames[i])-4:len(filenames[i])]=='webp':
            print('Converting '+str(len2)+'/'+str(length));
            im = Image.open(filenames[i]).convert("RGB")
            im.save(os.path.join(sub_folder_name,filenames[i][0:len(filenames[i])-5]+'.jpg'),"jpeg")
            os.remove(filenames[i])
            len2=len2+1;
    if len2>1:
        print('Finished conversions of pictures for now');

    filenames=os.listdir(folder)
    #Webm to mpeg-4
    length=0;
    for i in range(0,len(filenames)):
        if filenames[i][len(filenames[i])-4:len(filenames[i])]=='webm':
            length=length+1;
            
    len2=1;
    for i in range(0,len(filenames)):
        if filenames[i][len(filenames[i])-4:len(filenames[i])]=='webm':
            print('Converting '+str(len2)+'/'+str(length));
            ff = ffmpy.FFmpeg(inputs={filenames[i]: None},outputs={os.path.join(sub_folder_name,filenames[i][0:len(filenames[i])-5]+'.mp4'): None})
            ff.run()
            os.remove(filenames[i])
            len2=len2+1;
    if len2>1:
        print('Finished conversions of movies for now');
    event_schedule.enter(10, 1, transform_media)
        
event_schedule.enter(10, 1, transform_media)
event_schedule.run()
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:44:14 2021

@author: student
"""
import classes as classes
import time


def desision(end, start_point):

    comands = classes.my_programm(start_point, end)
    if (comands != None):
        #print(comands)
        #for i in range(0, len(comands), 2):
            # #Проверяем на наличие красного или жёлтого светофора
            # comand = "Traffic light"
            # if comand == "red":
            #     while not(command=="green"):
            #         time.sleep(1)
            #         comand = "green"
            # if comand == "yellow":
            #     while command=="yellow":
            #         time.sleep(0.25)
            #         comand = "red"


            #повернуть на
            #a = str(comands[i])
            #проехать
           # b = str(comands[i+1])
            #print(a)
           # print(b)
        return comands
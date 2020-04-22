# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/4/20 11:37 上午 

import os


# file = 'log_0.946286094224924.txt'

def analysis_file(file):
    print(file)

    lines = open(file).readlines()

    for line in lines:
        if 'Dialog Accuracy' in line:
            print(line.strip())
        if 'BLEU SCORE' in line:
            print(line.strip())

    # print("acc_test=" + lines[-3].strip())
    # print("acc_oov_test=" + lines[-1].strip())
    print(lines[-3].strip() + "\t" + lines[-1].strip())


def run_all():
    files = os.listdir('./')
    for file in files:
        if file.startswith('log_'):
            analysis_file(file)


def print_file():
    files = os.listdir('./')
    for file in files:
        if file.startswith('log_'):
            # file = file.replace("log_",'').replace(".txt",'')
            print(file)


# print_file()

analysis_file('log_0.8816251899696049.txt')

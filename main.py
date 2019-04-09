# -*- coding: UTF-8 -*-
# main.py
# Root file for EmotionDetection program.

# Prints out command line menu and handles user choices

from __future__ import print_function
from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import GUI

try:
    input = raw_input
except NameError:
    pass

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def printMenu():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,", "EmotionDetection", ",¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°\n")
    print("1. Training")
    print("2. Testing")
    print("3. Evaluate Text")
    print("4. GUI Evaluation")
    print("5. Information")
    print("6. Exit\n")
    print(78 * "-", "\n")


def main():
    print('welcome')


# Training Program, builds map of words and emotion values from annotated corpus
def train():
    reset = input("Reset training data? [y/n]: ").lower() in ["yes", "y", "1"]
    text = input("Text file: ")
    values = input("Value file: ")
    print("")

    try:
        print("Loading input values into WordMap...\n")
        with open("./data/" + text, 'r') as textFile:
            with open("./data/" + values, 'r') as valueFile:
                WordMap.buildWordMap(reset, textFile, valueFile)

    except IOError:
        print("File not found. Returning to main menu...\n")


def do_train(tf, vf, rs):
    try:
        print("Loading input values into WordMap...\n")
        with open(tf, 'r') as textFile:
            with open(vf, 'r') as valueFile:
                WordMap.buildWordMap(rs, textFile, valueFile)

    except IOError:
        print("File not found. Returning to main menu...\n")


def test():
    text = input("Text file: ")
    values = input("Value file: ")
    print("")
    print ("values file is " ,  "./data/" + values)
    try:
        print("\nRunning text evaluation...\n")
        with open("./data/" + text, 'r') as textFile:
            print ("text found")
            with open("./data/" + values, 'r') as valueFile:
                print ("values found")
                EvaluateText.evaluate(textFile, valueFile)

    except IOError:
        print("File not found. Returning to main menu...\n")


def do_test(tf, vf):
    try:
        print("\nRunning text evaluation...\n")
        with open(tf, 'r') as textFile:
            print ("text found")
            with open(vf, 'r') as valueFile:
                print ("values found")
                EvaluateText.evaluate(textFile, valueFile)

    except IOError:
        print("File not found. Returning to main menu...\n")



def evaluate():
    text = input("Text file: ")
    print("")

    try:
        print("Running text evaluation...\n")
        with open("./data/" + text, 'r') as textFile:
            EvaluateText.evaluate(textFile)

    except IOError:
        print("File not found. Returning to main menu...\n")


def gui():
    window = GUI.Evaluator()


def printInfo():
    print("\n°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,", "INFORMATION", ",¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°º¤ø\n")
    print("EmotionDetection v1, sentiment analysis system operating off a multinomial")
    print("Naive Bayes classififer. There are 13 possible labels that text can be")
    print("labelled as, the emotions are :empty, sadness, enthusiasm, neutral, worry,")
    print("surprise, love, fun, hate, happiness, boredom, relief and anger.\n")
    print("1. Training      - Generates a WordMap using a text file and emotion value file.")
    print("                   A word map is required for both testing and evaluation.\n")
    print("2. Testing       - Run the system and test its accuracy by supplying correct ")
    print("                   emotion values. Also produces reports and confusion plot\n")
    print("3. Evaluate Text - Run the system without given values. Used to evaluate input ")
    print("                   file that has not been pre-labelled.")
    print(78 * "-", "\n")
    input("Press enter to return to menu...\n")


main()

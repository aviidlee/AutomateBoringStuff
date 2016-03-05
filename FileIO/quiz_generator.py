#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.   
# Modified from Al Sweigar't book: https://automatetheboringstuff.com/chapter8/

import random
import sys
import os
import importlib

def generate_quizzes(dataDict, numQuizzes):
    '''Generate numQuizzes quizzes with questions randomly ordered from dataDict.

    params:
        dataDict dictionary contains quiz question and answer
        numQuizzes int the number of quizzes to generate 

    returns:

    '''
    # 
    
    quizItems = dataDict.items()
    questionsPerQuiz = 20

    for quizNo in range(numQuizzes):
        random.shuffle(quizItems)
        quizFile = open('quiz-' + str(quizNo), 'w')
        answerFile = open('answers-' + str(quizNo), 'w')

        for question in range(questionsPerQuiz):
            quizFile.write(quizItems[question][0] + '\n')
            answerFile.write(quizItems[question][1] + '\n')

        quizFile.close()
        answerFile.close()

    return

if __name__ == '__main__':
    helpMessage = "Usage: python quiz_generator.py <data dictionary> <num quizzes>"
    
    if(len(sys.argv) != 3):
        print helpMessage
    else:
        try:
            dataDict = importlib.import_module(sys.argv[1])
            if(type(dataDict.quizData) != type({})):
                print "Data was not a dictionary."
                sys.exit()

            generate_quizzes(dataDict.quizData, int(sys.argv[2]))

        except ImportError:
            print "Could not import dictionary; did you specify the full path?"
            sys.exit()

        except AttributeError:
            print "{} must contain a dictionary called quizData.".format(sys.argv[1])
            sys.exit()

        except ValueError:
            print "The second argument ({}) must be the number of quizzes to generate.".format(sys.argv[1])
            sys.exit()


       




import functionsExp1 as functionsExp1
import sys

## Input Variables


# featureSet = int(sys.argv[1])
# startPerson = int(sys.argv[2])
# endPerson = int(sys.argv[3])
# place = str(sys.argv[4])
# typeDatabase = str(sys.argv[5])
# printR = bool(int(sys.argv[6]))
# shotStart = int(sys.argv[7])
# k = int(sys.argv[8])
# nameFile = place + '_FeatureSet_' + sys.argv[1] + '_startPerson_' + sys.argv[2] + '_endPerson_' + sys.argv[
#     3] + 'shotStart' + sys.argv[7]+ 'memmory' + sys.argv[8] + '.csv'
# randomSeed = 1
# expTimes = 50

# for shotStart in range(1,3):

featureSet = 1
startPerson = 36  # Cote 20-36,EPN 31-60, Nina5 1-10
endPerson = 37  # Cote 20-36,EPN 31-60, Nina5 1-10
place = 'resultsExample/exampleE'
typeDatabase = 'EPN'
printR = 1
shotStart = 1
k = 1
randomSeed = 1
expTimes = 50

nameFile = place + '_' + typeDatabase + '_FeatureSet_' + str(featureSet) + '_startPerson_' + str(
    startPerson) + '_endPerson_' + str(endPerson) + 'shotStart' + str(shotStart) + 'memmory' + str(k) + '.csv'

# Upload Data
dataMatrix, _, _, classes, peoplePriorK, _, numberShots, _, allFeatures, _ = functionsExp1.uploadDatabases(
    typeDatabase, featureSet)

# Evaluation
functionsExp1.evaluation(dataMatrix, classes, peoplePriorK, featureSet, numberShots, nameFile, startPerson,
                         endPerson, allFeatures, typeDatabase, printR, k, shotStart, randomSeed, expTimes)

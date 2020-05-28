import re

def classify(inputTree, featLabels, testVec):
    firStr = list(inputTree.keys())[0]
    # 如果特征是数值型特征
    if '<=' in firStr:
        featValue = float(re.compile('<=.+').search(firStr).group()[2:])
        featKey = re.compile('.+<=').search(firStr).group()[:2]
        secondDict = inputTree[firStr]
        featIndex = featLabels.index(featKey)
        if testVec[featIndex]<=featValue:
            judge = 1
        else:
            judge = 0

        for key in secondDict.keys():
            if judge == int(key):
                if type(secondDict[key]).__name__=='dict':
                    classLabel = classify(secondDict, featLabels, testVec)
                else:
                   classLabel = secondDict[key]
    # 特征是类别性特征
    else:
        secondDict = inputTree[firStr]
        featIndex = featLabels.index(firStr)
        for key in secondDict.keys():
            if testVec[featIndex] == key:
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = classify(secondDict, featLabels, testVec)
                else:
                    classLabel = secondDict[key]
    return classLabel

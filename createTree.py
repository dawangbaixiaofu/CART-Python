from majorityCnt import majorityCnt
from chooseBestFeatureToSplit import chooseBestFeatureToSplit
from SplitCatoDataSet import SplitDataSet

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeatIndex = chooseBestFeatureToSplit(dataSet=dataSet, labels=labels)
    bestFeatLabel = labels[bestFeatIndex]

    myTree = {bestFeatLabel:{}}

    featValues = [example[bestFeatIndex] for example in dataSet]
    uniqueValues = set(featValues)

    del labels[bestFeatIndex]

    for value in uniqueValues:
        subDataSet = SplitDataSet(dataSet=dataSet, axis= bestFeatIndex, value=value)
        myTree[bestFeatLabel][value]=createTree(dataSet=subDataSet, labels=labels)
    
    return myTree

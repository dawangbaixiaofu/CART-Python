from SplitContinuous import SplitContinuousDataSet
from SplitCatoDataSet import SplitDataSet
from Gini import calcGini

def chooseBestFeatureToSplit(dataSet,labels):
    """
    :param dataSet:np.array
    :param labels: features type is a list
    :return: bestFeature int
    """
    bestFeature = -1
    numFeatures = len(dataSet[0])-1
    bestGiniIndex = 10000.0
    bestSplitDict = {}
    # bestSplitDict[feature_label]=切分点值
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
    #     对连续型特征进行处理
        if type(featList[0]).__name__ == 'float' or type(featList[0]).__name__ == 'int':
            sortfeatList = sorted(featList)
            # 产生n-1个候选划分点
            splitList = []
            for j in range(len(sortfeatList)-1):
                splitPoint = (sortfeatList[j]+sortfeatList[j+1])/2.0
                splitList.append(splitPoint)

            bestSplitGini = 10000
            slen = len(splitList)
            # 对每一个切分点对数据集进行切分，并计算切分后数据集的基尼系数，寻找特征最优切分点
            # 用到前面写的切分函数
            for j in range(slen):
                value = splitList[j]
                newGiniIndex = 0.0
                subDataSet0 = SplitContinuousDataSet(dataSet, axis=i, value=value, direction=0)
                subDataSet1 = SplitContinuousDataSet(dataSet, axis=i, value=value, direction=1)
                proba0 = len(subDataSet0)/float(len(dataSet))
                newGiniIndex += proba0*calcGini(subDataSet0)
                proba1 = len(subDataSet1)/float(len(dataSet))
                newGiniIndex += proba1*calcGini(subDataSet1)

                if newGiniIndex < bestSplitGini:
                    bestSplitGini = newGiniIndex
                    bestSplit = j
            # 使用字典记录特征i 对应的最佳切分点
            bestSplitDict[labels[i]] = splitList[bestSplit]
            GiniIndex = bestSplitGini
         # 对离散型特征进行计算Gin系数
        else:
            uniqueValues = set(featList)
            newGiniIndex = 0
            # 计算每种特征下Gini系数
            for value in uniqueValues:
                subDataSet = SplitDataSet(dataSet, axis=i, value=value)
                proba = len(subDataSet)/float(len(dataSet))
                newGiniIndex += proba*calcGini(subDataSet)
            GiniIndex = newGiniIndex

        if GiniIndex < bestGiniIndex:
            bestGiniIndex = GiniIndex
            bestFeature = i
    # 若当前节点的最佳划分特征为连续特征，则将其以之前记录的划分点为界进行二值化处理
    # 即是否小于等于bestSplitValue
    # 并将特征名改为 name<=value的格式
    if type(dataSet[0][bestFeature]).__name__ == 'float' or type(dataSet[0][bestFeature]).__name__=='int':
        bestSplitValue = bestSplitDict[labels[bestFeature]]
        labels[bestFeature] = labels[bestFeature]+'<='+str(bestSplitValue)
        for i in range(dataSet.shape[0]):
            if dataSet[i][bestFeature] <= bestSplitValue:
                dataSet[i][bestFeature] = 1
            else:
                dataSet[i][bestFeature] = 0

    return bestFeature
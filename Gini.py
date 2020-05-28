
def calcGini(dataSet):
    """

    :param dataSet: np.array,最后一列是对应的应变量
    :return: gini
    """
    gini = 1
    # 给所有可能的分类 创建字典
    labelCounts = {}
    # dataSet 数据类型是np.array
    for row in dataSet:
        currentLabel = row[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1

    total_rows = len(dataSet)
    for label in labelCounts.keys():
        proba = labelCounts[label]/total_rows
        gini -= proba
    return gini

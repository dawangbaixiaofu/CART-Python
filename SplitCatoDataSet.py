def SplitDataSet(dataSet, axis, value):
    # dataSet type is np.array
    # axis对应的特征是类别型特征
    retDataSet = []
    for row in dataSet:
        if row[axis] == value:
            reduceVec = row[:axis]
            reduceVec.extend(row[axis+1:])
            retDataSet.append(reduceVec)
    return retDataSet
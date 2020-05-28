def SplitContinuousDataSet(dataSet,axis,value,direction):
    """

    :param dataSet: np.array
    :param axis: feature
    :param value: split value
    :param direction: 0 refer to > and 1 refer to <=
    :return:
    """
    retDataSet = []
    for row in dataSet:
        if direction == 0:
            if row[axis]>value:
                reduceVec = row[:axis]
                reduceVec.extend(row[axis+1:])
                retDataSet.append(reduceVec)
        else:
            if row[axis]<=value:
                reduceVec = row[:axis]
                reduceVec.extend(row[axis+1:])
                retDataSet.append(reduceVec)
    return retDataSet
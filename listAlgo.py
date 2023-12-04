def groupBy():
    return int( input("Enter number to group by: ") )

def listLen( plainList ):
    listSize = 0
    for items in plainList:
        listSize += 1
    return listSize

def emptyList(listLen, numberOfGroups):
    template = []
    groupsDone = 0
    while groupsDone <= numberOfGroups:
        template.append([])
        groupsDone += 1
    return template

def newlist(listOne,groupSize):

    groupsDone = 0
    newlist = []
    counter = 0

    listLength = listLen( listOne )
    numberOfGroups = ( listLength // groupingSize )
    lastSize = ( listLength % groupingSize )

    template = emptyList(listLength, numberOfGroups)

    for items in listOne:
        
        if groupsDone <= numberOfGroups and counter <= groupSize:
            template[groupsDone].append(items)
            counter += 1

        if groupsDone <= numberOfGroups and counter == groupSize:
            counter = 0
            groupsDone += 1

    if lastSize == 0:
       del template[numberOfGroups]
    else:
        newlist = template
       
    return template

def getList():
    ungroupedList = []
    item = input("Enter an [item or end] when done: ")
    while item != "end":
        ungroupedList.append(item)
        item = input("Enter an [item or end] when done: ")

    return ungroupedList

     
listOne = [1,2,3,4,5,6,1]
groupingSize = groupBy()
ouputlist = newlist(listOne,groupingSize)

print( listOne )
print( ouputlist )

#second test
listOne = getList()
groupingSize = groupBy()
ouputlist = newlist(listOne,groupingSize)

print( listOne )
print( ouputlist )

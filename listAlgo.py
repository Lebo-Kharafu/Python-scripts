listOne = [1,2,3,4,5,6,1]
listTwo = []
groupingSize = 3


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

def newlist(template,listOne,numberOfGroups,groupSize,lastSize):

    groupsDone = 0
    newlist = []
    counter = 0

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
     

listLength = listLen( listOne )
numberOfGroups = ( listLength // groupingSize )
lastSize = ( listLength % groupingSize )

listTwo = emptyList(listLen, numberOfGroups)
listTwo = newlist(listTwo,listOne,numberOfGroups,groupingSize,lastSize)
    


print( listOne )
print( listTwo )

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:31:48 2017
sortify
@author: Riley
"""

#insertion sort algorithm

def insertionSort(myList):
    #assume first element is sorted
    #set sorted sentinel to 1
    operations=len(myList)
    sentinel=1
    #repeat until sentinel = len(myList)
    #for i in range(4):
    while sentinel<operations:
         #grab element at sorted sentinel
        value=myList.pop(sentinel)
        #iterate through elements before sentinel, insert before element that is bigger
        notBroke=True
        for f in range(sentinel):
            if myList[f]>value:
                myList.insert(f,value)
                notBroke=False
                break
        if notBroke:
            #don't fix it
            myList.append(value)
        sentinel+=1
    return myList

def insertionSortSegment(myList,segStart,segLen):
    listLeng=len(myList)
    #assume first element is sorted
    #set sorted sentinel to 1
    operations=segLen
    sentinel=1
    #repeat until sentinel = len(myList)
    #for i in range(4):
    while sentinel<operations:
        #grab element at sorted sentinel
        if sentinel+segStart==listLeng:
            break
        value=myList.pop(sentinel+segStart)
        #iterate through elements before sentinel, insert before element that is bigger
        notBroke=True
        for f in range(sentinel):
            if myList[f+segStart]>value:
                myList.insert(f+segStart,value)
                notBroke=False
                break
        if notBroke:
            #don't fix it
            myList.insert(segStart+segLen,value)
        sentinel+=1
    return myList

def gapSort(myList,gap):
    for i in range(0,len(myList),gap):
        insertionSortSegment(myList,i,gap)
    return myList

def shellSort(myList):
    myList=gapSort(myList,5)
    myList=gapSort(myList,3)
    myList=insertionSort(myList)
    return myList
        
#inputList=[89, 23, 33, 45, 10, 12, 45, 45, 45]
inputList=[67, 45, 2, 13, 1, 998]
#print (insertionSortSegment(inputList,3,3))
print (shellSort(inputList))
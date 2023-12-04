"""
    This program is use to Print out the times time table for user specific rows and colum 
"""

#Varilbes 
iTableRows = int( input("How many rows do you want: ") )
iTableCols = int( input("How many colums do you want: ") )


'''#iProduct = 0 # Stores each Product'''
iFinLen = len( str(iTableRows * iTableCols) ) #Idenfies the the largest digit len
'''#iProdlen = len( str(iProduct) ) # Identifies the len of each product'''

iMultiStart = 0 
iMutiLen = len( str(iMultiStart) + "x")
space = ' ' * ( (len( str(iTableRows) + "x" ) - iMutiLen) )
sLine = space + str(iMultiStart) + "x" 

iX = 0 # While loop controller
i = 0

niMutiLen = len( str(i) )
nspace = ' ' * ( (len( str(iTableCols) + "x" ) - niMutiLen) )
fLine = nspace + "x"


# The functionals loop to display


#The excecution of the program
while(iMultiStart <= iTableRows):
    if i <= 0 :
        while(i <= iTableCols ):
            niMutiLen = len( str(i) + "x" )
            nspace = ' ' * ( (iFinLen - niMutiLen) )
            if( space == '' and i <= 3):
                space = ' '
            fLine = fLine + '|' + nspace + "x" + str(i) 
            i += 1
        print(fLine)
       
    while(iX <= iTableCols ):
        iProduct = iMultiStart * iX
        iProdlen = len( str(iProduct) )
        space = ' ' * ( (iFinLen - iProdlen) )
        if( space == '' and iX <= 3):
           space = ' '
        sLine = sLine + '|' + space + str(iProduct) 
        iX += 1
        
    print(sLine)
    iMultiStart += 1
    iMutiLen = len( str(iMultiStart) + "x")
    space = ' ' * ( (len( str(iTableRows) + "x" ) - iMutiLen) )
    sLine = space + str(iMultiStart) + "x"
    iX = 0

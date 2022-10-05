import sys, os
from planning import planning_hour, planning_day
from PIL import Image

def checkFile(file1, file2):
    if not os.path.isfile(file1):
        print (file1+" is not a file")
        sys.exit(1)
    if not os.path.isfile(file2):
        print (file2+" is not a file")
        sys.exit(1)

#order the 2 screenshots to retrieve : the older, the newer
#this order is needed to notify about an added, deleted or substituted lecture
def selectFileFromTitle(file1, file2):
    checkFile(file1, file2)
    name1_l = str(file1).split("_")
    name2_l = str(file2).split("_")
    
    if(name1_l[2] > name2_l[2]): #file1 have greater year than file2
        readFile(file2, file1)
    elif (name1_l[2] < name2_l[2]):
        readFile(file1, file2)
    else:
        if(name1_l[1] > name2_l[1]): #file1 have greater month than file2
            readFile(file2, file1)
        elif (name1_l[1] < name2_l[1]):
            readFile(file1, file2)
        else:
            if(name1_l[0] > name2_l[0]): #file1 have greater day than file2
                readFile(file2, file1)
            elif (name1_l[0] < name2_l[0]):
                readFile(file1, file2)
            else:
                if(name1_l[3] > name2_l[3]): #file1 have greater hour than file2
                    readFile(file2, file1)
                elif (name1_l[3] < name2_l[3]):
                    readFile(file1, file2)
                else:
                    if(name1_l[4] > name2_l[4]): #file1 have greater second than file2
                        readFile(file2, file1)
                    elif (name1_l[4] < name2_l[4]):
                        readFile(file1, file2)
                    else:
                        if(name1_l[5] > name2_l[5]): #file1 have greater millisecond than file2
                            readFile(file2, file1)
                        elif (name1_l[5] < name2_l[5]):
                            readFile(file1, file2)
                        else:
                            sys.exit("Files have the same title !")

#pixel comparison between 2 screenshots to retrieve planning modification
def readFile(file1, file2):
    image1 = Image.open(file1, 'r') #older screenshot
    image2 = Image.open(file2, 'r') #newer screenshot

    lenDay = len(planning_day)
    lenHour = len(planning_hour)

    #(x,y) = (row, line)
    cpt = 0
    for x in range(lenDay):
        for y in range(lenHour):
            (r1,v1,b1) = image1.getpixel((planning_day[x]["row"],planning_hour[y]["line"]))
            (r2,v2,b2) = image2.getpixel((planning_day[x]["row"],planning_hour[y]["line"]))

            #change
            if((r1,v1,b1) != (r2,v2,b2)):
                cpt+=1

                #get change type
                # + : add
                # - : remove
                # <=> : substitution
                if((r1,v1,b1) == (217,219,220)):
                    print("Change "+str(cpt)+" (+)")
                elif((r2,v2,b2) == (217,219,220)):
                    print("Change "+str(cpt)+" (-)")
                else:
                    print("Change "+str(cpt)+" (<=>)")


                #get day/hour for each change
                for i in range(len(planning_day)):
                    if(planning_day[x]["row"] == planning_day[i]["row"]):
                        print(planning_day[i]["day"])
                        
                for i in range(len(planning_hour)):
                    if(planning_hour[y]["line"] == planning_hour[i]["line"]):
                        print(planning_hour[i]["hour"])

                print("")
                
    if(cpt == 0):
        print("Nothing has changed")

    #delete the older screenshot
    os.remove(file1)

#first function to be called
def getNumberOfPNG():
    list_d = os.listdir('./images/')
    list_f = []
    #get files from images directory
    for x in list_d:
        if os.path.isfile(x):
            list_f.append(x)

    if(len(list_f) == 2):
        selectFileFromTitle(list_f[0], list_f[1])
    elif(len(list_f) > 2):
        print("more than 2 screenshots. The 2 first will be compared.")
        selectFileFromTitle(list_f[0], list_f[1])
    else:
        print("2 screenshots are needed to be compared. Launch the bot.")


#start the project
getNumberOfPNG()
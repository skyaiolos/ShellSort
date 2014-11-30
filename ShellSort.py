
def shellSort(list):
    gap = len(list) // 2
    #gap = 1
    while gap > 0:
        for i in range(gap, len(list)):
            var = list[i]
            j = i
            while j >= gap and list[j - gap] > var:
                list[j] = list[j - gap]
                j -= gap
            list[j] = var
        gap //= 2
        #print gap


if __name__=="__main__":                 
    import sys
    import string
    import time
    import random

    outFile = open("ShellTime.txt", "a+")
    
    size = map(int,sys.argv[1:])

    #list = [5] * size[0]
    
    list = random.sample(range(9999999),size[0])

    #print string.join(map(str,list))

    #shellSort(list)
    
    startTime = time.clock()
    shellSort(list)
    #print string.join(map(str,list))

    print(time.clock() - startTime)

    outFile.write(str(size[0]))
    outFile.write(",")
    outFile.write(str(time.clock()-startTime))
    outFile.write("\n")
    

    


                

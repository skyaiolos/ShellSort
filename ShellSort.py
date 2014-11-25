
 def shellSort(list):
     gap = len(list) // 2
     while gap > 0:
         for i in range(gap, len(list)):
             val = list[i]
             j = i
             while j >= gap and list[j - gap] > val:
                 list[j] = list[j - gap]
                 j -= gap
             list[j] = val
         gap //= 2


if __name__=="__main__":                 
    import sys
    import string
    import time
    import random

    outFile = open("ShellTime.txt", "a+")

    startTime = time.clock()
    
    size = map(int,sys.argv[1:])
    
    list = random.sample(range(9999999),size[0])

    #print string.join(map(str,list))

    #print string.join(map(str,list))

    print(time.clock() - startTime)

    outFile.write(str(size[0]))
    outFile.write(",")
    outFile.write(str(time.clock()-startTime))
    outFile.write("\n")
    

    


                

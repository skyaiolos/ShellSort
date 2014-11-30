
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


def partition(list, p, r):
    q = list[r]             #pivot definition                      
    bot = p-1                           
    top = r
    woot = 0
    
    while not woot:                            

        while not woot:                        
            bot = bot+1                  

            if bot == top:                  
                woot = 1                      
                break

            if list[bot] > q:           
                list[top] = list[bot]     
                break                          

        while not woot:                        
            top = top-1                        
            
            if top == bot:                  
                woot = 1                       
                break

            if list[top] < q:              
                list[bot] = list[top]      
                break                          

    list[top] = q                         
    return top

def quickSort(list, p, r, t):
    
    if p < r:  
        split = partition(list, p, r)
        quickSort(list, p, split-1, t)       
        quickSort(list, split, r, t)
    else:
        return

if __name__=="__main__":                 
    import sys
    import string
    import time
    import random

    outFile = open("QuickTime.txt", "a+")

    size = map(int,sys.argv[1:])

    list = [5] * size[0]
    
    #list = random.sample(range(9999999),size[0])

    #print string.join(map(str,list))
    
    startTime = time.clock()

    p = 0
    r = len(list)-1
    
    quickSort(list,p,r, "only 1 thread")

    #print string.join(map(str,list))

    print(time.clock() - startTime)

    outFile.write(str(size[0]))
    outFile.write(",")
    outFile.write(str(time.clock()-startTime))
    outFile.write("\n")
    

    


                

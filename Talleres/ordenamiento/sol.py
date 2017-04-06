nums = int(raw_input())

while(nums!=0):
    entrada = raw_input().strip().split()
    print entrada

    for i in entrada: print sorted(i)
    #print(sorted(entrada)[0])

    nums = int(raw_input())

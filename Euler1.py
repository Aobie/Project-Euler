import time

def list_of_multiples_below(n):
    multipleslist = []
    limit = int (n / 3)
    for x in range (1, limit + 1):
        if x * 3 < n and x % 5:
            multipleslist.append(x * 3)
        if x * 5 < n:
            multipleslist.append(x * 5)
    else:
        return multipleslist
        
def sum_list():
    t1 = time.time()
    mylist = list_of_multiples_below(1000)
    answer = sum(mylist)
    t2 = time.time()
    tfinal = (t2 - t1) * 1000.0
    print (tfinal, " ms")
    return answer

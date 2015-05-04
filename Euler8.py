def find_max_product(n):
    dictionary = "73167176531330624919225119674426574742355349194934"
    dictionary += "96983520312774506326239578318016984801869478851843"
    dictionary += "85861560789112949495459501737958331952853208805511"
    dictionary += "12540698747158523863050715693290963295227443043557"
    dictionary += "66896648950445244523161731856403098711121722383113"
    dictionary += "62229893423380308135336276614282806444486645238749"
    dictionary += "30358907296290491560440772390713810515859307960866"
    dictionary += "70172427121883998797908792274921901699720888093776"
    dictionary += "65727333001053367881220235421809751254540594752243"
    dictionary += "52584907711670556013604839586446706324415722155397"
    dictionary += "53697817977846174064955149290862569321978468622482"
    dictionary += "83972241375657056057490261407972968652414535100474"
    dictionary += "82166370484403199890008895243450658541227588666881"
    dictionary += "16427171479924442928230863465674813919123162824586"
    dictionary += "17866458359124566529476545682848912883142607690042"
    dictionary += "24219022671055626321111109370544217506941658960408"
    dictionary += "07198403850962455444362981230987879927244284909188"
    dictionary += "84580156166097919133875499200524063689912560717606"
    dictionary += "05886116467109405077541002256983155200055935729725"
    dictionary += "71636269561882670428252483600823257530420752963450"
    
    answer = 0
    for x in range(len(dictionary) - n):
        temp = int (dictionary[x])
        for i in range(1, n):
            temp *= int(dictionary[x + i])
        else:
            if temp > answer:
                answer = temp
            temp = 0
    else:
        return answer
        
if __name__ == "__main__":
    print("Problem 8")
    print("Find the largest product of 13 consecutive digits of a large string of numbers.")
    answer = find_max_product(13)
    print(answer)
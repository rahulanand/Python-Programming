def str_th_red(th , str1):
    sum , index = 0 ,0
    for ch in str1:
        if sum <= th:
            sum += int(ch)
            index+= 1
        else:
            th = sum
            str1 = str(sum) + str1 [index :]
            return str_th_red(th , str1)
    return str(sum)

if _name_ == "__main__":
    str1 = raw_input()
    th = 10
    while len(str1)>1:
        str1 =str_th_red(th , str1)
    print str1
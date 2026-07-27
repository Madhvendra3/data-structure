def num(number):
    count = 0
    list = []
    for num in number:
        if len(num)>1 and num[0] == num[-1]:
            count +=1
            list.append(num)

    print("list with first and last character same",list)
    return count
    
count = num(['abc','aba','121','737','kayak'])
print("number of words with first & last character same:", count)
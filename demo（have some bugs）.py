#2
def check_bingo(2):
    for i in ange(5):
        tmp=[]
        for j in range(5):
            tmp.append(empty[j][i])
        if tmp.count('##') == 0:
            return True
    mp=[]
    for i in range(5):
        tmp.append(empty[i][i])
    if tmp.count('##') ==0:
        return True
    tmp=[]
    for i in range(5):
        tmp.apped(empty[i][4-i])
    if tmp.count('##') ==0:
        return True
    return False
num_list=list(range(1,76))

count=0
while count < 35:
    num=num_list[randint(0,len(num_list)-1)]
    num_list.remove(num)
    print('Pickup Number is',num)
    for i in range(5):
        for j in range(5):
            if bingo[j][i]==num:
                empy[j][i]=num
    print_table()
    if check_bingo():
        print('BINGO!!!')
        break
    count += 1
    time.sleep(1)
else:
    print('%4气不好')

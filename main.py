
from base64 import encode


def myLoto3():
    num = 782
    textNum = str(num)
    numLv1 = []
    numlv2 = []
    ### handle with level-1 by suffle last 2 digit number.
    numLv1.append(textNum[0:1]+textNum[1:2])
    numLv1.append(textNum[1:2] + textNum[0:1])
    endnum = textNum[-1]
    
    # print(numLv1)
    # print(endnum)
    for i in range(2):
        # print(i)
        numlv2 = [x for x in numLv1[i]]
        # print(numlv2)
        print(endnum+numlv2[0]+numlv2[1]+" "+numlv2[0]+endnum+numlv2[1]+" "+numlv2[0]+numlv2[1]+endnum)
        pass
    pass

def myLoto4():
    total = []
    get_fetch = []
    get_input = ["1234","5678"]
    
    
    for gInput in get_input:
        s_fomula_1 = gInput
        s_fomula_2 = gInput[1] + gInput[0] + gInput[2] + gInput[3]
        s_fomula_3 = gInput[2] + gInput[0] + gInput[1] + gInput[3]
        s_fomula_4 = gInput[3] + gInput[0] + gInput[1] + gInput[2]
        
        get_fetch.append(s_fomula_1)
        get_fetch.append(s_fomula_2)
        get_fetch.append(s_fomula_3)
        get_fetch.append(s_fomula_4)
    # print(get_fetch)
    for f in get_fetch:
        current_Value = f
        s1 = current_Value
        s2 = current_Value[0]+current_Value[1]+current_Value[3]+current_Value[2]
        s3 = current_Value[0]+current_Value[2]+current_Value[1]+current_Value[3]
        s4 = current_Value[0]+current_Value[2]+current_Value[3]+current_Value[1]
        s5 = current_Value[0]+current_Value[3]+current_Value[1]+current_Value[2]
        s6 = current_Value[0]+current_Value[3]+current_Value[2]+current_Value[1]
        total.append([s1,s2,s3,s4,s5,s6])
    for num in total:
        print(num)
    pass

    


def myLoto4Couple():
    total = []
    get_fetch = []
    get_input = ["01212604"]
    total_Str = ""
    
    for gInput in get_input:
        print('START')
        print(gInput)
        print(gInput[2:4])
        s_fomula_1 = gInput
        s_fomula_2 = gInput[2:4] + gInput[0:2] + gInput[4:6] + gInput[6:]
        s_fomula_3 = gInput[4:6] + gInput[0:2] + gInput[2:4] + gInput[6:]
        s_fomula_4 = gInput[6:] + gInput[0:2] + gInput[2:4] + gInput[4:6]
        
        get_fetch.append(s_fomula_1)
        get_fetch.append(s_fomula_2)
        get_fetch.append(s_fomula_3)
        get_fetch.append(s_fomula_4)
    print(get_fetch)
    for f in get_fetch:
        current_Value = f
        s1 = current_Value
        s2 = current_Value[0:2]+current_Value[2:4]+current_Value[6:]+current_Value[4:6]
        s3 = current_Value[0:2]+current_Value[4:6]+current_Value[2:4]+current_Value[6:]
        s4 = current_Value[0:2]+current_Value[4:6]+current_Value[6:]+current_Value[2:4]
        s5 = current_Value[0:2]+current_Value[6:]+current_Value[2:4]+current_Value[4:6]
        s6 = current_Value[0:2]+current_Value[6:]+current_Value[4:6]+current_Value[2:4]
        total.append([s1,s2,s3,s4,s5,s6])
    for nums in total:
        print(nums)
        for num in nums:
            total_Str +=  f"{num}\n"
            
    with open("Double4_animal.txt", mode="w", encoding='utf-8') as Db_animal:
        Db_animal.write("ຜົນລັບຂອງການສະຫລັບໂຕເລກນາມສັດ\n" + total_Str)
    pass

myLoto4Couple()
# TODO решите задачу
def task() -> float:

    numb1 = 0
    numb2 = 0
    sum_values = 0
    file_ = open("input.json", "r")

    schit_str = file_.readlines()

    for i in range(len(schit_str)):
        if schit_str[i].find("score") != -1:
            numb1 = float(schit_str[i][((schit_str[i].find("score"))+8):len(schit_str[i])-2])

        elif (schit_str[i].find("weight")) != -1:
            numb2 = float(schit_str[i][((schit_str[i].find("weight"))+9):len(schit_str[i])-1])

        if(numb1 != 0) and (numb2 != 0):
            sum_values += numb1*numb2
            numb1 = 0
            numb2 = 0

    file_.close()

    return round(sum_values, 3)

print(task())

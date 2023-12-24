def BoubleSort(arr:list) -> list:
    for i in range(0, len(mass) - 1):
        for j in range(len(mass) - 1):
            if (mass[j] > mass[j + 1]):
                res = mass[j]
                mass[j] = mass[j + 1]
                mass[j + 1] = res



def Reverse(arr:list) -> list:
    pass



if __name__ == "__main__":
    mass = [1,2,9,3,8,23,9,228,3]
    mass = BoubleSort(mass)
    mass2 = Reverse(mass)
    mass.reverse()
    if mass == mass2:
        print("Ok")
    else:
        print("Not Work")

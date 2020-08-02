'''
Given array of numbers
can u get to 0 by summing or subtracting those numbers?

a=[1,2,3]
1+2-3 = 0
'''
 
def plusOrMinus(arr):
    res = plusOrMinus_(arr, 0)
    if res is None:
        print("Not possible")
    else:
        print(res, " = 0")

def plusOrMinus_(arr, target):
    if len(arr) == 0:
        return ""
    if len(arr) == 1 and arr[0] == target:
        return str(arr[0])
    if len(arr) == 1 and arr[0] != target:
        return None
    else:
        head = arr[-1]
        tail = arr[:-1]

        pos1 = plusOrMinus_(tail, target-head)
        pos2 = plusOrMinus_(tail, target+head)

        if pos1 is not None:
            return  pos1 + "+" + str(head)
        elif pos2 is not None:
            return pos2 + "-" + str(head)
        else:
            return None


plusOrMinus([1,2,3])
plusOrMinus([1,2,4])
plusOrMinus([3,4,15,1,2,15,5,15])
plusOrMinus([4,4,2,2,4])
plusOrMinus([4,1,2,2,4])



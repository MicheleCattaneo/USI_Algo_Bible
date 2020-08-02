
def hasEqualPartition(S):
    return partition(S, 0, "", "", 0, 0)

def partition(S, i, part1, part2, sum1, sum2):
    # if the end of the Sequence is reached, check if the sums are the same
    # return if the sum are the same and the 2 partitions Strings
    if i == len(S):
        return sum1 == sum2, part1 + "|" + part2

    else:
        head = S[i]
        i += 1

        # try adding the value to the first partition

        pos1 = partition(S,i, part1 +" "+ str(head), part2, sum1 + head, sum2)
        # try adding the value to the second partition
        pos2 = partition(S,i, part1, part2 +" "+ str(head), sum1, sum2 + head)

        # if one of the two possibilities returned True ( first returned value )
        # return also the two strings that represents it ( second returned value )
        if pos1[0]:
            return True, pos1[1]
        if pos2[0]:
            return True, pos2[1]
        # otherwise return False and None
        return False, None

def alternative(S):
    '''
    Alternatively you can sum the value of all elements, if it's odd, return false,
    otherwise use SubSetSum problem with the desired sum being total / 2
    '''
    pass



S1 = [3,1,1,2,2,1]
S2 = [3,3,3]
S3 = [1,5,8,15,9,10,7,15,-10]

print(hasEqualPartition(S1))
print(hasEqualPartition(S2))
print(hasEqualPartition(S3))

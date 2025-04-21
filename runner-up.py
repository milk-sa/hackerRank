if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(arr)
    uni_arr = list(arr_set)
    uni_arr.sort()
    
    print (uni_arr[-2])
        

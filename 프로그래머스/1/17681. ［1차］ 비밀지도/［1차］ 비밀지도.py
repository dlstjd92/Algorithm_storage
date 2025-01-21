def solution(n, arr1, arr2):
    answer = []
    
    def make_map(arr1):
        ret = []
        for i in arr1:
            temp_str=""
            while i>0:
                temp = i%2
                i = i//2
                temp_str = str(temp) + temp_str
            if len(temp_str) != n:
                while len(temp_str) != n:
                    temp_str = '0'+temp_str
            ret.append(list(temp_str))
        return ret
        
    map1 = make_map(arr1)
    map2 = make_map(arr2)
    ans = []
    for i in range(n):
        temp = ""
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                temp = temp + "#"
            else:
                temp = temp + " "
        ans.append(temp)
        
    return ans
        
    

    
    return answer
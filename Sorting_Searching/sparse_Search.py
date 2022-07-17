    
def binary_search(list_s, s):
    n = len(list_s)
    mid = n//2
    i = mid
    found = False
    if len(list_s)==0:
        return  -1
    if list_s[mid] == "":
        #move left
        while(i >= 0):
            if list_s[i] != "":
                mid = i
                found = True
                break
            i-=1
        i = mid
        if not found:
            while(i < n):
                if list_s[i] != "":
                    mid = i
                    found = True
                    break
                i+=1
        if not found:
            return -1
    if list_s[mid] == s:
        return mid
    if s > list_s[mid]:
        return mid + 1 + binary_search(list_s[mid+1:], s)
    else:
        return binary_search(list_s[:mid], s)
    

strs = ["at","","","","ball","","","cat","","","dad","","egg","","","food"]
res = binary_search(strs,"egg")
print(res)
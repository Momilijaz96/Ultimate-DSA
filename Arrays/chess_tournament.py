import numpy as np
def chessTournament(arr, n , c):
    #arr.sort()
    focus = abs(arr[-1] - arr[0])
    i = 0
    c -=2
    ass = [arr[0],arr[-1]]
    arr.pop(0)
    arr.pop(-1)
    while(i<c):
        #focus,ass,arr = binary_s(arr,focus,ass)
        focus,ass,arr = greedy_assign(arr,ass,focus)
        #print("Focus: ",focus)
        #print("Assigned: ",ass)
        #print("Arr: ",arr)
        i+=1
    return focus

def greedy_assign(arr,ass,curr_focus):
    room_focus = []
    overall_focus = []
    for r in arr:
        room_focus = []
        for a in ass:
            room_focus.append(abs(r-a))
        overall_focus.append(min(room_focus))
    #print("Overall: ",overall_focus)
    ass.append(arr[np.argmax(overall_focus)])
    arr.pop(np.argmax(overall_focus))
    focus = min(curr_focus,max(overall_focus))
    return focus,ass,arr

def binary_s(arr,focus,ass):
    mid = len(arr)//2
    diff = [abs(arr[mid]-d) for d in ass]
    if min(diff) > focus:
        ass.append(arr[mid])
        arr.pop(mid)
        focus = min(diff)
        return focus,ass,arr
    else:
        focus,ass,arr = binary_s(arr[mid:],focus,ass)
    return focus,ass,arr
    

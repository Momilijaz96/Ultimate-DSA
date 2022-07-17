def radix_sort(arr):
    n = len(arr)
    buckets = [[] for x in range(10)]
    md = len(str(max(arr)))
    
    for i in range(n):
        digit = arr[i]%10
        buckets[digit].append(arr[i])
    print(buckets)
    div = 10

    for _ in range(md-1):
        
        for bi in range(len(buckets)):
            bucket = buckets[bi]
            for i in range(len(bucket)):
                digit = (bucket[i]//div)%10
                if digit==bi: continue
                buckets[digit].append(bucket[i])
                bucket.pop(i)
                print(buckets)
            buckets[bi] = bucket
        div *= 10
    print(buckets)


x = [15, 11, 22 ,24,33,42,51]
print(radix_sort(x))



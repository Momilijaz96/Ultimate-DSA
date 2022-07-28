class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def heapify(self,root_idx=0):
        left_child = (2*root_idx) + 1
        right_child = (2*root_idx) + 2
        
        smallest = root_idx
        if left_child < len(self.heap) and self.heap[left_child]<self.heap[smallest]:
                smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]<self.heap[smallest]:
                smallest = right_child
        if smallest != root_idx:
            self.heap[smallest],self.heap[root_idx] = self.heap[root_idx],self.heap[smallest]
            self.heapify(smallest)
            
    def insertKey(self,x):
        self.heap.append(x)
        self.min_heapify()
        
    def min_heapify(self):
        i = len(self.heap) - 1
        parent = (i-1)//2
        
        while(i!=0 and self.heap[parent]>self.heap[i]):
                self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
                #self.heapify(parent)
                i = parent
                parent = (i-1)//2
                
    def getMin(self):
        return self.heap[0]
    
    def extractMin(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify()

    def deleteKey(self,key):
        for idx,k in enumerate(self.heap):
            if k==key:
                break
        self.heap[idx] = self.getMax() + 1
        self.heapify()
        self.extractMin()
    
    def updateKey(self,old_key,new_key):
        for idx,k in enumerate(self.heap):
            if k==old_key:
                break
        self.heap[idx] = new_key
        self.heapify()

def minHeap(N: int, Q: [[]]) -> []:
    heap = MinHeap()
    mins = []
    for q in Q:
        #print(heap.heap)
        if q[0]==0:
            heap.insertKey(q[1])
        else:
            mins.append(heap.getMin())
            heap.extractMin()
    #print(heap.heap)
    return mins    
 
    
    
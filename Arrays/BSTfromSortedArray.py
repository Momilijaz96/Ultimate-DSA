'''
    Following is the TreeNode class structure
'''
class TreeNode :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def make_bst(arr):
    if len(arr)==0:
        return None
    if len(arr)==1:
        return TreeNode(arr[0])
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    root.left = make_bst(arr[:mid])
    root.right = make_bst(arr[mid+1:])
    return root
    
def sortedArrToBST(arr, n):
    
    # Write your code here
    return make_bst(arr)
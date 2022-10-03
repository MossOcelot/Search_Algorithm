class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
    
    def addNode(self,other):
        if self.next:
            self.next.addNode(other)

        else:
            self.next = other
    
    def print_node(self):
        print(self.val)
        if self.next:
            self.next.print_node()

def sublist_search(first, second, first_full):
    if not first and not second:
        return True

    if not first or not second:
        return False

    return findList(first,second,first_full,0)

def findList(first, second,first_full,n = 0):

    if first.val == second.val:
        if first.next == None:
            return True
        elif second.next == None:
            return False
            
        return findList(first.next,second.next,first_full,1)
    else:
       
        if n == 0:
            return findList(first,second.next,first_full,0)
        else:
            return findList(first_full,second,first_full,1)

def auto_addNode(arr):
    for i in range(len(arr)):
        if i == 0:
            node = Node(arr[i])
        else:
            node.addNode(Node(arr[i]))

    return node

arr_f = [1,2,3,4,5]
arr2_f = [1,2,3]

first_all = auto_addNode(arr_f)
second_all = auto_addNode(arr2_f)


result = sublist_search(first_all,second_all,first_all)

if result:
    print("List Found")
else:
    print("List Not Found")

    

    
        
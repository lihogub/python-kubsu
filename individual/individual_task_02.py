def search(storage, src, dst):
    if src not in storage:
        return False
    elif storage[src] == dst:
        return True
    else:
        return search(storage, storage[src], dst)


# Input: N lines of <parent child>. K lines of <node1 node2>.
# Output: 1 if node1 is parent of node2, 2 if node2 is parent of node1, 0 otherwise
def task01():
    N = int(input("N: "))
    tree = {}
    for i in range(N):
        child, parent = input().split()
        tree[child] = parent
    K = int(input("K: "))
    for i in range(K):
        child, parent = input().split()
        if search(tree, child, parent):
            print(1)
        elif search(tree, parent, child):
            print(2)
        else:
            print(0)


task01()

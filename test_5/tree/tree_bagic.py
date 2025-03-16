

def pre_ord(node):
    preorder.append(node)

    if tree[node]:
        if len(tree[node]) > 0 and tree[node][0]:
            pre_ord(tree[node][0])
        if len(tree[node]) > 1 and  tree[node][1]:
            pre_ord(tree[node][1])


def in_ord(node):
    if len(tree[node]) > 0 and tree[node][0]:
        in_ord(tree[node][0])

    inorder.append(node)

    if len(tree[node]) > 1 and tree[node][1]:
        in_ord(tree[node][1])


def post_ord(node):
    if len(tree[node]) > 0 and tree[node][0]:
        post_ord(tree[node][0])

    if len(tree[node]) > 1 and tree[node][1]:
        post_ord(tree[node][1])

    postorder.append(node)

T = int(input())
ar = list(map(int, input().split()))
mx = max(ar)+2
tree = [[] for _ in range(mx)]

for i in range(0, len(ar), 2):
    tree[ar[i]].append(ar[i+1])

preorder = []
inorder = []
postorder = []


pre_ord(1)
in_ord(1)
post_ord(1)
print(*preorder)
print(*inorder)
print(*postorder)

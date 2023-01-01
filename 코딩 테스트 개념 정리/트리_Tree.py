# Tree
# -->> Tree는 서로 연결된 Node의 계층형 자료구조로써, root와 부모-자식 관계의 subtree로 구성되어 있습니다.

# Tree 관련 개념
# * 노드(Node) : 트리는 보통 노드로 구현됩니다.
# * 간선(Edge) : 노드간에 연결된 선
# * 루트 노드(Root) : 트리는 항상 루트에서 시작합니다.
# * 리프 노드(Leef) : 더이상 뻗어나갈 수 없는 마지막 노드
# * 자식 노드(Child), 부모 노드(Parent), 형제 노드(Sibling)
# * 차수(degree) : 각 노드가 갖는 자식의 수. 모든 노드의 차수가 n개 이하인 트리를 n진 트리라고 합니다.
# * 조상(ancestor) : 위쪽으로 간선을 따라가면 만나는 모든 노드
# * 자손(descendant) : 아래쪽으로 간선을 따라가면 만나는 모든 노드
# * 높이(height) : 루트노드에서 가장 멀리 있는 리프 노드 까지의 거리. 즉 리프 노드 중에서 최대 레벨 값.
# * 서브트리(subtree) : 트리의 어떤 노드를 루트로 하고, 그 자손으로 구성된 트리를 subtree라고 한다.

# 이진 트리 : Binary Tree
# Binary Tree
# -->> "Complete Binary Tree"

# (Binary Tree를 구성하는) Node
"""
class Node:
  def __init__(self):
    self.value = 0
    self.left_child = None
    self.right_child = None
"""

# (Node)를 이용해 구현한 Binary Tree
class Node:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

class BinaryTree:
    def __init_(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)
bt.root.right.left = Node(value = 6)

# 너비 우선 탐색 (Breadth-first search, BFS)

# 트리 순회 Traversal
# -->> "트리 순회(Traversal)"란 트리 탐색(search)이라고도 불리으며 트리의 각 노드를 방문하는 과정을 말한다.
# 모든 노드를 한 번씩 방문 해야 하므로 -->> '완전 탐색'이라고도 불린다.
# 순회 방법으로는 "너비 우선 탐색의 BFS"와 "깊이 우선 탐색의 DFS"가 있다.

# 너비 우선 탐색 Breadth-first Search
# BFS

from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return []
    q = deque() # '우선순위 큐'를 쓰기위한 덱 자료구조 변수 q의 선언. <<-- 여기까지가 BFS의 초기 셋팅입니다..!!
    q.append(root) # -->> * '큐에 들어간다'라는 의미는 해당 노드에 (앞으로) 방문(접근)할 예정이라는 뜻입니다..!!
    while q: # <<-- 방문할 예정인 노드가 남아있다면 while문을 진행하면 됩니다..!!      # * '큐에서 나온다'라는 의미는 해당 노드에 ''접근''('방문')하였다는 의미입니다..!!
        cur_node = q.popleft() # 큐에서 노드 하나를 꺼내어 -->> 해당 노드에 접근.
        visited.append(cur_node.value) # 해당 노드에 방문. -->> 방문의 표시를 남기기 위해 visited 리스트(배열)에 해당 노드 value값을 append하여 일종의 방명록을 남기고 있습니다..!!

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

print(bfs(bt.root))
# 출력결과로 '[1,2,3,4,5,6]'이 잘 나오는 것을 확인하실 수 있을 것입니다..!!
# 참고> '트리(그래프)의 순회'에 있어서 노드의 '접근'과 노드의 '방문'은 다른 의미입니다..!!
# 즉, '접근'은 여러번 할 수 있으나 '방문'은 딱 한번만 이뤄져야 합니다..!!

# 깊이 우선 탐색 (Depth-first Search, DFS)
# DFS의 구현 방법에는 크게 2가지가 있는데, -->> 1. 첫번째는 스택을 이용해서 구현하는 방법이고  2. 나머지 하나는 재귀(Recursion)을 이용해서 구현하는 방법입니다..!!
# 참고> 재귀를 이용하여 DFS를 구현하면 이해하기 쉽고, 실제로 코딩 테스트에서 재귀를 이용한 DFS를 많이 이용한다고 합니다..!!

# DFS by recursion
# (ex) .... 접근 순서 : A, B, D, G, D, H, D, B, E, B, A, C, F, C, A
# 즉, 한 길을 파고들고 나오고 이런식으로 접근을 합니다..!!

# DFS
"""
def dfs(root): # root 노드에 접근.
    if root is None: # base case : 재귀적으로 소스코드를 짜는데 있어서 없어서 안될 부분입니다..!!
        return
    # root 노드의 방문. : root 노드에 접근해서 어떤 행동을 한다. -->> (ex) print(root.value)
    dfs(root.left) # By using recursion ....
    dfs(root.right) # By using recursion ....

dfs(bt.root) # 이 행의 의미 : root만 나한테 줘. 그러면 root가 가리키는 Tree에 속한 모든 노드를 접근해 줄께
""" 

# DFS 즉, 깊이 우선 탐색에 있어서 방문을 언제할 것이냐에 따라서 3가지로 구분됩니다..!!

# 전위 순회(Preorder), 중위 순회(Inorder), 후위 순회(Postorder)

# DFS (# 참고> DFS에 있어서 ""방문 순서""에 따라 크게 3가지로 나뉩니다. -->> 1. 전위 순회, 2. 중위 순회, 3. 후위 순회)
# 전위 순회(preorder)
# 중위 순회(inorder)
# 후위 순회(postorder)

# 전위 순회
# preorder
def preorder(cur_node): # 루트 노드의 방문순서가 우선인 case
    if cur_node is None:
        return
    
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

preorder(bt.root)
print('\n')

# 중위 순회 : 루트 노드의 방문순서가 중간인 case
# inorder
def inorder(cur_node):
    if cur_node is None:
        return
    
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

inorder(bt.root)
print('\n')

# 후위 순회 : 루트 노드의 방문순서가 마지막인 case
# postorder
def postorder(cur_node):
    if cur_node is None:
        return
    
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)

postorder(bt.root)

# 참고> -->> "즉, 정리하자면 전위순회, 중위순회, 후위순회 모두 접근 순서는 같지만 루트 노드를 언제 방문하느냐에 따라서 구분되는 것입니다..!!"

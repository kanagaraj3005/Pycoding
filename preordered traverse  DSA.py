class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('H')
nodeI = TreeNode('I')
nodeJ = TreeNode('J')
nodeK = TreeNode('K')
nodeL = TreeNode('L')
nodeM = TreeNode('M')
nodeN = TreeNode('N')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeC.right = nodeH

nodeD.ledt = nodeI
nodeD.right = nodeJ

nodeE.left = nodeK
nodeE.right = nodeL

nodeF.left = nodeM
nodeF.right = nodeN

preOrderTraversal(root)

  
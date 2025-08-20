class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('RO')
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
nodeO = TreeNode('O')
nodeP = TreeNode('P')
nodeQ = TreeNode('Q')
nodeR = TreeNode('R')
nodeS = TreeNode('S')
nodeT = TreeNode('T')
nodeU = TreeNode('U')
nodeV = TreeNode('V')
nodeW = TreeNode('W')
nodeX = TreeNode('X')
nodeY = TreeNode('Y')
nodeZ = TreeNode('Z')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeC.right = nodeH

nodeD.left = nodeI
nodeD.right = nodeJ

nodeE.left = nodeK
nodeE.right = nodeL

nodeF.left = nodeM
nodeF.right = nodeN

nodeG.left = nodeO
nodeG.right = nodeP

nodeH.left = nodeQ
nodeH.right = nodeR

nodeI.left = nodeS
nodeI.right = nodeT

nodeJ.left = nodeU
nodeJ.right = nodeV

nodeK.left = nodeW
nodeK.right = nodeX

nodeL.left = nodeY
nodeL.right = nodeZ




# Test
print("root.right.left.right.left.data:", root.right.left.right.left.data)
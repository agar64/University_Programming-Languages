#Define a árvore como uma classe. Não sei se é muito funcional mas foi a melhor forma que achei que funcionava.
class Tree:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

leaf = None

exTreeMain = Tree("a", 111, Tree("b", 55, Tree("x", 100, Tree("z", 56, leaf, leaf), Tree("w", 23, leaf, leaf)), Tree("y", 105, leaf, Tree("r", 77, leaf, leaf))), Tree("c", 123, Tree("d", 119, Tree("g", 44, leaf, leaf), Tree("h", 50, Tree("i", 5, leaf, leaf), Tree("j", 6, leaf, leaf))), Tree("e", 133, leaf, leaf)))

#prints de teste comentados, para testar facilmente só descomentar
scale = 30
def depthFirstMain(tree, level, leftLim):
    match tree:
        case Tree(left=None, right=None): #por algum motivo, tentar dar match com leaf não funciona, apesar de leaf = None. Vai saber.
            #print("Both are leaves")
            x = rootX = rightLim = leftLim
            y = scale*level
            X_Y_RootX_RightLim = (x, y, rootX, rightLim)
            setattr(tree, "x", x) #Adiciona X e Y na árvore. Teste com tree.x e tree.y antes e depois de rodar o código, antes deve dar erro, depois funciona. Teste também instanciando uma nova árvore pra mostrar como isso apenas adiciona na árvore existente e não na classe Tree().
            setattr(tree, "y", y)
            #print("Key:",tree.key,"X:",x,"Y:",y,"Root X:",rootX,"Right Lim:",rightLim)
            return X_Y_RootX_RightLim
        case Tree(left=Tree(), right=None):
            #print("Left is a subtree, Right is a leaf")
            X_Y_RootX_RightLim = depthFirstMain(tree.left, level+1, leftLim)
            x = X_Y_RootX_RightLim[2]
            y = scale*level
            setattr(tree, "x", x)
            setattr(tree, "y", y)
            #print("Key:",tree.key,"X:",x,"Y:",y,"Root X:",X_Y_RootX_RightLim[2],"Right Lim:",X_Y_RootX_RightLim[3])
            return X_Y_RootX_RightLim
        case Tree(left=None, right=Tree()):
            #print("Left is a leaf, Right is a subtree")
            X_Y_RootX_RightLim = depthFirstMain(tree.right, level+1, leftLim)
            x = X_Y_RootX_RightLim[2]
            y = scale*level
            setattr(tree, "x", x)
            setattr(tree, "y", y)
            #print("Key:",tree.key,"X:",x,"Y:",y,"Root X:",X_Y_RootX_RightLim[2],"Right Lim:",X_Y_RootX_RightLim[3])
            return X_Y_RootX_RightLim
        case Tree(left=Tree(), right=Tree()):
            #print("Both are subtrees")
            y = scale*level
            X_Y_LRootX_LRightLim = depthFirstMain(tree.left, level+1, leftLim)
            RLeftLim = X_Y_LRootX_LRightLim[3] + scale
            X_Y_RRootX_RightLim = depthFirstMain(tree.right, level+1, RLeftLim)
            x = rootX = (X_Y_LRootX_LRightLim[2] + X_Y_RRootX_RightLim[2])//2
            rightLim = X_Y_RRootX_RightLim[3]
            X_Y_RootX_RightLim = (x, y, rootX, rightLim)
            setattr(tree, "x", x)
            setattr(tree, "y", y)
            #print("Key:",tree.key,"X:",x,"Y:",y,"Root X:",rootX,"Right Lim:",rightLim)
            return X_Y_RootX_RightLim
        case _:
            #print("Nyoron~~")
            return (0, 0, 0, 0)
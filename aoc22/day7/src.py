from anytree import Node, RenderTree,  AsciiStyle
import sys
f = open(sys.argv[1],'r')

terminal = [l.rstrip().split() for l in f]



root = Node('/')
currentFolder = root

def parseDir(input):
    if parseFile(input):
        return True
    elif parseFolder(input):
        return True
    else:
        return False

def parseFile(input):
    global currentFolder
    currentParse = input[0]
    
    
    try:
        size, name = currentParse
        file = Node(name,parent=currentFolder,sz = int(size))
        return True
    except:
        return False

def parseFolder(input):
    
    global currentFolder
    currentParse = input[0]
 
    if len(currentParse) == 2 and currentParse[0] == 'dir':
        Node(currentParse[1],parent=currentFolder)
        return True
    else:
        return False


def parseCommand(input):
    global currentFolder
    currentParse = input[0]
    if currentParse[0] =='$':
        if  currentParse[1] == 'cd':
            newDir = currentParse[2]
            if newDir == '..':
                currentFolder = currentFolder.parent
            else:
                for child in currentFolder.children:
                    if child.name == currentParse[2]:
                        currentFolder = child

            return True
        elif currentParse[1] == 'ls':
            return True
        else :
            return False
    else:
        return False

def parseAll(input):
    if len(input) > 0:
        if parseCommand(input):
            return parseAll(input[1:])
        elif parseDir(input):
            return parseAll(input[1:])
        else:
            return 'noparse'
    else:
        return 'finished parsing'

print(parseAll(terminal))

print(RenderTree(root, style=AsciiStyle()))

s = []

def findSize(tree:Node):
    size = 0
    if len(tree.children) == 0:
        return tree.sz
    for child in tree.children:
        try:
            size += findSize(child)
        except:
            pass
    if size > 0:
        s.append(size)
    return size

findSize(root)

toFree = (30000000-(70000000-max(s)))
print(min([dir for dir in s if dir > toFree]))
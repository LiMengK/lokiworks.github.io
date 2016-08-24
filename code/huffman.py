# 仅仅模拟了最小优先级队列的功能，并未用最小堆来实作  
class MinPriorityQ:  
    def __init__(self):  
        self.heaplist = []  
    def Dequeue(self):  
        minObj = self.heaplist[0]  
        idxMin = 0  
        for o in self.heaplist:  
            if o.comFun(minObj) < 0:   
                minObj = o  
                idxMin = self.heaplist.index(o)         
        del self.heaplist[idxMin]  
        return minObj  
    def Insert(self, objectIn):  
        self.heaplist.append(objectIn)  
    def Empty(self):  
        return len(self.heaplist) == 0  
  
# Huffman树上的每个节点  
class HuffmanTreeNode:  
    def __init__(self, freq, char):  
        self.key = freq   # 存储字符的频率  
        self.char = char  # 存储字符本身  
        self.left = 0     # 左子节点  
        self.right = 0    # 右子节点  
    def comFun(self, OtherNode): # 比如树节点，是以字符出现的频率为key来进行的  
        if self.key > OtherNode.key:  
            return 1  
        elif self.key == OtherNode.key:  
            return 0  
        else:  
            return -1  
  
# 生成一树Huffman树。  
def MakeHuffmanTree(charList, freList):  
    num = len(charList)  
    minQ = MinPriorityQ()  
    # 将所有字符以及出现频率生成相应的树节点，插入到以频率为key的  
    # 最小优先级队列中去  
    for i in range(0, num):   
        node = HuffmanTreeNode(freList[i], charList[i])  
        minQ.Insert(node)  
    for i in range(0, num - 1):  
        # 最出优先级最低的两个节点  
        x = minQ.Dequeue()     
        y = minQ.Dequeue()  
        # 用取出的两个节点的频率和作为新节点的频率  
        z = HuffmanTreeNode(x.key + y.key, 0)  
        # 取出的两个节点作为新节点的左右子节点  
        z.left = x  
        z.right = y  
        minQ.Insert(z)  # 将新节点插入到队列中  
    return minQ.Dequeue()      
  
  
#-----------------------------------------------  
# 以下程序仅用于测试  
def PrintHuffmanTree(ht):  
    code = []  
    Traval(code, ht)  
  
def Traval(code, root, dir='3'):  
    if not dir == '3':  
        code.append(dir)  
  
    if not root.char == 0:  
        print root.char, " : ", "".join(code)  
    else:  
        Traval(code, root.left, '0')  
        code.pop()  
        Traval(code, root.right, '1')  
        code.pop()  
      
  
if __name__ == '__main__':  
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  
    freqList = [ 2,  5,   9,    3,   40,  6,  10 ]  
    TreeTop = MakeHuffmanTree(charList, freqList)  
    PrintHuffmanTree(TreeTop) 
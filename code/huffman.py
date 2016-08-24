# ����ģ������С���ȼ����еĹ��ܣ���δ����С����ʵ��  
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
  
# Huffman���ϵ�ÿ���ڵ�  
class HuffmanTreeNode:  
    def __init__(self, freq, char):  
        self.key = freq   # �洢�ַ���Ƶ��  
        self.char = char  # �洢�ַ�����  
        self.left = 0     # ���ӽڵ�  
        self.right = 0    # ���ӽڵ�  
    def comFun(self, OtherNode): # �������ڵ㣬�����ַ����ֵ�Ƶ��Ϊkey�����е�  
        if self.key > OtherNode.key:  
            return 1  
        elif self.key == OtherNode.key:  
            return 0  
        else:  
            return -1  
  
# ����һ��Huffman����  
def MakeHuffmanTree(charList, freList):  
    num = len(charList)  
    minQ = MinPriorityQ()  
    # �������ַ��Լ�����Ƶ��������Ӧ�����ڵ㣬���뵽��Ƶ��Ϊkey��  
    # ��С���ȼ�������ȥ  
    for i in range(0, num):   
        node = HuffmanTreeNode(freList[i], charList[i])  
        minQ.Insert(node)  
    for i in range(0, num - 1):  
        # ������ȼ���͵������ڵ�  
        x = minQ.Dequeue()     
        y = minQ.Dequeue()  
        # ��ȡ���������ڵ��Ƶ�ʺ���Ϊ�½ڵ��Ƶ��  
        z = HuffmanTreeNode(x.key + y.key, 0)  
        # ȡ���������ڵ���Ϊ�½ڵ�������ӽڵ�  
        z.left = x  
        z.right = y  
        minQ.Insert(z)  # ���½ڵ���뵽������  
    return minQ.Dequeue()      
  
  
#-----------------------------------------------  
# ���³�������ڲ���  
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
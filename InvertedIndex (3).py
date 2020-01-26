import sys
class InvertedIdx:
    def __init__(self):
        self.docdic={}
        self.count=0

    def AddDoc(self,name):
        self.docdic[self.count]=name+'.txt'
        self.count+=1

    def RecordLevel(self):
        term=self.ReadFiles()
        term=term[0]
        word=[]
        c=[]
        for x,y in self.docdic.items():
            infile=open(y,'r')
            a=infile.read()
            a=a.split()
            infile.close()
            for j in a:
                if len(j)>2 and (j[-2]=="'" or j[-2]==":" or j[-2]==";"):
                    word.append((j[-1*len(a):-2]).lower())
                elif '.' in j:
                    word.append((j.replace('.','')).lower())
                elif len(j)>2:
                    word.append(j.lower())
            for i in word:
                if i in term:
                    c.append((i,y))
                word=[]
        return c

    def WordLevel(self):
        files=[]
        pos=[]
        l=[]
        for x,y in self.docdic.items():
            files.append(y)
        for i in files:
            n=0
            infile=open(i,'r')
            a=infile.read()
            a=a.split()
            infile.close()
            for j in a:
                if (len(j)>2) and  a.index(j) not in pos:
                    pos.append(a.index(j))
                else:
                    a[a.index(j)]=''
                if (len(j)>2) and  a.index(j) not in pos:
                    pos.append(a.index(j))
            l.append(pos)
            pos=[]
        return l

    def ReadFiles(self):
        files=[]
        term=[]
        stopword=[]
        for x,y in self.docdic.items():
            files.append(y)
        for i in files:
            infile=open(i,'r')
            a=infile.read()
            a=a.split()
            infile.close()
            for j in a:
                if len(j)>2 and (j[-2]=="'" or j[-2]==":" or j[-2]==";"):
                    term.append((j[-1*len(a):-2]).lower())
                elif '.' in j:
                    term.append((j.replace('.','')).lower())
##                elif len(j)>2 and j not in term:
                elif len(j)>2:
                    term.append(j.lower())
                elif len(j)<=3 and j not in stopword:
                    stopword.append(j.lower())
        term,stopword.sort()
        return term,stopword

class Main:
    def __init__(self):
        self.i=InvertedIdx()
    def run(self):
        while True:
            print('''
            ================INVERTED INDEX==================
            1.ADD DOCUMENT *Note add all docs before testing
            2.WORDS COLLECTED FROM THE DOCUMENT
            3.STOP WORDS IN THE FILE
            4.RECORD-LEVEL INVERTED INDEX
            5.WORD-LEVEL INVERTED INDEX
            6.EXIT
            ''')
            choice=int(input('enter choice'))
            if choice==1:
                a=input('enter document name')
                self.i.AddDoc(a)
            if choice==2:
                a=(self.i.ReadFiles())
                print(a[0])
            if choice==3:
                a=self.i.ReadFiles()
                print(a[1])
            if choice==4:
                a=(self.i.RecordLevel())
                d=list(dict.fromkeys(a))
                d.sort()
                for x in d:
                    print(x[1],x[0])
            if choice==5:
                #a=(self.i.ReadFiles())
                a=(self.i.RecordLevel())
                b=(self.i.WordLevel())
                c=0
                while c!=len(b):
                    for i in range(len(b[c])):
                        print(a[i],b[c][i], sep = ':', end = '\t')
                    c+=1
            if choice==6:
                sys.exit()
m=Main()
m.run()

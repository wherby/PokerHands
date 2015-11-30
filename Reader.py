from  GlobalVars import *
from pprint import pprint
import re;

class ReadFile:
    def __init__(self,fileName):
        self.fileName=fileName
        self.hands=[]
        pass

    def readAllLine(self):
        file_obj=open(self.fileName)
        try:
            self.allLines=file_obj.readlines()
        finally:
            file_obj.close()

    def splitToHand(self):
        temp="";
        count=0;
        num=0;
        for line in self.allLines:
            count=count+1
            if count==1:
                print "Line 1:"+line;
            if line.strip()=="" and temp!="":
                num=num+1;
                self.hands.append(temp);
                #print num;
                #print temp;
                temp="";
            else:
                if temp=="":
                    temp=line.strip()
                else:
                    temp=temp+line
                
    def getHands(self):
        return self.hands
    
    def __str__(self):
        return self.hands[8];


class Hand:
    def __init__(self,lines):
        self.lines=lines.splitlines(True);
        self.heros=[]
        self.type=""
        self.time=""
        #print lines;
        self.preflop=[]
        self.flop=[]
        self.turn=[]
        self.river=[]
        self.showdown=[]
        self.summary=[]
        

    def getNumber(self):
        m = re.match(r'(.*)(Hand #)(\d*)(:)(.*?)(-)(.*)(Table)(.*)', self.lines[0])
        #print "m.group(1,2):", m.group(3)
        if m!=None:
            self.type= m.group(5)
            self.time= m.group(7)
            #print "TESDTT", m.group(7)
            self.ID=m.group(3)

    def getHeros(self):
        status=0
        for line in self.lines:
            m = re.match(r'(Seat \d: )(\w*) (.*)',line);
            if m!=None:
                if self.heros.count(m.group(2))==0:
                    self.heros.append(m.group(2))         
            if line.find(PREFLOPSTR) >= 0:
                status = 1
                continue
            if line.find(FLOPSTR) >= 0:
                status = 2 
                continue
            if line.find(TURNSTR) >= 0:
                status = 3 
                continue
            if line.find(RIVERSTR) >= 0:
                status = 4 
                continue
            if line.find(SHOWHANDSTR) >= 0:
                status = 5 
                continue
            if line.find(SUMMERSTR) >= 0:
                status = 6 
                continue
            if status == 1:
                self.preflop.append(line)
            if status == 2:
                self.flop.append(line)
            if status == 3:
                self.turn.append(line)
            if status == 4:
                self.river.append(line)
            if status == 5:
                self.showdown.append(line)
            if status == 6:
                self.summary.append(line)
                 

            

    def __str__(self):
        pprint(vars(self))
        return "object printed"

if __name__=="__main__":
    temp=ReadFile(".\HandHistory\scuipio\HH20121012 Halley - $0.01-$0.02 - USD No Limit Hold'em.txt")
    temp.readAllLine();
    temp.splitToHand();
    #print temp
    hands=temp.getHands();
    print hands[7];
    a=Hand(hands[7])
    a.getNumber();
    a.getHeros();
    print a;


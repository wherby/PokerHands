#import GlobalVars
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
        #print lines;
        self.states=[]
        self.summary=[]

    def getNumber(self):
        m = re.match(r'(.*)(Hand #)(\d*)(:)(.*)', self.lines[0])
        #print "m.group(1,2):", m.group(3)
        if m!=None:
            self.ID=m.group(3)

    def getHeros(self):
        for line in self.lines:
            m = re.match(r'(Seat \d: )(\w*) (.*)',line);
            if m!=None:
                if self.heros.count(m.group(2))==0:
                    self.heros.append(m.group(2))         
            pass

    def getStates(self):
        temp="";
        start=0;
        num=0;
        for line in self.lines:
            num=num+1;
            if start==1:
                if line.find("***")<0:
                    if temp=="":
                        temp=line.strip();
                    else:
                        temp=temp+line;
                else:
                    self.states.append(temp);
                    temp="";
            if start==2:
                if temp=="":
                    temp=line.strip();
                else:
                    temp=temp+line;
                if num==len(self.lines):
                    self.summary.append(temp);
                    temp="";     
            if line.find("*** HOLE CARDS ***")>=0:
                start=1;
            if line.find("*** SUMMARY ***")>=0:
                start=2;
            
            

    def __str__(self):
        temp="Heros :\n"
        for hero in self.heros:
            temp+="  "+hero+" \n"
        return temp+ "Number: "+self.ID

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
    a.getStates();
    #print "states number of a: "+str(len(a.states))
    #print "summary of a: "+a.summary[0]
    

from pandas.core import frame   #( here only)
import random
from datetime import *
from tkinter import *

def shuffle(list_of_match):
        if(n>4):
                random.shuffle(list_of_match)
                ano_list_of_match=[]
                ano_list_of_match.append(list_of_match.pop())
                i=-1
                while 0<len(list_of_match):
                        if list_of_match[i][0] in ano_list_of_match[-1] or list_of_match[i][1] in ano_list_of_match[-1]:
                                if len(list_of_match)==-i:
                                        for jj in range(len(list_of_match)):
                                                ano_list_of_match.insert(random.randrange(12),list_of_match[jj])
                                        list_of_match.clear()
                                i=i-1
                                
                        else:
                                ano_list_of_match.append(list_of_match[i])
                                del list_of_match[i]
                                i=-1
        
        else:
                random.shuffle(list_of_match)                                           #both are
                ano_list_of_match=random.sample(list_of_match,len(list_of_match))       #shuffle function
        
        return ano_list_of_match
  
  
def versus(a,rot):
        global n
        list_of_match=[]
        
        if rot%2==0:
                for j in range (n):
                        for k in range (j+1,n):             
                                list_of_match.append([a[j],a[k]])
                                list_of_match.append([a[k],a[j]])
        else:
                for j in range (n):
                        for k in range (j+1,n):
                                if k%2==j%2:
                                        list_of_match.append([a[j],a[k]])
                                else:
                                        list_of_match.append([a[k],a[j]])
        ano_list_of_match=shuffle(list_of_match)
        return ano_list_of_match
        
def ma(t1,t2):
        global predict_mat
        if(predict_mat==1):
                        #       Default
                wi=10
                if(fo>50):
                        pre=2; nxt=5
                elif(fo>30):
                        pre=2; nxt=9
                elif(fo>20):
                        pre=3; nxt=10
                elif(fo>=15):
                        pre=4; nxt=12
                elif(fo>=10):
                        pre=5; nxt=14
                elif(fo>=5):
                        pre=5; nxt=15; wi=5
                elif(fo>=2):
                        pre=5; nxt=25; wi=3
                else:
                        pre=3; nxt=30; wi=2
                t1r=random.randint(fo*pre,fo*nxt)
                t1o=random.choice([fo,random.randrange(int(fo/round(random.uniform(1.1,1.6),1)),fo)+round(random.uniform(0,0.6),1)])
                if(t1o<fo):
                        t1w=wi
                else:
                        t1w=random.randrange(1,wi+1)
                print(t1,"  :  ",t1r,"/",t1w,"  (",t1o,")",end ="  ")
                
                t2r=random.choice([random.randrange(t1r-fo,t1r),random.randrange(t1r,t1r+6),random.randrange(t1r-(fo*2),t1r)])
                t2o=random.choice([fo,random.randrange(int(fo/round(random.uniform(1.1,1.6),1)),fo)+round(random.uniform(0,0.6),1)])
                if(t2o<fo and t1r>t2r):
                        t2w=wi
                else:
                        t2w=random.randrange(1,wi)
                print("\t",t2,"  :  ",t2r,"/",t2w,"  (",t2o,")")
        
        else:        
                t1r=int(input("Enter the 1 team RUNS:"))
                t1w=int(input("Enter the 1 team WICKETS:"))
                t1o=float(input("Enter the 1 team OVERS  & BaLLS:"))
                t2r=int(input("Enter the 2 team RUNS:"))
                t2w=int(input("Enter the 2 team WICKETS:"))
                t2o=float(input("Enter the 2 team OVERS & BALLS:"))
        
        return t1r,t1w,t1o,t2r,t2w,t2o

def pre_match(i,t1,t2):
        global n,a,b,fo
        print("\t\t\t",i," Match")
        print("\t\t",t1,"   VS  ",t2)
        t1r,t1w,t1o,t2r,t2w,t2o=ma(t1,t2)
        i1=a.index(t1)
        i2=a.index(t2)
        if(t1w==10 and t1r<t2r):
                t1o=fo
        if(t1r>t2r):
                print(t1,"is win")
                b[i1][0]+=1;b[i2][1]+=1;b[i1][3]+=2;
                b[i1][4]+=t1r;       #runs scoring
                ext=(b[i1][5]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i1][5]=int(ext)+h[0]+h[1];  
                b[i1][6]+=t2r;       #runs scoring opposit team
                ext=(b[i1][7]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i1][7]=int(ext)+h[0]+h[1];
                b[i2][4]+=t2r;       
                ext=(b[i2][5]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i2][5]=int(ext)+h[0]+h[1];  
                b[i2][6]+=t1r;       
                ext=(b[i2][7]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i2][7]=int(ext)+h[0]+h[1]; 
        elif(t1r<t2r):
                print(t2,"is win")
                b[i2][0]+=1;b[i1][1]+=1;b[i2][3]+=2;
                b[i2][4]+=t2r;       #runs scoring
                ext=(b[i2][5]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i2][5]=int(ext)+h[0]+h[1];  
                b[i2][6]+=t1r;       #runs scoring opposit team
                ext=(b[i2][7]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i2][7]=int(ext)+h[0]+h[1];
                b[i1][4]+=t1r;      
                ext=(b[i1][5]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i1][5]=int(ext)+h[0]+h[1];  
                b[i1][6]+=t2r;       
                ext=(b[i1][7]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                b[i1][7]=int(ext)+h[0]+h[1];
        else:
                if(t1r==0 and t2r==0):
                        print("Match was abandone due to rain and light problem")
                        b[i1][2]+=1;b[i2][2]+=1
                        b[i2][3]+=1;b[i1][3]+=1
                else:
                        print("Match was tie")
                        t=superover(t1,t2)
                        if(t==t1):
                                b[i1][0]+=1;b[i2][1]+=1;
                                b[i1][3]+=2;
                        elif(t==t2):
                                b[i2][0]+=1;b[i1][1]+=1;
                                b[i2][3]+=2
                        else:
                                b[i1][2]+=1;b[i2][2]+=1
                                b[i2][3]+=1;b[i1][3]+=1        
def match(i):
        global n,a,b,fo
        print("\t\t\t",i," Match")
        t1=input("Enter the 1st Batting Team name:").upper()
        t2=input("Enter the 2nd Team name:").upper()
        if((t1 in a) and (t2 in a) and  t1!=t2):
                i1=a.index(t1)
                i2=a.index(t2)
                t1r,t1w,t1o,t2r,t2w,t2o=ma(t1,t2)
                if(t1w==10 and t1r<t2r):
                        t1o=fo
                if(t1r>t2r):
                        print(t1,"is win")
                        b[i1][0]+=1;b[i2][1]+=1;b[i1][3]+=2;
                        b[i1][4]+=t1r;       #runs scoring
                        ext=(b[i1][5]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i1][5]=int(ext)+h[0]+h[1];  
                        b[i1][6]+=t2r;       #runs scoring opposit team
                        ext=(b[i1][7]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i1][7]=int(ext)+h[0]+h[1];
                        b[i2][4]+=t2r;       
                        ext=(b[i2][5]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i2][5]=int(ext)+h[0]+h[1];  
                        b[i2][6]+=t1r;       
                        ext=(b[i2][7]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i2][7]=int(ext)+h[0]+h[1]; 
                elif(t1r<t2r):
                        print(t2,"is win")
                        b[i2][0]+=1;b[i1][1]+=1;b[i2][3]+=2;
                        b[i2][4]+=t2r;       #runs scoring
                        ext=(b[i2][5]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i2][5]=int(ext)+h[0]+h[1];  
                        b[i2][6]+=t1r;       #runs scoring opposit team
                        ext=(b[i2][7]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i2][7]=int(ext)+h[0]+h[1];
                        b[i1][4]+=t1r;      
                        ext=(b[i1][5]+t1o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i1][5]=int(ext)+h[0]+h[1];  
                        b[i1][6]+=t2r;       
                        ext=(b[i1][7]+t2o);g=round(ext%1,1);h=divmod(g,0.6);
                        b[i1][7]=int(ext)+h[0]+h[1];
                else:
                        if(t1r==0 and t2r==0):
                                print("Match was abandone due to rain and light problem")
                                b[i1][2]+=1;b[i2][2]+=1
                                b[i2][3]+=1;b[i1][3]+=1
                        else:
                                print("Match was tie")
                                t=superover(t1,t2)
                                if(t==t1):
                                        b[i1][0]+=1;b[i2][1]+=1;
                                        b[i1][3]+=2;
                                elif(t==t2):
                                        b[i2][0]+=1;b[i1][1]+=1;
                                        b[i2][3]+=2
                                else:
                                        b[i1][2]+=1;b[i2][2]+=1
                                        b[i2][3]+=1;b[i1][3]+=1
        else:
                print("enter the team name correctly")
                match(i)
'''def test(t1,t2):
        print("\t\t",t1 "Vs",t2,"\nEnter the 1 st innings details")
        t1r1=int(input("Enter the 1 team RUNS:"))
        t1w1=int(input("Enter the 1 team WICKETS:"))
        t1o1=float(input("Enter the 1 team OVERS & BaLLS:"))
        t2r1=int(input("Enter the 2 team RUNS:"))
        t2w1=int(input("Enter the 2 team WICKETS:"))
        t2o1=float(input("Enter the 2 team OVERS & BALLS:"))
        print("Enter the 2 nd innings details")
        t1r2=int(input("Enter the 1 team RUNS:"))
        t1w=t1w1+int(input("Enter the 1 team WICKETS:"))
        t1o=t1o1+float(input("Enter the 1 team OVERS & BaLLS:"))
        t2r2=int(input("Enter the 2 team RUNS:"))
        t2w=t2w1+int(input("Enter the 2 team WICKETS:"))
        t2o=t2o1+float(input("Enter the 2 team OVERS & BALLS:"))
        t1r=t1r1+t1r2;t2r=t2r1+t2r2;
        return t1r,t1w,t1o,t2r,t2w,t2o'''
        
def point_table(): 
        global tro,year,table
        '''     #Sorting
        for i in range(n-1):
                m=i
                for j in range(i+1,n):
                        if(b[m][3]<b[j][3]):
                                m=j
                e=a[i];  a[i]=a[m];  a[m]=e;
                e=b[i];  b[i]=b[m];  b[m]=e
        for i in range(n-1):
                m=i
                for j in range(i+1,n):
                        if(b[m][3]==b[j][3] and b[m][0]<b[j][0]):
                                m=j
                e=a[i];  a[i]=a[m];  a[m]=e;
                e=b[i];  b[i]=b[m];  b[m]=e
        for i in range(n-1):
                m=i
                for j in range(i+1,n):
                        if(b[m][3]==b[j][3] and b[m][0]==b[j][0] and b[m][8]<b[j][8]):
                                m=j
                e=a[i];  a[i]=a[m];  a[m]=e;
                e=b[i];  b[i]=b[m];  b[m]=e
        
        print("\n\t\t",tro," POINT TABLE\n\t\t",ven,year)
        print("\nTEAM\tMATCHES\tWINS\tLOSE\tDRAW\tRUN RATE\tPOINTS\n")
        for i in range (n):
                        print("{0} \t{6:2d}\t{1:2d}\t{2:2d}\t{3:2d}\t{4:2.3f}\t\t{5:3d}\n".format(a[i],b[i][0],b[i][1],b[i][2],b[i][8],b[i][3],b[i][0]+b[i][1]+b[i][2]))
        '''
        pt1=frame.DataFrame([[value for value in a],[value[0]+value[1]+value[2] for value in b],[value[0] for value in b],[value[1] for value in b],[value[2] for value in b],[value[8] for value in b],[value[3] for value in b]])
        pt1=pt1.T
        pt_df=pt1.sort_values([6,2,5],ascending=False)        
        pt_df.index=range(1,n+1)
        pt_df.columns=['TEAM','MATCHES','WINS','LOSE','DRAW','RUN RATE','POINTS']

        return pt_df

def superover(t1,t2):
        print("super-over will condect")
        t1r=int(input("Enter the 1 team RUNS:"))
        t2r=int(input("Enter the 2 team RUNS:"))
        if(t1r>t2r):
                print(t1,"is win")
                return t1
        elif(t1r<t2r):
                print(t2,"is win")
                return t2
        else:
                print("Match was tie Again")
                return 0
        
def semi(t1,t2,r):
        print("\n\t\t",r,"Semi-Final is  ",t1,"  VS  ",t2)
        t1r,t1w,t1o,t2r,t2w,t2o=ma(t1,t2)
        if(t1r>t2r):
                print(t1,"is win\n")
        elif(t1r<t2r):
                print(t2,"is win\n")
                return t2
        else:
                if(t1r==0 or t2r==0):
                        print("Match was abandome due to Rain\nAccording from point table ",t1,"enter the finals")
                else:
                        print("Match was tie")
                        t=superover(t1,t2)
                        if(0==t):
                                print("According from point table ",t1,"enter the finals")
                        else:
                                return t
        return t1

def elim(t1,t2):
        print("\n\t\t Eliminator is",t1,"   VS  ",t2)
        t1r,t1w,t1o,t2r,t2w,t2o=ma(t1,t2)
        if(t1r>t2r):
                print(t1,"is win\n")
        elif(t1r<t2r):
                print(t2,"is win\n")
                return t2
        else:
                if(t1r==0 or t2r==0):
                        print("Match was abandome due to Rain\nAccording from point table ",t1,"enter the semi")
                else:
                        print("Match was tie")
                        t=superover(t1,t2)
                        if(0==t):
                                print("According from point table ",t1,"enter the semi")
                        else:
                                return t
        return t1

def final(t1,t2):
        global re,win
        print("\n\t\tFinal is",t1.upper(),"  VS  ",t2.upper())
        t1r,t1w,t1o,t2r,t2w,t2o=ma(t1,t2)
        if(t1r>t2r):
                win=t1
        elif(t1r<t2r):
                win=t2
        else:
                if(t1r==0 or t2r==0):
                        print("Match was abandome due to rain ")
                        re+=1
                        if(re<2):
                                print("\nREMATCH WILL BE CONTECTED")
                                final(t1,t2)
                        else:
                                print("\nWINNER WAS SELECTED BY TOSS")
                                win=random.choice([t1,t2])
                                print("\n",win,"is win the toss")
                else:
                        print("Match was tie")
                        t=superover(t1,t2)
                        if(0==t):
                                print("\nWINNER WAS SELECTED BY TOSS")
                                win=random.choice([t1,t2])
                                print("\n",win,"is win the toss")
                        else:
                                win=t
        info=win.upper()+" IS WIN THE FINAL TROPHY "
        print("\n\t\t",info)
        print("\n\t\t  Congrats to ",win.upper(),"Team")
#        Label(table, text=info,font=("ariel",20,"bold")).grid(row=50,sticky=W+E)
#        table.mainloop()


n = int(input("Enter the total number of teams play : "))
tro= input("Enter the trophy Name:").upper()

if( tro=="IPL" or tro=="BBL" or tro=="T20" or tro=="PPL"):
        fo=20;          #Assign 20 Overs
else:
        ov_in = input("Enter the Over 20 or 50 or 90...(T20 or ODI or test..): ")
        if ov_in.upper() == 'TEST':
                fo = 90
        elif ov_in.upper() == 'ODI':
                fo = 50
        elif ov_in.upper() == 'T20':
                fo = 20
        else:
                fo = int(ov_in)
        

year = int(input("Enter the Match year:"))
month = int(input("Enter the Match month (only 1 to 12) :"))
#ven = input("Enter the venue:").upper()
b = [[0 for i in range(9)] for j in range(n)]             #list  comprehension
a = [input("Enter the team name:").upper() for i in range(n)]
re = 0
predict_mat = int(input("\nIf you want Predict the all matches automatically ,Enter 1 otherwise Enter 2:"))

if(predict_mat==1):
        ma_v1=[]
        ma_v2=[]
        rot=int(input("How many matches(rotation) are played against one team:"))
        ano_list_of_match=versus(a,rot)
        d=date(year,month,random.randrange(1,28))
        print("\n\t\t\t",tro," MATCHES LIST\nMATCH.NO","VENUES".center(12),"VERSUS".center(32),"DATES".center(8),"\n")
        if (rot%2==0):
                loop=int(rot/2)
        else:
                loop=rot
        serial=0
        for _ in range(loop):
                for i in range (len(ano_list_of_match)):        
                        print("  ",serial+1,"\t",ano_list_of_match[i][0].center(13)," ",ano_list_of_match[i][0].rjust(12)," VS ",ano_list_of_match[i][1].ljust(10),d.isoformat().center(10))
                        ma_v1.append(ano_list_of_match[i][0])
                        ma_v2.append(ano_list_of_match[i][1])
                        d+=timedelta(days=1)
                        serial+=1
                ano_list_of_match=shuffle(ano_list_of_match)
                d+=timedelta(days=1)
        print("\n\t\t\tEvery matches start at 08:00 PM\n")
        for i in range(serial):
                pre_match(i+1,ma_v1[i],ma_v2[i])

else:
        n1=int(input("How many matches will conduct:"))
        for i in range(1,n1+1):
                match(i);

if(n==2):
        if(b[0][0]>b[1][0]):
                print("\n\t\t",a[0],"WINS THE",tro,"TROPHY")
        elif(b[0][0]<b[1][0]):
                print("\n\t\t",a[1],"WINS THE",tro,"TROPHY")
        else:
                print("\n\t\t",a[0],"AND",a[1],"SHARE THE",tro,"TROPHY")
        exit()
for i in range(n):
        if(b[i][5]==0 or b[i][7]==0):
                b[i][5]=1;   b[i][7]=1
        rr1=b[i][4]/(int(b[i][5])+((b[i][5]%1)/0.6))
        rr2=b[i][6]/(int(b[i][7])+((b[i][7]%1)/0.6))
        b[i][8]=rr1-rr2

#                       GUI oriented view
table = Tk()                    
table.title(" POINT TABLE")

'''
Label(table, text="TEAMS     ").grid(row=0,column=0)
Label(table, text="MATCHES   ").grid(row=0,column=1)
Label(table, text="WINS      ").grid(row=0,column=2)
Label(table, text="LOSE      ").grid(row=0,column=3)
Label(table, text="DRAW      ").grid(row=0,column=4)
Label(table, text="RUN RATE  ").grid(row=0,column=5)
Label(table, text="POINTS    ").grid(row=0,column=6)

for i in range(n):
        Label(table,text= a[i]).grid(row=i+1,column=0)
        Label(table,text= b[i][0]+b[i][1]+b[i][2]).grid(row=i+1,column=1)
        Label(table,text= b[i][0]).grid(row=i+1,column=2)
        Label(table,text= b[i][1]).grid(row=i+1,column=3)
        Label(table,text= b[i][2]).grid(row=i+1,column=4)
        Label(table,text= b[i][8]).grid(row=i+1,column=5)
        Label(table,text= b[i][3]).grid(row=i+1,column=6)
'''

pt_df=point_table()
print("\n\t\t",tro,"  ",year," POINT TABLE\n")
print(pt_df)
Label(table,text=pt_df).pack()

if(tro=="IPL" and n>5):
        info="First 4 teams are enter into Play-Offs"
        Label(table,text= info).pack()
        table.mainloop()
        print("\t",info,"\n")
        print(" 1ST SEMI-FINAL\t\t    ELIMMINATOR\n",pt_df['TEAM'][1]," VS ",pt_df['TEAM'][2],"\t\t   ",pt_df['TEAM'][3]," VS ",pt_df['TEAM'][4])
        print("\t|\t\t\t|\n\t|\t\t\t| winner\n\t|\t\t\tv")
        print("\t|Loser\t\t    2ND SEMI-FINAL\n\t|-------->1st Semi loser VS Eliminator winner")
        print("\t|\t\t\t|\n\t|\t\t\t| Winner\n\t|\t\t\tv")
        print("\t|Winner\t\t      FINAL\n\t------------>  1st Semi win Vs 2nd semi win")
        '''
        f1=semi(a[0],a[1],1)
        ei=elim(a[2],a[3])
        if(a[0]==f1):
                f2=semi(a[1],ei,2)
        else:
                f2=semi(a[0],ei,2)
        '''
        f1=semi(pt_df['TEAM'][1],pt_df['TEAM'][2],1)
        ei=elim(pt_df['TEAM'][3],pt_df['TEAM'][4])
        if(pt_df['TEAM'][1]==f1):
                f2=semi(pt_df['TEAM'][2],ei,2)
        else:
                f2=semi(pt_df['TEAM'][1],ei,2)
                
elif(n>5 and tro!="IPL"):
        info="First 4 teams are enter into Semi-Finals"
        Label(table,text= info).pack()
        table.mainloop()
        print("\t",info,"\n")
        f1=semi(pt_df['TEAM'][1],pt_df['TEAM'][4],1);
        f2=semi(pt_df['TEAM'][2],pt_df['TEAM'][3],2);
        
else:
        info="First 2 team are enter into Finals"
        Label(table,text= info).pack()
        table.mainloop()
        print("\t",info,"\n")
        f1=pt_df['TEAM'][1];f2=pt_df['TEAM'][2];
        
final(f1,f2)
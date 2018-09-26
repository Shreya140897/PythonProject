import math
import sqlite3
def  batting(runs,numfour,numsix,balls,field,catch,Stumping):
    a=runs/2
    strike_Rate=runs/balls*100
    four= numfour
    six=numsix*2
    field_points=(field+catch+Stumping)*10
    if runs>=50 and runs<100:
        batscore=a+four+six+5+field_points
    elif runs>=100:
        batscore=a+four+six+10+field_points
    else:
          batscore=a+four+six+field_points

    if strike_Rate>=80 and strike_Rate<=100:
       batscore=batscore+2
    elif  strike_Rate>100:
        batscore=batscore+4
    else:
        batscore=batscore
    return batscore

def bowling(wickets,field,bowled,Given,catch,Stumping):
    if bowled==0:
        economy_rate=0
    else:
        overs=bowled/6
        economy_rate=Given/overs
    c=10*wickets
    field_points=(field+catch+Stumping)*10
    if economy_rate>3.5 and economy_rate<4.5:
        bowlscore=c+4+field_points
    elif economy_rate>=2 and economy_rate<=3.5:
        bowlscore=7+c+field_points
    elif economy_rate>0 and economy_rate<2:
        bowlscore=10+c+field_points
    else:
        bowlscore=c+field_points

    if wickets==3:
        bowlscore=bowlscore+5
    elif wickets>=5:
        bowlsc0re=bowlscore+10

    return bowlscore

def batscoring(txt):
    connection=sqlite3.connect("Cricket.db")
    result2=connection.execute("SELECT Scored,Fours,Sixes,Faced,RunOut,Catches,Stumping from Match WHERE Player='"+txt+"';")
    record2=result2.fetchall()
    a=0
    for i in record2:
        points=int(batting(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        a+=points
    return a

def bowlscoring(txt):
    connection=sqlite3.connect("Cricket.db")
    result4=connection.execute("SELECT Match.Wickets,Match.RunOut,Match.Bowled,Match.Given,Match.Catches,Match.Stumping from Match WHERE Player='"+txt+"';")
    record4=result4.fetchall()
    b=0
    for i in record4:
        points_bowl=int(bowling(i[0],i[1],i[2],i[3],i[4],i[5]))
        b+=points_bowl
    return b

def AllRounder(txt):
    connection=sqlite3.connect("Cricket.db")
    point_2=connection.execute("SELECT Match.Wickets,Match.RunOut,Match.Bowled,Match.Given,Match.Catches,Match.Stumping,Match.Scored,Match.Fours,Match.Sixes,Match.Faced from Match WHERE Player='"+txt+"';")
    record_2=point_2.fetchall()
    c=0
    d=0
    e=0
    for i in record_2:
        points_bowl=int(bowling(i[0],i[1],i[2],i[3],i[4],i[5]))
        points_bat=int(batting(i[6],i[7],i[8],i[9],0,0,0))
        c+=points_bowl
        d+=points_bat
    e=c+d
    return e

def WicketKeeping(txt):
    connection=sqlite3.connect("Cricket.db")
    result=connection.execute("SELECT Match.Scored,Match.Fours,Match.Sixes,Match.Faced,Match.RunOut,Match.Catches,Match.Stumping from Match WHERE Player='"+txt+"';")
    record=result.fetchall()
    f=0
    for i in record:
        points=int(batting(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        f+=points
    return f



    


    
        

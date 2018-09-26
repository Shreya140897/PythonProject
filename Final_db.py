import sqlite3
Cricket=sqlite3.connect('Cricket.db')
myCricket=Cricket.cursor()
# Table-1
myCricket.execute('''CREATE TABLE Match (
Player TEXT(60) PRIMARY KEY ,
Scored INTEGER, Faced INTEGER, Fours INTEGER,Sixes INTEGER, Bowled INTEGER, Maiden INTEGER, Given INTEGER, Wickets INTEGER, Catches INTEGER, Stumping INTEGER,
RunOut INTEGER);''' )

myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Kohli',102,98,8,2,0,0,0,0,0,0,1);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Yuvraj',12,20,1,0,48,0,36,1,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Rahane',49,75,3,0,0,0,0,0,1,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Dhawan',32,35,4,0,0,0,0,0,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Dhoni',56,45,3,1,0,0,0,0,3,2,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Axar',8,4,2,0,48,2,35,1,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Pandya',42,36,3,3,30,0,25,0,1,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Jadeja',18,10,1,1,60,3,50,2,1,0,1);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Kedar',65,60,7,0,24,0,24,0,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Ashwin',23,42,3,0,60,2,45,6,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Umesh',0,0,0,0,54,0,50,4,1,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Bumrah',0,0,0,0,60,2,49,1,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Bhuvneshwar',15,12,2,0,60,1,46,2,0,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Rohit',46,65,5,1,0,0,0,0,1,0,0);")
myCricket.execute("INSERT INTO Match (Player, Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut ) VALUES ('Kartik',29,42,3,0,0,0,0,0,2,0,1);")

# Table-2
myCricket.execute('''CREATE TABLE Stats (
Player TEXT(60) PRIMARY KEY ,
Matches INTEGER, Runs INTEGER, Century INTEGER, Half_Century INTEGER, Value INTEGER, Category TEXT(20));''' )
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Kohli',189,8257,29,43,120,'BAT');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Yuvraj',86,3689,10,21,100,'AR');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Rahane',158,5435,11,31,100,'BAT');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Dhawan',25,565,2,1,85,'BAT');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Dhoni',78,2573,3,19,75,'WK');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Axar',67,208,0,0,100,'BWL');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Pandya',77,8257,0,0,75,'AR');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Jadeja',16,1,0,0,85,'AR');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Kedar',111,675,0,1,90,'BWL');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Ashwin',136,1914,0,10,100,'AR');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Umesh',296,9496,10,64,110,'BWL');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Bumrah',73,1365,0,8,60,'BWL');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Bhuvneshwar',17,299,0,2,75,'AR');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Rohit',304,8701,14,52,85,'BAT');")
myCricket.execute("INSERT INTO Stats (Player, Matches,Runs,Century,Half_Century,Value,Category ) VALUES ('Kartik',11,111,0,0,75,'WK');")



# Table-3
myCricket.execute(''' CREATE TABLE Teams( Name TEXT(60) PRIMARY KEY, Players TEXT(90), Value INTEGER);''')


Cricket.commit()
Cricket.close()

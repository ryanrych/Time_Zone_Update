from urllib import *

#kamchatka = @2125071
#rangoon = @1298822
#kiev = @703446
#Guadalcanal = @2108832
#Tongatapu = @2181938
#Azores = @3411865
#Godthab = @3421324

africanCountries=["algeria","egypt","morocco","zimbabwe","south-africa","liberia","kenya"]
asianCountries=["kazakhstan","jordan","iraq","azerbaijan","thailand","china","sri-lanka","bangladesh","palestine","russia","indonesia","Israel","afghanistan","pakistan","nepal","india","malaysia","oman","saudi-arabia","south-korea","singapore","taiwan","uzbekistan","georgia","iran","japan","mongolia","armenia"]
europeanCountries=["netherlands","greece","serbia","germany","slovakia","belgium","romania","hungary","denmark","ireland","finland","turkey","portugal","uk","spain","belarus","russia","france","czech-republic","latvia","italy","bosnia-herzegovina","republic-of-macedonia","bulgaria","sweden","estonia","austria","lithuania","warsaw","croatia"]
pacificCountries=["samoa","new-zealand","tokelau","marshall-islands","france","papua-new-guinea","usa"]
americanCountires=["usa","argentina","colombia","venezuela","mexico","canada","bolivia","peru","uruguay","chile","brazil","antigua-and-barbuda","us-virgin",]

table=[]
file=open("timezones.csv","r")

for x in file:
    table.append(x.split(","))

file.close()

s=""
print s.join(list(urlopen("https://www.timeanddate.com/worldclock/algeria/algiers")))
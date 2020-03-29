from urllib import *
from calendar import *
from datetime import *

countries={"Algiers":"algeria","Cairo":"egypt","Casablanca":"morocco","Harare":"zimbabwe","Johannesburg":"south-africa","Monrovia":"liberia","Nairobi":"kenya","Hong-Kong":"hong-kong","Almaty":"kazakstan","Amman":"jordan","Baghdad":"iraq","Baku":"azerbaijan","Bangkok":"thailand","Chongqing":"china","Colombo":"sri-lanka","Dhaka":"bangladesh","Hebron":"palestine","Irkutsk":"russia","Jakarta":"indonesia","Jerusalem":"israel","Kabul":"afghanistan","Karachi":"pakistan","Kathmandu":"nepal","Kolkata":"india","Krasnoyarsk":"russia","Kuala-Lumpur":"malaysia","Magadan":"russia","Muscat":"oman","Novosibirsk":"russia","Riyadh":"saudi-arabia","Seoul":"south-korea","Singapore":"singapore","Shanghai":"china","Taipei":"taiwan","Tashkent":"uzbekistan","Tbilisi":"georgia","Tehran":"iran","Tokyo":"japan","Ulaanbaatar":"mongolia","Urumqi":"china","Vladivostok":"russia","Yakutsk":"russia","Yekaterinburg":"russia","Yerevan":"armenia","Amsterdam":"netherlands","Athens":"greece","Belgrade":"serbia","Berlin":"germany","Bratislava":"slovakia","Brussels":"belgium","Bucharest":"romania","Budapest":"hungary","Copenhagen":"denmark","Dublin":"ireland","Helsinki":"finland","Istanbul":"turkey","Lisbon":"portugal","London":"uk","Madrid":"spain","Ljubljana":"slovenia","Minsk":"belarus","Moscow":"russia","Paris":"france","Prague":"czech-republic","Riga":"latvia","Rome":"italy","Sarajevo":"bosnia-herzegovina","Skopje":"republic-of-macedonia","Sofia":"bulgaria","Stockholm":"sweden","Tallinn":"estonia","Vienna":"austria","Vilnius":"lithuania","Warsaw":"poland","Zagreb":"croatia","Apia":"samoa","Auckland":"new-zealand","Chatham-Islands":"new-zealand","Fakaofo":"tokelau","Honolulu":"usa","Majuro":"marshall-islands","Noumea":"france","Port-Moresby":"papua-new-guinea","Midway":"usa","Pago-Pago":"usa","Guatemala":"guatemala","Anchorage":"usa","Adak":"usa","Buenos-Aires":"argentina","Bogota":"colombia","Boise":"usa","Caracas":"venezuela","Chicago":"usa","Chihuahua":"mexico","Dawson-Creek":"canada","Denver":"usa","Detroit":"usa","Edmonton":"canada","Fort-Nelson":"canada","Glace-Bay":"canada","Happy-Valley-Goose-Bay":"canada","Halifax":"canada","Indianapolis":"usa","Juneau":"usa","La-Paz":"bolivia","Lima":"peru","Los-Angeles":"usa","Mazatlan":"mexico","Monterrey":"mexico","Montevideo":"uruguay","Montreal":"canada","New-York":"usa","Nome":"usa","Phoenix":"usa","Regina":"canada","Santiago":"chile","Sao-Paulo":"brazil","Saint-Johns":"antigua-and-barbuda","Saint-Thomas":"us-virgin","Thunder-Bay":"canada","Tijuana":"Mexico","Mexico-City":"mexico","Vancouver":"canada","Toronto":"canada","Whitehorse":"canada","Winnipeg":"canada"}
months=["January","February","March","April","May","June","July","August","September","October","November","December"]

table=[]
file=open("timezones.csv","r")
for x in file:
    table.append(x.split(","))
file.close()

for i in range(len(table)):
    country=""
    url=""

    city=table[i][0].split("/")[1]
    city=city.replace("St_", "Saint-")
    city=city.replace("_","-")

    if city=="Fiji":
        country="fiji"
        city="suva"
    elif city=="Kuwait":
        country="kuwait"
        city="kuwait-city"
    elif city=="Guam":
        country="usa"
        city="guam-hagatna"
    elif city=="Cape-Verde":
        country="cape-verde"
        city="praia"
    elif city=="Guyana":
        country="guyana"
        city="georgetown"
    elif city=="Puerto-Rico":
        country="puerto-rico"
        city="san-juan"
    elif city=="South-Georgia":
        country="south-georgia-sandwich"
        city="king-edward-point"
    elif city=="Chatham":
        city="Chatham-Islands"
    elif city=="Goose-Bay":
        city="Happy-Valley-Goose-Bay"
    elif city=="Kamchatka":
        url="https://www.timeanddate.com/time/zone/@2125071"
    elif city=="Rangoon":
        url="https://www.timeanddate.com/time/zone/@1298822"
    elif city=="Kiev":
        url="https://www.timeanddate.com/time/zone/@703446"
    elif city=="Guadalcanal":
        url="https://www.timeanddate.com/time/zone/@2108832"
    elif city=="Tongatapu":
        url="https://www.timeanddate.com/time/zone/@2181938"
    elif city=="Azores":
        url="https://www.timeanddate.com/time/zone/@3411865"
    elif city=="Godthab":
        url="https://www.timeanddate.com/time/zone/@3421324"
    elif city=="UTC":
        continue

    if url=="":
        if country=="":
            if table[i][0].split("/")[0]=="Australia":
                country="australia"
            else:
                country=countries[city]
        url="https://www.timeanddate.com/time/zone/%s/%s" % (country,city)

    page="".join(list(urlopen(url)))

    print city

    start=page.find("UTC/GMT")
    if page[start-3:start-1]=="No":
        table[i][1]=0
    else:
        j=start+8
        difference=""
        while page[j]!=' ':
            difference+=page[j]
            j+=1
        difference=difference.replace(":30",".5")
        difference=difference.replace(":15",".25")
        difference=difference.replace(":45",".75")
        table[i][1]=float(difference)*3600

    page=urlopen(url.replace("zone","change"))
    page="".join(list(page))
    start=page.find("Start DST:")
    if start==-1:
        table[i][2]="FALSE"
        table[i][3]=0
        for j in range(4,12):
            table[i][j]="NULL"
        table[i][12]=0
    else:
        table[i][2]="TRUE"
        step=start+35
        day=""
        while page[step]!="<":
            day+=page[step]
            step+=1
        day=day.split()
        print day
        table[i][4]=months.index(day[1])
        table[i][6]=day[0][:-1]
        month = monthcalendar(datetime.now().year, table[i][4])
        for j in range(len(month)):
            if int(day[2][:-1]) in month[j]:
                table[i][5]
                break
        start=page.find("When local standard time")
        start=page.find("<strong>",start)
        start+=8
        step=start
        time=""
        while page[step]!="<":
            time+=page[step]
            step+=1
        table[i][7]=time


for x in table:
    print x
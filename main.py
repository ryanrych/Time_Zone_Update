from urllib import *
from calendar import *
from datetime import *

#test push

#the locations are listed by continent and city, this connects cities to countries
countries={"Algiers":"algeria","Cairo":"egypt","Casablanca":"morocco","Harare":"zimbabwe","Johannesburg":"south-africa","Monrovia":"liberia","Nairobi":"kenya","Hong-Kong":"hong-kong","Almaty":"kazakstan","Amman":"jordan","Baghdad":"iraq","Baku":"azerbaijan","Bangkok":"thailand","Chongqing":"china","Colombo":"sri-lanka","Dhaka":"bangladesh","Hebron":"palestine","Irkutsk":"russia","Jakarta":"indonesia","Jerusalem":"israel","Kabul":"afghanistan","Karachi":"pakistan","Kathmandu":"nepal","Kolkata":"india","Krasnoyarsk":"russia","Kuala-Lumpur":"malaysia","Magadan":"russia","Muscat":"oman","Novosibirsk":"russia","Riyadh":"saudi-arabia","Seoul":"south-korea","Singapore":"singapore","Shanghai":"china","Taipei":"taiwan","Tashkent":"uzbekistan","Tbilisi":"georgia","Tehran":"iran","Tokyo":"japan","Ulaanbaatar":"mongolia","Urumqi":"china","Vladivostok":"russia","Yakutsk":"russia","Yekaterinburg":"russia","Yerevan":"armenia","Amsterdam":"netherlands","Athens":"greece","Belgrade":"serbia","Berlin":"germany","Bratislava":"slovakia","Brussels":"belgium","Bucharest":"romania","Budapest":"hungary","Copenhagen":"denmark","Dublin":"ireland","Helsinki":"finland","Istanbul":"turkey","Lisbon":"portugal","London":"uk","Madrid":"spain","Ljubljana":"slovenia","Minsk":"belarus","Moscow":"russia","Paris":"france","Prague":"czech-republic","Riga":"latvia","Rome":"italy","Sarajevo":"bosnia-herzegovina","Skopje":"republic-of-macedonia","Sofia":"bulgaria","Stockholm":"sweden","Tallinn":"estonia","Vienna":"austria","Vilnius":"lithuania","Warsaw":"poland","Zagreb":"croatia","Apia":"samoa","Auckland":"new-zealand","Chatham-Islands":"new-zealand","Fakaofo":"tokelau","Honolulu":"usa","Majuro":"marshall-islands","Noumea":"france","Port-Moresby":"papua-new-guinea","Midway":"usa","Pago-Pago":"usa","Guatemala":"guatemala","Anchorage":"usa","Adak":"usa","Buenos-Aires":"argentina","Bogota":"colombia","Boise":"usa","Caracas":"venezuela","Chicago":"usa","Chihuahua":"mexico","Dawson-Creek":"canada","Denver":"usa","Detroit":"usa","Edmonton":"canada","Fort-Nelson":"canada","Glace-Bay":"canada","Happy-Valley-Goose-Bay":"canada","Halifax":"canada","Indianapolis":"usa","Juneau":"usa","La-Paz":"bolivia","Lima":"peru","Los-Angeles":"usa","Mazatlan":"mexico","Monterrey":"mexico","Montevideo":"uruguay","Montreal":"canada","New-York":"usa","Nome":"usa","Phoenix":"usa","Regina":"canada","Santiago":"chile","Sao-Paulo":"brazil","Saint-Johns":"antigua-and-barbuda","Saint-Thomas":"us-virgin","Thunder-Bay":"canada","Tijuana":"Mexico","Mexico-City":"mexico","Vancouver":"canada","Toronto":"canada","Whitehorse":"canada","Winnipeg":"canada"}

#converts months from word to number form
months=["January","February","March","April","May","June","July","August","September","October","November","December"]

#reads the spreadsheet into a 2d array
table=[]
file=open("timezones.csv","r")
for x in file:
    table.append(x.split(","))
file.close()

#iterates for each row (each location)
for i in range(len(table)):
    country=""
    url=""

    #splits the first cell into continent and city
    city=table[i][0].split("/")[1]

    #replaces the space and saint conventions of the spreadsheet to those of the website
    city=city.replace("St_", "Saint-")
    city=city.replace("_","-")

    #certain cities didn't conform to the dictionary layout
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

    #skip the row with the UTC timezone (it doesn't change)
    elif city=="UTC":
        continue

    #set url if it hasn't been set
    if url=="":
        #set coutnry if it hasn't been set
        if country=="":
            #if the continent is australia, the country is australia
            if table[i][0].split("/")[0]=="Australia":
                country="australia"
            else:
                #use dictionary to find country
                country=countries[city]
        #set the url with the country and city
        url="https://www.timeanddate.com/time/zone/%s/%s" % (country,city)

    #convert the page source to a single screen
    page="".join(list(urlopen(url)))

    #find where the difference from UTC is listed
    start=page.find("UTC/GMT")

    if page[start-3:start-1]=="No":
        #theres no change when these characters are no
        table[i][1]=0
    else:
        #parse through the pext characters to find the time difference
        j=start+8
        difference=""
        while page[j]!=' ':
            difference+=page[j]
            j+=1
        #replace extra mintutes to hours
        difference=difference.replace(":30",".5")
        difference=difference.replace(":15",".25")
        difference=difference.replace(":45",".75")

        #convert hours to seconds
        table[i][1]=float(difference)*3600

    #open new page to find dst changes
    page=urlopen(url.replace("zone","change"))
    #convert neww page to string
    page="".join(list(page))
    #find the information for starting dst
    start=page.find("Start DST:")
    if start==-1:
        #set information if the location doesn't use dst
        table[i][2]="FALSE"
        table[i][3]=0
        for j in range(4,13):
            table[i][j]="NULL"
    else:
        #the location uses dst
        table[i][2]="TRUE"
        #if this value isn't 0, it is 3600. no need to find it on the page
        table[i][3]=3600
        #parse through the date in the page source
        step=start+35
        day=""
        while page[step]!="<":
            day+=page[step]
            step+=1
        day=day.split()
        #convert month from word to int form using month array
        table[i][4]=months.index(day[1])+1
        #find the week number by listing the days of the specific month
        month=monthcalendar(datetime.now().year,table[i][4])
        for j in range(len(month)):
            if int(day[2][:-1]) in month[j]:
                table[i][5]=j+1
                break
        #set the day
        table[i][6] = day[0][:-1]

        #finds the time dst starts
        start=page.find("When local standard time")
        start=page.find("<strong>",start)
        start+=8
        step=start
        time=""
        while page[step]!="<":
            time+=page[step]
            step+=1
        #set the time in the table
        table[i][7]=time

        #check if the location uses end dst data (some countries haven't ended their first dst yet) repeat the same process as start dst (above)
        if page.find("End DST:")==-1:
            for j in range(8,12):
                table[i][j]="NULL"
            table[i][12]=0
        else:
            start=page.find("Daylight Saving Time End")
            start=page.find("<br>",start)
            start+=4
            day=""
            step=start
            while page[step]!="<":
                day+=page[step]
                step+=1
            day=day.split()
            table[i][8]=months.index(day[1])+1
            month=monthcalendar(datetime.now().year,table[i][8])
            for j in range(len(month)):
                if int(day[2][:-1]) in month[j]:
                    table[i][9]=j+1
                    break
            table[i][10] = day[0][:-1]
            step+=8
            time=""
            while page[step]!="<":
                time+=page[step]
                step+=1
            table[i][11]=time
            table[i][12]=0

#create a new file with the updated information
newFile=open("OVtimezones_updated_%s-%s-%s.txt" % (str(datetime.now().month),str(datetime.now().day),str(datetime.now().year)),"w")

#write the header and table data to the new file
newFile.write("id,gmt_offset_seconds,uses_dst,dst seconds,start month,start week,start day,start hour,end month,end week,end day,end hour,dst end seconds,\n")
for i in range(len(table)):
    for j in range(len(table[i])):
        newFile.write(str(table[i][j])+',')
    newFile.write('\n')

newFile.close()
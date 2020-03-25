from urllib import *

countries={"Algiers":"algeria","Cairo":"egypt","Casablanca":"morocco","Harare":"zimbabwe","Johannesburg":"south-africa","Monrovia":"liberia","Nairobi":"kenya","Hong-Kong":"hong-kong","Almaty":"kazakhstan","Amman":"jordan","Baghdad":"iraq","Baku":"azerbaijan","Bangkok":"thailand","Chongqing":"china","Colombo":"sri-lanka","Dhaka":"bangladesh","Hebron":"palestine","Irkutsk":"russia","Jakarta":"indonesia","Jerusalem":"israel","Kabul":"afghanistan","Karachi":"pakistan","Kathmandu":"nepal","Kolkata":"india","Krasnoyarsk":"russia","Kuala_Lumpur":"malaysia","Magadan":"russia","Muscat":"oman","Novosibirsk":"russia","Riyadh":"saudi-arabia","Seoul":"south-korea","Singapore":"singapore","Shanghai":"china","Taipei":"taiwan","Tashkent":"uzbekistan","Tbilisi":"georgia","Tehran":"iran","Tokyo":"japan","Ulaanbaatar":"mongolia","Urumqi":"china","Vladivostok":"russia","Yakutsk":"russia","Yekaterinburg":"russia","Yerevan":"armenia","Amsterdam":"netherlands","Athens":"greece","Belgrade":"serbia","Berlin":"germany","Bratislava":"slovakia","Brussels":"belgium","Bucharest":"romania","Budapest":"hungary","Copenhagen":"denmark","Dublin":"ireland","Helsinki":"finland","Istanbul":"turkey","Lisbon":"portugal","London":"uk","Madrid":"spain","Ljublijana":"slovenia","Minsk":"belarus","Moscow":"russia","Paris":"france","Prague":"czech-republic","Riga":"latvia","Rome":"italy","Sarajevo":"bosnia-herzegovina","Skopje":"republic-of-macedonia","Sofia":"bulgaria","Stockholm":"sweden","Tallinn":"estonia","Vienna":"austria","Vilnius":"lithuania","Warsaw":"poland","Zagreb":"croatia","Apia":"samoa","Auckland":"new-zealand","Chatham-Islands":"new-zealond","Fakaofo":"tokelau","Honolulu":"usa","Majuro":"marshall-islands","Noumea":"france","Port-Moresby":"papua-new-guinea","Midway":"usa","Pago-Pago":"usa","Guatemala":"guatemala","Anchorage":"usa","Adak":"usa","buenos-aires":"argentina","Bogota":"colombia","Boise":"usa","Caracas":"venezuela","Chicago":"usa","Chihuahua":"mexico","Dawson-Creek":"canada","Denver":"usa","Detroit":"usa","Edmonton":"canada","Fort-Nelson":"canada","Glace-Bay":"canada","happy-valley-goose-bay":"canada","halifax":"canada","Indianapolis":"usa","Juneau":"usa","La-Paz":"bolivia","Lima":"peru","Los-Angeles":"usa","Mazatlan":"mexico","Monterrey":"mexico","Montevideo":"uruguay","Montreal":"canada","New-York":"usa","Nome":"usa","Phoenix":"usa","Regina":"canada","Santiago":"chile","Sao-Paulo":"brazil","Saint-Johns":"antigua-and-barbuda","Saint-Thomas":"us-virgin","Thunder-Bay":"canada","Tijuana":"Mexico","Toronto":"canada","Whitehorse":"canada","Winnipeg":"canada"}

table=[]
file=open("timezones.csv","r")
for x in file:
    table.append(x.split(","))
file.close()

for i in range(len(table)):
    continent=""
    country=""
    url=""

    city=table[i][0].split("/")[1]
    city=city.replace("_","-")
    city=city.replace("St","Saint")

    if city=="Fiji":
        country="fiji"
        city="suva"
    elif city=="Kuwait":
        country="kuwait"
        city="kuwait-city"
    elif city=="guam":
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
    elif city=="Chatham":
        city="chatham-islands"
    elif city=="Goose-Bay":
        city="happy-valley-goose-bay"
    elif city=="South-Georgia":
        city="south-georgia-sandwhich"
    elif city=="Kamchatka":
        url="https://www.timeanddate.com/time/zone/@2125071"
    elif city=="Rangoon":
        url="https://www.timeanddate.com/time/zone/@1298822"
    elif city=="Kiev":
        url="https://www.timeanddate.com/time/zone/@703446"
    elif city=="Guadalcanal":
        url="https://www.timeanddate.com/time/zone/@2108832"
    elif city=="Tangatapu:":
        url="https://www.timeanddate.com/time/zone/@2181938"
    elif city=="Azores":
        url="https://www.timeanddate.com/time/zone/@3411865"
    elif city=="Godthab":
        url="https://www.timeanddate.com/time/zone/@3421324"

    if url=="":
        if country=="":
            country=countries[city]
        url="https://www.timeanddate.com/time/zone/%s/%s" % (country,city)

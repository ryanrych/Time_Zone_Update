from urllib import *

#kamchatka = @2125071
#rangoon = @1298822
#kiev = @703446
#Guadalcanal = @2108832
#Tongatapu = @2181938
#Azores = @3411865
#Godthab = @3421324

africanCountries={"Algiers":"algeria","Cairo":"egypt","Casablanca":"morocco","Harare":"zimbabwe","Johannesburg":"south-africa","Monrovia":"liberia","Nairobi":"kenya"}
asianCountries={"Almaty":"kazakhstan","Amman":"jordan","Baghdad":"iraq","Baku":"azerbaijan","Bangkok":"thailand","Chongqing":"china","Colombo":"sri-lanka","Dhaka":"bangladesh","Hebron":"palestine","Irkutsk":"russia","Jakarta":"indonesia","Jerusalem":"israel","Kabul":"afghanistan","Karachi":"pakistan","Kathmandu":"nepal","Kolkata":"india","Krasnoyarsk":"russia","Kuala_Lumpur":"malaysia","Magadan":"russia","Muscat":"oman","Novosibirsk":"russia","Riyadh":"saudi-arabia","Seoul":"south-korea","Singapore":"singapore","Shanghai":"china","Taipei":"taiwan","Tashkent":"uzbekistan","Tbilisi":"georgia","Tehran":"iran","Tokyo":"japan","Ulaanbaatar":"mongolia","Urumqi":"china","Vladivostok":"russia","Yakutsk":"russia","Yekaterinburg":"russia","Yerevan":"armenia"}
europeanCountries={"Amsterdam":"netherlands","Athens":"greece","Belgrade":"serbia","Berlin":"germany","Bratislava":"slovakia","Brussels":"belgium","Bucharest":"romania","Budapest":"hungary","Copenhagen":"denmark","Dublin":"ireland","Helsinki":"finland","Istanbul":"turkey","Lisbon":"portugal","London":"uk","Madrid":"spain","Ljublijana":"slovenia","Minsk":"belarus","Moscow":"russia","Paris":"france","Prague":"czech-republic","Riga":"latvia","Rome":"italy","Sarajevo":"bosnia-herzegovina","Skopje":"republic-of-macedonia","Sofia":"bulgaria","Stockholm":"sweden","Tallinn":"estonia","Vienna":"austria","Vilnius":"lithuania","Warsaw":"poland","Zagreb":"croatia"}
pacificCountries={"Apia":"samoa","Auckland":"new-zealand","Chatham-Islands":"new-zealond","Fakaofo":"tokelau","Honolulu":"usa","Majuro":"marshall-islands","Noumea":"france","Port-Moresby":"papua-new-guinea","Midway":"usa","Pago-Pago":"usa"}
americanCountires={"Anchorage":"usa","Adak":"usa","buenos-aires":"argentina","Bogota":"colombia","Boise":"usa","Caracas":"venezuela","Chicago":"usa","Chihuahua":"mexico","Dawson-Creek":"canada","Denver":"usa","Detroit":"usa","Edmonton":"canada","Fort-Nelson":"canada","Glace-Bay":"canada","happy-valley-goose-bay":"canada","halifax":"canada","Indianapolis":"usa","Juneau":"usa","La-Paz":"bolivia","Lima":"peru","Los-Angeles":"usa","Mazatlan":"mexico","Monterrey":"mexico","Montevideo":"uruguay","Montreal":"canada","New-York":"usa","Nome":"usa","Phoenix":"usa","Regina":"canada","Santiago":"chile","Sao-Paulo":"brazil","Saint-Johns":"antigua-and-barbuda","Saint-Thomas":"us-virgin","Thunder-Bay":"canada","Tijuana":"Mexico","Toronto":"canada","Whitehorse":"canada","Winnipeg":"canada"}

table=[]
file=open("timezones.csv","r")
for x in file:
    table.append(x.split(","))
file.close()

for i in range(len(table)):
    city=table[i][0].split("/")[1]

    continent=table[i][0].split("/")[0]

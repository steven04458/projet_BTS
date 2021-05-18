import mariadb
import datetime

def treat(x):
    x=x.replace("\n","")
    x=x.replace("\r","")
    x=x.split(",")
    if(x[0]=="$GPGGA"):
        p="-> REPONSE GPS: ['"
        for i in x:
             p=p+i+"','"
        p=p+"']"
        print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+p)
        gpgga(x)

def gpgga(x):
    latitude=x[2]+x[3]
    longitude=x[4]+x[5]
    if((latitude or longitude)==''):
        print("La latitude ou la longitude comporte des valeurs nulles ! Par sécurité, aucune action sur la BDD n'est effectuée.")
    else:
        updt = update_database(latitude, longitude)
        log = update_log(latitude, longitude)

def update_database(latitude, longitude):
    db = mariadb.connect(host="localhost",user="usergps",password="gpsadmin",database="mesures")
    cursor = db.cursor()
    cmd="UPDATE GPS SET latitude='"
    cmd=cmd+latitude
    cmd=cmd+"', longitude='"+longitude+"' WHERE id=1"
    cursor.execute(cmd)
    db.commit()
    cmd="SELECT * FROM GPS"
    cursor.execute(cmd)
    data = cursor.fetchone()
    result="-> DANS LA BDD: "+str(data)
    print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+result)
    db.close()
    
def update_log(latitude, longitude):
    with open('log_gps.txt', 'a') as f:
        data = "["+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"] -> Lat:"+latitude+" ; Lon:"+longitude+"\n"
        f.write(data)
        f.close()

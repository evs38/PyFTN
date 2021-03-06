#!/usr/local/bin/python3 -bb

LINK="2:5020/12000"
#LINK="2:5020/4441"
#LINK="2:5097/31"

#ECHO="$CRACK$%"
#ECHO='%TEST%'
ECHO='RU.JNODE'

MARK=1183202


import ftnconfig

db=ftnconfig.connectdb()



for i, l, t in db.prepare("""select s.id, s.lastsent, t.text from subscriptions s, addresses sr, addresses t 
                where s.target=t.id and t.text LIKE $1 and t.domain=$2 and s.subscriber=sr.id and sr.text=$3 and sr.domain=$4""")\
                    (ECHO, db.FTN_domains["echo"], LINK, db.FTN_domains["node"]):
    print(i, l, t)
    db.prepare("update subscriptions set lastsent=$2 where id=$1")(i, MARK)

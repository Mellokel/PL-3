import requests
import re
import time
import datetime

f=open('result.html', 'w')
f.write('<!DOCTYPE html>\n')
f.write('<html><head><meta http-equiv="Content-Type" content="text/html" charset=UTF-8"></head><body>')
now=int(time.time())*1000
print(now)
day = now - (((datetime.datetime.now().hour*60+datetime.datetime.now().minute)*60+datetime.datetime.now().second)*1000)
print(day)


weekdays={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday",8:"Monday",9:"Tuesday",10:"Wednesday",11:"Thursday",12:"Friday",13:"Saturday",14:"Sunday"}
weekday=datetime.datetime.now().isoweekday()

r=requests.get('https://api.meetup.com/2/concierge?key=5d416692975687ea642e36631792d&sign=true&photo-host=public&country=us&city=Denver&category_id=34&state=CO')
name=re.findall(r'"name":"([\w\d\ \&\,\@\!\:\-\'\"\+]+)","id":"[\w ]+","time"', r.text)
address=re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
times=re.findall(r'"name":"[\w\d\ \&\,\@\!\:\-\'\"\+]+","id":"[\w ]+","time":([\d]+)', r.text)
print(times[0],times[1])
for i in range(7):
    f.write( weekdays[weekday+i] +' day: \n<ul>\n')
    print(i*86400000+day,(i+1)*86400000+day)
    for j in range(len(times)):
        if (int(times[j])>=(i*86400000+day+50400000)) and (int(times[j])<=((i+1)*86400000+day+50400000)):
            date=time.strftime(" %d %b %Y %H:%M", time.localtime(float(times[j])/1000-50400))
            f.write('<li>' + str(date) + ',<br> ' + str(name[j]) + ',<br> ' + str(address[j]) + '</li>\n')
            #print(i * 86400000 + day, i, times[j], i + 1, (i + 1) * 86400000 + day)
    f.write('</ul>\n')
f.write('</body></html>')

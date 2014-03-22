import csv
import re


def is_number(s):
   try:
       float(s)
       return True
   except ValueError:
        return False
def findAPNS(s):
    apns = []
    exp = r'[0-9]{3}-[0-9]{4}-[0-9]{3}-[0-9]{2}'
    exp1 = r'[0-9]{3} -[0-9]{4}-[0-9]{3}-[0-9]{2}'
    fPApns = re.findall(exp,s)
    if fPApns:
       for apn in fPApns:
           apns.append(apn)
    sPApns = re.findall(exp1,s)
    if sPApns:
        for apn in sPApns:
            apn.replace(" ","")
            apns.append(apn)
        apns.append(sPApns)
    if not fPApns and not sPApns:
        geocodeAddress(s)
    #print apns
    return apns   

def makeCSV(k,v):
    data = [k,v]
    #print data
    #output.writerow(data)    
    return 
def geocodeAddress(s):
    print s
    return
#output = csv.writer(open("f:\\projectlist\\output.csv", 'wb'))
#output.writerow(['Code','apn'])
data = csv.reader(open("f:\\projectlist\\MajorProjectsList-Feb2014.csv", "rb"))

fields = ["code","name","applicant","location","district","description","contact","status"]
dev = {}
dev['projects'] = [] 
rownum = 0
for row in data:
#this is where there needs to be the check for data
    if is_number(row[0]):
        items = zip(fields,row)
        item = {}
        
        for (name,value) in items:
            item[name] = value.strip()
        project = {}
        project['code'] = item['code']
           
        exp1 = '[0-9]{3}'
        tapns = findAPNS(item['location'])
        project['apns'] = tapns
        dev['projects'].append(project)
        for apn in tapns:
            if type(apn) == list:
                for v in apn:
                    makeCSV(project['code'],v)    
            else:
                makeCSV(project['code'],apn)

#check for garbage records if code is not numeric boot it.

    

    

    

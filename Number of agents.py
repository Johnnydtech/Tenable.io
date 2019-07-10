import requests, json, datetime, csv
import win32com.client as win32


access_key = ""
secret_key = ""

url = "https://cloud.tenable.com/"

api = "scanners/"
agents = "/agents"
headers = {"accept":"application/json", "content-type": "application/json","X-ApiKeys":"accessKey="+access_key+";secretKey="+secret_key}
limit='?limit=5000'
response = requests.get(url+api, headers=headers)

 
now = datetime.datetime.now()
today=datetime.date.today()



#----------------------------Number of agents, on and off----------------------------------#

def agents_scanned_daily():
    print("-----------------------------------------------------------------")
    print("-----------------------------------------------------------------")
    print("------------------ Todays date :: ", today,"---------------------")
    for scanner in response.json()['scanners']:
        scanner_id = scanner['id']
        scanner_name= scanner['name']
        resp = requests.get(url+api+str(scanner_id)+agents+limit,headers=headers)
        Total=0
        on_count=0
        of_count=0
        print("--------------------"+ scanner_name + "---------------------------")
        for agents_scanner in resp.json()['agents']:
            Total=Total+1
            if agents_scanner['status'] == 'on':
                on_count=on_count + 1
            elif agents_scanner['status'] == 'off':
                of_count =of_count + 1
                
        print("# Total Agents :",Total)
        print("# Agents on :", on_count)
        print("# Agents off :", of_count)
            

#outlook = win32.Dispatch('outlook.application')
#mail = outlook.CreateItem(0)
#mail.To = ''
#mail.Subject = 'Agent Weekly Scan'
#mail.Body = agents_scanned_daily()
mail.Send()

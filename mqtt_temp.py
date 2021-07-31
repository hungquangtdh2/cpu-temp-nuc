import paho.mqtt.client as mqtt  #import the client1
import time
import subprocess
from retry import retry
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
def checktemp():
    result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
    kq = result.stdout.decode('utf-8')
    print ((kq))
    for line in kq.split('\n'):
        print (line )
        if ("Core 0") in line: 
            x = line.find ("+",0,22)
            y = line.find ("°",0,22)
            #print("tim thay core0 ")
            return (line[x+1:y])
@retry()        
def mainprocess():

    mqtt.Client.connected_flag=False#create flag in class
    broker="192.168.1.63"

    client = mqtt.Client("python1")
    client.username_pw_set(username= "analog", password = "quanghung")             #create new instance 
    client.on_connect=on_connect  #bind call back function
    client.loop_start()
    print("Connecting to broker ",broker)
    client.connect(broker)      #connect to broker
    while not client.connected_flag: #wait in loop
        print("In wait loop")

        time.sleep(1)
    print("in Main Loop")

    client.publish("cpu/temp",checktemp()) 
    time.sleep(10)
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect
if __name__ == "__main__":
    mainprocess()
   

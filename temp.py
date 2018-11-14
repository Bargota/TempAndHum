import machine
import time
import ssd1306
import dht


HTML = """<!DOCTYPE html>
<hnml>       
    <body>
        <h1>ESP8266-Температура и Влажность</h1>
        <h2>Температура</h2>
        <p>Текущяя температура</p>
        <p>Минимальная температура</p>
        <p>Максимальная температура</p>
        <h2>Влажность</h2>
        <p>Текущяя влажность</p>
        <p>Минимальная влажность</p>
        <p>Максимальная влажность</p>
    </body>
</html>
        """

#import socket
#addr = socket.getaddrinfo('192.168.0.105', 80)[0][-1]

#s = socket.socket()
#s.bind(addr)
#s.listen(1)

start_time=time.time()
start_time2=time.time()
print(str(start_time))
print(str(start_time2))
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
d=dht.DHT22(machine.Pin(0))
#print(d)
min_t=50
min_h=100
max_t=0
max_h=0
num=0
while 1:
    #cl, addr = s.accept()
    #cl_file = cl.makefile('rwb', 0)
    #while True:
        #line = cl_file.readline()
        #if not line or line == b'\r\n':
            #break    
    #response = HTML
    #cl.send(response)
    #cl.close()


    if num%4==0:
        d.measure()
        temp=d.temperature()
        hum = d.humidity()
    
    time.sleep(0.5)
    #print('temp='+str(temp))
    #print('hum='+str(hum))

    if min_t>temp:
        min_t=temp
    if min_h>hum:
        min_h=hum

    if max_t<temp:
        max_t=temp
    if max_h<hum:
        max_h=hum
    
    oled.text('t='+str(d.temperature())+'/'+str(min_t)+'/'+str(max_t),0,0)
    oled.text('h='+str(d.humidity())+'/'+str(min_h)+'/'+str(max_h),0,8)
   
    hour_work=(time.time()-start_time)/3600
    hour_work=round(hour_work,1)
    #print(str(hour_work)+'h')
    #h_str=str(hour_work)
    #print (h_str)
        
    oled.text(str(hour_work)+'h',0,16)
    if num%2==0:
        #oled.pixel(0,20,1)
        oled.pixel(0,26,1)
        #oled.text(')',4,20)
        #oled.invert(True)
    #oled.invert(False)
    oled.show()

    
    
    oled.fill(0)
    num+=1

# cpu-temp-nuc
bring the temperature for nuc. Đưa nhiệt độ cpu hassio lên nuc 
xin chào các bạn 
Mình xin hướng dẫn các bạn cách đưa nhiệt độ cpu của NUC lên hassio 

b1: các bạn cài thư viện 
>pip3 install paho-mqtt

>pip3 install retry

b2: 
>git clone https://github.com/hungquangtdh2/cpu-temp-nuc.git

>sudo apt-get install lm-sensors

b3: sửa file 
điền địa chỉ MQTT và username, password trong file vừa tải 

>sudo nano mqtt_temp.py


    broker="192.168.1.63"

    client = mqtt.Client("python1")
    client.username_pw_set(username= "analog", password = "quanghung")  
b4: tạo sensor trên hassio 
```
  - platform: mqtt
    name: CPU Temperature
    state_topic: "cpu/temp"
    unit_of_measurement: "°C"
```
b5: chạy thử file 
```
python3 mqtt_temp.py 
```
b6: kiểm tra xem giá trị có thay đổi trên hassio không 
b7: chạy file khi khỏi động 
```
 sudo nano /etc/systemd/system/cpu-temp.service
 ```
 paste nội dung sau. nhớ thay user của bạn 
 ```
 [Unit]
Description=cpu-temp

[Service]
User=hung # thay bang user của ban
WorkingDirectory=/home/hung
ExecStart=/bin/bash -c 'cd /home/hung && python3 mqtt_temp.py'
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
```
lưu file ctrl +x , y 
```
 sudo systemctl daemon-reload
```
```
sudo systemctl start cpu-temp.service
```
 kiểm tra file chạy ok chưa bằng lệnh
```
sudo systemctl status cpu-temp.service
```
 enable service bằng lệnh
 ```
sudo systemctl enable  cpu-temp.service
```
 
 
 chúc thành công!



import serial 
import serial.tools.list_ports
import time 


def take_ecg():
    # ports = list(serial.tools.list_ports.comports())
    # port_name = ""
    # for p in ports:
    #     port_name =p.name
    #     print(p.name)
    # ecg_array = list()
    # try:
    #     arduino = serial.Serial(port=port_name, baudrate=115200) 
    #     print('Получаю данные из порта', arduino.port)
    #     i = 0
    #     while i<500:
    #         i=i+1
    #         try:
    #             s = arduino.read(3)
    #             s=s.hex()
    #             s= s.replace("4130","")
    #             d = int(s[0],base=16)*16+int(s[1],base=16)
    #             ecg_array.append(d)
    #         except Exception as e:
    #             print(e.with_traceback)
    #             return None
    #         time.sleep(0.01)
    # except Exception:
    #     print("Ошибка при попытке получения данных")
    #     return None
    
    # ecg = str(ecg_array).replace("[","").replace("]","").replace(",","")
    # return ecg

    l = list()
    for i in range(0,500):
        l.append(i)
    l_2 = str(l).replace("[","").replace("]","").replace(",","")
    return l_2
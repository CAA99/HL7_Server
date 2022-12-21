'''
CODE WRITE BY Cristian Archila Atehortua
GitHub: CAA99
email : cristian.archila00@gmail.com
'''

import socket
import threading
import time
import hl7
import requests
import sys
import mysql.connector


from concurrent.futures import thread
from mysql.connector import errorcode
from time import localtime, asctime
from datetime import datetime
from random import randrange


global _columns
global _values

print('RUNING')
HEADER = 50000
HOST = '0.0.0.0'
PORT = 22222
ADDR = (HOST,PORT)
FORMAT = 'utf-8'
hl7_wtt = []
ip_acc = ''
URL = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def bd(_columns, _values):
    try: 
        start = time.perf_counter()
        mydb = mysql.connector.connect(
            host='',
            user= '', 
            password= '',
            database='',
        )
        cursor = mydb.cursor()
        sql = "INSERT INTO monitores (ip ,id, msg, time) VALUES (%s, %s, %s, %s)"
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('ambulancias', _columns, _values)
        cursor.execute(sql)
        end = time.perf_counter()
        print(f'TIME TO INSERTION IN DB {end - start}\n')
        mydb.commit()
        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("DENIED ACCESS!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB NOT EXIST!")
        else:
            print(err)
    else:
        mydb.close()

def handle_client(conn, addr):
    print(f"[Nueva Conexion] {addr}")
    while True:
        try:
            msg = conn.recv(HEADER)
            
            if  msg:
                msg = msg.decode('UTF-8')
                dt = datetime.now()

                mensaje = {
                    'ip': addr[0],
                    'id' : 'dispositivo1',
                    'msg' : msg,
                    'time': dt,
                }

                HTTP = requests.post(URL, data=mensaje) 

                _columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mensaje.keys())
                _values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mensaje.values())
                bd(_columns, _values)
                conn.send(respuestaHL7(msg))
                
        except TimeoutError as a :
            print('conexion cerrada')
            print(a)
            thread.exit()
        except ConnectionAbortedError as e:
            pass
        except ConnectionError as e:
            pass

def respuestaHL7(hl7_msg):
    try:
        #Create ACK msg for the MSV

        msg = hl7.parse(hl7_msg)
        print(f'\nMensaje HL7 desde monitor:\n {msg}'.replace('\r', '\n'))
        msg_respuesta = msg.create_ack()
        hl7_wtt.append(msg_respuesta)
        _convert = ''.join([str(item) for item in hl7_wtt]).encode('utf-8')
        msg_respuesta = b'\x0b' + bytes(_convert) + b'\x1c\r'
        hl7_wtt.clear()
        print (f'Respuesta\n: {msg_respuesta}')
        return msg_respuesta
    except hl7.exceptions.ParseException as e: 
        print(e)

def filtrado_msg(msg):
    # Filter data from OBX

    msg = hl7.parse(msg)
    obx = msg['OBX'][0][5][0]
    print(f'filtrado de OBX: {obx}')


def start_server():
    
    server.listen()
    while True:
        try:
            conn, addr = server.accept()
            if addr[0] == ip_acc or '10.200.16.239':
                thread = threading.Thread(target=handle_client, args=(conn, addr)) 
                print(f"[Conexiones Activas] {threading.active_count() - 1}") 
            else:
                print(f'La direccion IP no es la esperada {addr[0]}, la IP esperada es {ip_acc}')
                thread.exit()
        except (KeyboardInterrupt, SystemExit):
            print('Proceso Interrumpido')
            sys.exit()        


if __name__ == "__main__":
    start_server()
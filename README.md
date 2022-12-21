This is a Python script that implements a socket server that listens for incoming connections on a specific host and port. The server receives HL7 messages from client devices, processes the messages, and sends a response back to the client.

# HL7 Server

This is a Python script that implements a socket server that listens for incoming connections on a specific host and port. The server receives HL7 messages from client devices, processes the messages, and sends a response back to the client.

## Features

- Receives HL7 messages from client devices and stores them in a MySQL database
- Sends a response (ACK) message to the client in the form of an HL7 message
- Posts the received message and client information to a specified URL

## Requirements

- Python 3
- mysql-connector-python
- hl7
- requests

## Usage

To run the script, navigate to the directory where it is located and run the following command:

`python hl7_server.py`

The server will start listening for incoming connections on the specified host and port.

## Notes

- Make sure to update the MySQL and URL details in the script before running it.
- The script has been tested with Python 3.8.5 on macOS.
- The script has been tested with Python 3.10.4 on Microsoft.

## Author

Cristian Archila Atehortua

GitHub: CAA99

Email: cristian.archila00@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Este es un script de Python que implementa un servidor de sockets que escucha conexiones entrantes en un host y puerto específicos. El servidor recibe mensajes HL7 de dispositivos cliente, procesa los mensajes y envía una respuesta de vuelta al cliente.

# Servidor HL7

Este es un script de Python que implementa un servidor de sockets que escucha conexiones entrantes en un host y puerto específicos. El servidor recibe mensajes HL7 de dispositivos cliente, los procesa y envía una respuesta de vuelta al cliente.

## Características

- Recibe mensajes HL7 de dispositivos cliente y los almacena en una base de datos MySQL
- Envía un mensaje de respuesta (ACK) al cliente en forma de mensaje HL7
- Publica el mensaje recibido y la información del cliente en una URL especificada

## Requisitos

- Python 3
- mysql-connector-python
- hl7
- requests

## Uso

Para ejecutar el script, navegue hasta el directorio donde se encuentra y ejecute el siguiente comando:

`python hl7_server.py`


El servidor comenzará a escuchar conexiones entrantes en el host y puerto especificados.

## Notas

- Asegúrese de actualizar los detalles de MySQL y URL en el script antes de ejecutarlo.
- El script ha sido probado con Python 3.8.5 en macOS.
- The script has been tested with Python 3.10.4 on Microsoft.

## Author

Cristian Archila Atehortua

GitHub: CAA99

Email: cristian.archila00@gmail.com


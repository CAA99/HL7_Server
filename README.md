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

## Author

Cristian Archila Atehortua

GitHub: CAA99

Email: cristian.archila00@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

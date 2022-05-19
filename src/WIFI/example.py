import socket_tool
import time

if __name__ == '__main__':
    service = socket_tool.Service(ip="127.0.0.1", port=8000)
    socket_tool.rev_message(service)
    
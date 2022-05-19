import socket_tool
if __name__ == '__main__':
    client = socket_tool.Client(ip="127.0.0.1", port=8000)
    socket_tool.send_message(client, "tangbin")

    
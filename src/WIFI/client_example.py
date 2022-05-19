import socket_tool
if __name__ == '__main__':
    client = socket_tool.Client(ip="0.0.0.0", port=8001)
    socket_tool.send_message(client, "tangbin")

    
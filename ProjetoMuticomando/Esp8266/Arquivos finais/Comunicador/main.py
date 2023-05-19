from httpServer import HttpServer
"""
while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:  
        last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
"""

server = HttpServer()

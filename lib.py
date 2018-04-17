# Проверка аргументов адреса и порта
import re

def addr_check(addr):
    if re.findall(r'^\d*\.\d*\.\d*\.\d*$', addr) \
    or re.findall(r'^localhost$', addr) \
    or re.findall(r'', addr):
        return addr
    else:
        return False
    
def port_check(port):
    if type(port) == int \
    and port > 1024 and port < 49151:
        return port
    else:
        return False
# Проверка сообщения сервером

# Провека ответа сервера клиентом

#
#
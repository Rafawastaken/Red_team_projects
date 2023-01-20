import socket

def scanner(target:str, port:int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    status = s.connect_ex((target, port))
    if status == 0:
        return True
    return False

def main():
    target = str(input("Target: "))
    port = int(input("Port: "))

    if scanner(target, port): print(f"{port} is open")
    else: print(f"{port} is closed")
    
if __name__ == '__main__':
    main()
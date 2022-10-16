#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Денис
#
# Created:     16.10.2022
# Copyright:   (c) Денис 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def main():

    try:
        myIP = extraxt_ip()
    except:
        myIP = "Ничего не получилось!"
    print(extract_ip())

    stri = f'<p>Привет Матвейка! <br>Это наше первое приложение на Питоне в сети Интернет!<br>Ура!<br>{myIP}</p>'
    print(stri)
    pass

if __name__ == '__main__':
    main()

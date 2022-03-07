from shutil import which
import os
import sys
import time
import json
import requests
import subprocess as subp
R = '\033[31m' # red
G = '\033[31m' # red
C = '\033[0m' #  white
W = '\033[0m'  # white



def check_dependencies():
    print(G + '[+]' + C + ' Checking Dependencies...' + W)
    pkgs = ['python3', 'pip3', 'php', 'ssh']
    inst = True
    for pkg in pkgs:
        present = which(pkg)
        if present == None:
            print(R + '[-] ' + W + pkg + C + ' is not Installed!')
            inst = False
        else:
            pass
    if inst == False:
        exit()


def server(template):
      port = 3333
      print('\n' + G + '[+]' + C + ' Port : '+ W + str(port))
      print('\n' + G + '[+]' + C + ' Starting PHP Server......' + W, end='')
      try:
          subp.Popen(['php','-s','0.0.0.0:{}'.format(port),'-t','templates/{}/'.format(template)])
          time.sleep(3)
          url = 'http://0.0.0.0:{}/index.html'.format(port) 
          php_rqst = requests.get(url)
          php_sc = php.php_rqst.status_code
          print(php_sc)
          if php_sc == 200:
              return url
          else:
              return None
      except requests.ConnectionError:
          print(C + "["+ R+"FAILED"+ C + "]" + W)
          return None





    



    
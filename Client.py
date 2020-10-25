import json
import requests
import time
import threading
from rsacrypt import rsacrypt
from Stuff import monster, character
import rsa

class Game():

    def __init__(self):
        self.mons = monster()
        self.char = character()

    def run(self):
        
        headers = {'Content-Type': 'application/json'}
        
        #d = 1
        while (True):

            time.sleep(1)

            rk = rsacrypt()

            j = [self.mons.__dict__, self.char.__dict__, {'crypt' : '', 'key' : ''}]

            j[2]['crypt'] = str(rk.encrypt('random'), encoding='UTF-8')
            j[2]['key'] = str(rk.prikey._save_pkcs1_pem(), encoding='UTF-8')

            rk.prikey = rsa.PrivateKey._load_pkcs1_pem(j[2]['key'])
            
            #print('certification = {}\nencrypt = {}\n'.format('random', j[2]['crypt']))
            #print(rk.decrypt(j[2]['crypt']))
            
            json_string = json.dumps(j)

            r = requests.post('http://127.0.0.1:8080', headers=headers, data = json_string)

            #print("Transfer {} | ".format("11"))

            #print(r.text)

            #d += 1

    def start(self):
        
        t = threading.Thread(target=self.run)
        t.start()

        dic = [self.char.__dict__, self.mons.__dict__]

        while(True):

            r = input()

            r = r.split(' ')
            #print(r)

            try:
                #char/mons, attribute, value
                if(len(r) == 3):

                    dic[int(r[0])][r[1]] = float(r[2])
                    print( dic )
                    #self.char.__dict__ = dic[0]
                    #self.mons.__dict__ = dic[1]

            except Exception as e:
                print(e.args[0])

Game().start()


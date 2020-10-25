

import json
import http.server 
from http.server import SimpleHTTPRequestHandler
from Stuff import monster, character
from rsacrypt import rsacrypt
import rsa

# Test
class Server(SimpleHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        self._set_headers()
        self.wfile.write(("Hello world").encode())

    def do_POST(self):

        length = int(self.headers.get('Content-length'))

        s = self.rfile.read(length)
        
        json_data = str(s, encoding='UTF-8')
        
        js_obj = json.loads(json_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write('AHOY'.encode())

        #print(js_obj)

        mons = monster()
        mons.__dict__ = js_obj[0]
        char = character()
        char.__dict__ = js_obj[1]
        
        rk = rsacrypt()
        crypt = js_obj[2]['crypt']
        rk.prikey = rsa.PrivateKey._load_pkcs1_pem(js_obj[2]['key'])
        decry_string = rk.decrypt(crypt)

        print('certification = {}\ndecrypt = {}\n'.format(crypt, decry_string))

        flag = {'s': 0, 'u': 0, 'a': 0}
        # value modification
        # infinite skill cast 
        print("hp = ",char.hp)
        if (char.delay < 0.5):
            flag['s'] = 1
            print("[Warning]Game Bot Detected :　Unusaul Skill Delay")  
        else :
            flag['s'] = 0

        # unusual character atk / hp
        if (char.hp >= char.threshold * 1000 or char.atk >= char.threshold * 100 ):
            flag['u'] = 1
            
            print("[Warning]Game Bot Detected : Unusual Character Status")
        else:
            flag['u'] = 0
    
        
        # acceleration
        
        if (char.frames >= 2 * 60):
            flag['a'] = 1
            print("[Warning] Game Bot Detected :　Acceleration Scipt")        
        else:
            flag['a'] = 0
        # auto script (optional)


    # Formula, calculate the certification string
    def formula(self):
        pass


def run(server_class=http.server.HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

run()
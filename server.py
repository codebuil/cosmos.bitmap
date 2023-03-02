from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import socket

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configura a resposta HTTP
        
        PORTs = 8080
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        # Configura a resposta como uma string contendo código 
        link = self.path[1:]
        
        l1=""
        html=""
        url = link.split("&")
        ll1=-1
        ll2=-1
        ll3=-1
        try:
            ll1=l1.find(".png")
            ll2=l1.find(".jpg")
            ll3=l1.find(".bmp")
        except:
            ll1=-1
            ll2=-1
            ll3=-1
                
        try:
            if len(url)>1 :
                  l1=url[1]
                  with urllib.request.urlopen(l1) as response:
                       if ll1<1 and ll2<1 and ll3<1:
                           self.send_response(200)
                           self.send_header('Content-type', 'text/html')
                           self.end_headers()
                           hostname = socket.gethostname()
                           ip_address = socket.gethostbyname(hostname)
                           html = response.read().decode()
                           html=html.replace("https://","rrr1234567890://"+ip_address+":"+str(PORTs)+"/&rrr1234567890s://")
                           html=html.replace("./","rrr1234567890://"+ip_address+":"+str(PORTs)+"/&rrr1234567890s://")
                           html=html.replace("rrr1234567890","http")
                           self.wfile.write(bytes(html, "utf8"))
                       else:
                           self.send_response(200)
                           self.send_header('Content-Type', 'image/png')
                           self.end_headers()
                           html = response.read().decode()
                           self.wfile.write(bytes(html, "utf8"))
                        
        except:
            try:
                self.wfile.write(bytes(html, "utf8"))
            except:
               print ("error")
        return

# Define a porta em que o servidor deve escutar
PORT = 8080
print ("\033c\033[44;30m\n")
# Cria um servidor que escuta na porta especificada e usa o manipulador de solicitações HTTP personalizado
with HTTPServer(("", PORT), MyServer) as httpd:
    print("Servidor rodando na porta:", PORT)
    # Aguarda indefinidamente por solicitações HTTP
    httpd.serve_forever()

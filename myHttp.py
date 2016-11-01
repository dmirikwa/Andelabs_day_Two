import socket
import httplib
s=socket.gethosstbyname("ajax.googleapis.com")
p=socket(AF_INET,SOCK_STREAM)
p.connect((s,80))
Request=httplib.HTTP("ajax.googleapis.com",80)
Request.putrequest(GET,"/ajax/libs/jquery/3.1.1/jquery.min.js")
Request.putheader('Accept','text/html')
Request.endheaders()
Request.getreply()
page=Request.getfile()

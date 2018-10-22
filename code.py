import web


OurIpAddr = '127.0.0.1'
render = web.template.render('templates/')
urls =   '/','index'

app = web.application(urls, globals())


class index:
    def GET(self):
	return render.index()
        
    
    def POST(self):
	IpAddr = web.ctx['ip']
	if IpAddr == OurIpAddr: '''here we verify the ip adress of the sender''''
            data = web.data()
            print ('There is incoming data')
            print (data)
	    print
	    return render.index()
	
        

if __name__ == "__main__":     
    app.run() 

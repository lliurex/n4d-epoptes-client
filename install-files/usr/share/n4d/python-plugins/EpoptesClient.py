import subprocess
import os
import lliurex.net
import threading

class EpoptesClient:
	
	def startup(self,options):
		
		#Old n4d:if options["controlled"]:
		if options["boot"]:
			self.grab_epoptes_certificate_thread()
			self.disable_wol_thread()
					
	#def startup
	
	def grab_epoptes_certificate_thread(self):
		
		t=threading.Thread(target=self._grab_epoptes_certificate)
		t.daemon=True
		t.start()
		
	#def epoptes_daemon
	
	def _grab_epoptes_certificate(self):
		
		if os.system("host server > /dev/null")==0:
			
			execute=False
			p=subprocess.Popen(["ps aux | grep 'epoptes-client -c' | wc -l"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			output=p.communicate()[0]

			if type(output) is bytes:
				output=output.decode()

			try:
				t=int(output.strip("\n"))
				if t<=2:
					execute=True
			except:
				execute=False
				
			
			if execute:
				p=subprocess.Popen(["epoptes-client -c"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				p.communicate()
		
	#def _grab_epoptes_certificate
	
	def disable_wol_thread(self):
		
		t=threading.Thread(target=self._disable_wol)
		t.daemon=True
		t.start()
		
	#def disable_wol_thread
	
	
	def  _disable_wol(self):
		
		devices=lliurex.net.get_devices_info()
		for dev in devices:
			os.system("ethtool -s %s wol g"%dev["name"])
		
	#def _disable_wol
	
#class EpoptesClient


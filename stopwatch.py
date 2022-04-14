try:
	from tkinter import *
	import time,os,notify2
	from PyQt5 import QtCore
	from threading import *
	from PyQt5.QtGui import *
	from PyQt5.QtWidgets import *
	from PIL import Image,ImageTk
	class stop_watch():
		def __init__(self):
			self.running = False
			self.count=66600
			self.root = Tk()
			self.root.title("StopWatch")
			self.root.iconphoto(False, PhotoImage(file='icons/clock.png'))
			self.root.geometry('300x260')
			self.d_time="00:00:00"
			self.timer_label = Label(self.root,text='Set timer : ',font = ('1',12))
			self.timer_label.grid(row=0,column=0,padx=11)
			self.hour_box = Spinbox(self.root,from_=0,to=24,width=2)
			self.hour_box.grid(row=0,column=1,pady=19)
			self.hour_label = Label(self.root,text=' H ')
			self.hour_label.grid(row=0,column=2)
			self.minute_box = Spinbox(self.root,from_=0,to=60,width=2)
			self.minute_box.grid(row=0,column=3)
			self.minute_label = Label(self.root,text=' M ')
			self.minute_label.grid(row=0,column=4)
			self.second_box = Spinbox(self.root,from_=0,to=60,width=2)
			self.second_box.grid(row=0,column=5)
			self.second_label = Label(self.root,text=' S')
			self.second_label.grid(row=0,column=6)
			self.repeat_label = Label(self.root,text='Repeat    :',font=('1',12))
			self.repeat_label.grid(row=1,column=0)
			self.repeat_box = Spinbox(self.root,from_=0,to=100,width=5)
			self.repeat_box.grid(row=1,column=1,columnspan=2)
			self.tkopen = True
			self.apprun = False
			self.timer_value = True
			self.notify_me = True
			self.sound_on = True
			self.label = Label(self.root,text = '   Welcome!',font=('1',19))
			self.label.grid(row=2,column=0,columnspan=7,pady=30)
			self.start = Button(self.root,text = 'Start',width = 6,command = self.Start)
			self.stop = Button(self.root,text = 'Stop',width = 6, state = 'disabled',command = self.Stop)
			self.reset = Button(self.root,text = 'Reset',width=6, state = 'disabled',command=self.Reset)
			self.start.grid(row=3,column=0,columnspan=2)
			self.stop.grid(row=3,column=1,columnspan=3)
			self.reset.grid(row=3,column=4,columnspan=4)
			self.minimize = Button(self.root,text='Hide',width=7,command=self.tray)
			self.minimize.grid(row=4,column=1,columnspan=3,pady=8)
			self.silence_btn_img = Image.open('icons/silence.png')
			self.silence_btn_img = self.silence_btn_img.resize((28,26),Image.ANTIALIAS)
			self.silence_btn_img = ImageTk.PhotoImage(self.silence_btn_img)
			self.nsound_btn_img = Image.open('icons/sound.png')
			self.nsound_btn_img = self.nsound_btn_img.resize((23,26),Image.ANTIALIAS)
			self.nsound_btn_img = ImageTk.PhotoImage(self.nsound_btn_img)
			self.sound_on_btn_img = Image.open('icons/speaker.png')
			self.sound_on_btn_img = self.sound_on_btn_img.resize((20,28),Image.ANTIALIAS)
			self.sound_on_btn_img = ImageTk.PhotoImage(self.sound_on_btn_img)
			self.sound_off_btn_img = Image.open('icons/mute.png')
			self.sound_off_btn_img = self.sound_off_btn_img.resize((23,23),Image.ANTIALIAS)
			self.sound_off_btn_img = ImageTk.PhotoImage(self.sound_off_btn_img)
			self.sound_btn = Button(self.root,command = self.sound_on_off,width = 70,image = self.sound_on_btn_img,height = 26)
			self.sound_btn.grid(row = 4,column=0,columnspan=2)
			self.notify_btn = Button(self.root,command = self.notify_on_off,width = 70,image = self.nsound_btn_img)
			self.notify_btn.grid(row = 4,column=4,columnspan=7)
			self.root.bind("<Destroy>",self._destroy)
			self.starttime = time.time()
			self.root.mainloop()
		def sound_on_off(self):
			if self.sound_on:
				self.sound_on = False
				self.sound_btn['image']=self.sound_off_btn_img
				if self.apprun:self.option4.setText("Turn On Sound")
			else:
				self.sound_on = True
				self.sound_btn['image']=self.sound_on_btn_img
				if self.apprun:self.option4.setText("Turn Off Sound")
		def notify_on_off(self):
			if self.notify_me:
				self.notify_me = False
				self.notify_btn['image']=self.silence_btn_img
				if self.apprun:self.option5.setText("Turn On Notification")
			else:
				self.notify_me = True
				self.notify_btn['image']=self.nsound_btn_img
				if self.apprun:self.option5.setText("Turn Off Notification")
		def _destroy(self,h):
			self.tkopen = False
		def timerEvent1(self):
			def sound():
				show_timer = 'Timer : '+watch
				notify2.init('')
				n = notify2.Notification('Stopwatch',show_timer,'notification-message-im')
				if str(self.repeat)=='True':self.timer+=self.x_timer-66600
				elif self.repeat>1:
					self.timer+=self.x_timer-66600
					self.repeat-=1
				if self.notify_me:n.show()
				if self.sound_on:os.system('play -nq -t alsa synth {} sine {}'.format(1,5000))
			b = 0
			self.starttime = time.time()
			while self.running and (self.apprun or self.tkopen):
				a = (time.time()-self.starttime)
				change = (a-b)-1
				if change<0:change=0
				b=a
				realtime = time.ctime(self.count)
				realtime = realtime.split(" ")
				watch = realtime[4]
				if self.count==self.timer:
					thread = Thread(target=sound)
					thread.start()
				if self.tkopen:
					display = "   "+watch
					self.label['text'] = display
				else:self.thread.cancel()
				if self.apprun:self.option1.setText(watch)
				else:self.thread.cancel()
				self.count+=1
				time.sleep(1-change)
			else:
				self.thread.cancel()
		def tray(self):
			self.root.withdraw()
			self.tkopen = False
			app = QApplication([])
			app.setQuitOnLastWindowClosed(False)
			self.apprun = True
			def tray_stop():
				option2.setText("Start")
				option2.triggered.connect(tray_start)
				self.Stop()
			def tray_reset():
				self.option1.setText("00:00:00")
				self.Reset()
			def tray_start():
				option2.setText("Stop")
				option2.triggered.connect(tray_stop)
				self.running = True
				self.start['state'] = 'disabled'
				self.stop['state'] = 'normal'
				self.reset['state'] = 'normal'
				self.hour_box['state']='disabled'
				self.minute_box['state']='disabled'
				self.second_box['state']='disabled'
				self.repeat_box['state']='disabled'
				self.reset['command']=self.Reset
				self.thread = Timer(1,self.timerEvent1)
				self.thread.start()
			icon = QIcon('icon.png')
			tray = QSystemTrayIcon()
			tray.setIcon(icon)
			tray.setVisible(True)
			menu = QMenu()
			self.option1 = QAction("00:00:00")
			option2 = QAction('')
			option3 = QAction("Reset")
			self.option4 = QAction('Sound')
			self.option5 = QAction('Notification')
			menu.addAction(self.option1)
			menu.addAction(option2)
			menu.addAction(option3)
			menu.addAction(self.option4)
			menu.addAction(self.option5)
			if self.sound_on:
				self.option4.setText("Turn Off Sound")
			if self.notify_me:
				self.option5.setText('Turn Off Notification')
			self.option4.triggered.connect(self.sound_on_off)
			self.option5.triggered.connect(self.notify_on_off)
			option3.triggered.connect(tray_reset)
			self.option1.triggered.connect(self.call_back)
			self.option1.triggered.connect(app.quit)
			quit = QAction('quit')
			quit.triggered.connect(self.collapse)
			menu.addAction(quit)
			quit.triggered.connect(app.quit)
			tray.setContextMenu(menu)
			if self.running:
				option2.setText("Stop")
				option2.triggered.connect(tray_stop)
				if self.running:
					self.thread = Timer(1,self.timerEvent1)
					self.thread.start()
			else:
				option2.setText("Start")
				option2.triggered.connect(tray_start)
				self.option1.setText(self.d_time)
			app.exec_()
		def call_back(self):
			self.tkopen = True
			self.apprun = False
			if self.count==66600:self.label['text'] = "   00:00:00"
			else:
				realtime = time.ctime(self.count-1)
				realtime = realtime.split(" ")
				self.d_time = realtime[4]
				display = "   "+self.d_time
				self.label['text'] = display
			self.root.deiconify()
			if self.running:self.Start()
		def collapse(self):
			self.apprun=False
			self.root.destroy()
		def counter(self):
			self.thread = Timer(1,self.timerEvent1)
			self.thread.start()
		def Start(self):
			self.running = True
			self.start['state'] = 'disabled'
			self.stop['state'] = 'normal'
			self.reset['state'] = 'normal'
			self.hour_box['state']='disabled'
			self.minute_box['state']='disabled'
			self.second_box['state']='disabled'
			self.repeat_box['state']='disabled'
			self.reset['command']=self.Reset
			if self.timer_value:self.n_timer()
			self.counter()
		def n_timer(self):
			self.timer_value = False
			hour = self.hour_box.get()
			minute = self.minute_box.get()
			seconds = self.second_box.get()
			repeat = self.repeat_box.get()
			if hour:hour=int(hour)
			else:hour = 0
			if minute:minute = int(minute)
			else:minute=0
			if seconds:seconds=int(seconds)
			else:seconds=0
			if repeat:self.repeat=int(repeat)
			else:self.repeat=1
			self.timer = ((hour*3600)+(minute*60)+seconds)
			if self.timer==0:self.repeat=False
			else:self.timer+=66600
			self.x_timer = self.timer
			self.x_repeat = self.repeat
		def Stop(self):
			self.start['state'] = 'normal'
			self.stop['state'] = 'disabled'
			self.reset['state'] = 'normal'
			self.running = False
		def Reset(self):
			self.n_timer()
			self.count = 66600
			self.d_time = "00:00:00"
			if self.running==False:self.reset['command'] = self.timer_reset
			self.label['text'] = '   00:00:00'
		def timer_reset(self):
			self.timer_value = True
			self.hour_box['state']='normal'
			self.minute_box['state']='normal'
			self.second_box['state']='normal'
			self.repeat_box['state']='normal'
			self.hour_box.delete(0,2)
			self.minute_box.delete(0,2)
			self.second_box.delete(0,2)
			self.repeat_box.delete(0,2)
	stop_watch()
except ImportError:
	print("Installing required packages...")
	from urllib.request import urlopen
	def is_internet_available():
	    try:
	        urlopen('http://216.58.192.142', timeout=1)
	        return True
	    except:return False
	if is_internet_available():
		os.system("sudo apt update && sudo apt install python3-pip && sudo apt install python3-tk && python3 -m pip install pyqt5 && python3 -m pip install notify2 && sudo apt install sox")
		print("Re-Run the program")
	else:print('Please connect to internet')

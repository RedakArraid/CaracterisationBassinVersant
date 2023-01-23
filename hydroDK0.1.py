from tkinter import*
from time import*
from random import*
from tkinter.messagebox import askyesno
import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
class HydroDk(object):
	"""docstring for HydroDk"""
	def __init__(self, arg=0):
		self.fp = Tk()
		self.fp.geometry(str(self.fp.winfo_screenwidth())+"x"+str(self.fp.winfo_screenheight())+"0")
		fileMenu = Menubutton(self.fp, text ='Fichier')
		me1 = Menu(fileMenu)
		me1.add_command(label ='Nouveau', underline =0,command =self.nouveau)
		me1.add_command(label ='Quitter', underline =0,command = self.fp.destroy)
		fileMenu.configure(menu = me1)
		fileMenu.grid(row=0,column=0)
		fileMenu1 = Menubutton(self.fp, text ='Option')
		me2 = Menu(fileMenu1)
		me2.add_command(label ='Digitaliser', underline =0,command =self.digitaliser)
		me2.add_command(label ='Calculer', underline =0,command = self.calculer)
		self.surface=Label(self.fp,text="surface = ",font='calibri 20')
		self.surface.place(x=600,y=200)
		self.perimetre=Label(self.fp,text="perimetre = ",font='calibri 20')
		self.perimetre.place(x=600,y=250)
		self.longeur=Label(self.fp,text="longeur = ",font='calibri 20')
		self.longeur.place(x=600,y=300)
		self.largeur=Label(self.fp,text="largeur = ",font='calibri 20')
		self.largeur.place(x=600,y=350)
		self.ccg=Label(self.fp,text="CCG KG = ",font='calibri 20')
		self.ccg.place(x=600,y=400)
		fileMenu1.configure(menu = me2)
		fileMenu1.grid(row=0,column=1)
		self.fond=Canvas(self.fp,bg="turquoise",widt=500,height=700)
		self.fond.place(x=0,y=30)
		self.s=0
		self.a,self.b,self.u=[],[],[]
		self.fp.mainloop()
	def nouveau(self):
		self.s=0
		self.a,self.b,self.u=[],[],[]
		file_name=askopenfilename()
		im1=Image.open(file_name)
		im2=im1.resize((500,700))
		photo=ImageTk.PhotoImage(im2)
		self.fond.create_image(250, 350, image=photo)
		self.fond.place(x=0,y=30)
		self.etat_dig=0
		self.fond.mainloop()
	def cercle(self,can, x, y, r,color="red"):
	#"dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
		can.create_oval(x-r, y-r, x+r, y+r,fill=color)
	def ligne(self, x, y):
		self.create_line(x,y1,x,y2)
	
	def put(self,event):
		
		if event.x<500 and event.y>30:
			print("x = ",event.x," y = ",event.y)
			self.a.append(event.x)
			self.b.append(event.y)
			#print("lena",len(self.a))
			if len(self.a)+len(self.b)>=4:
				self.s+=self.distance(self.a[len(self.a)-2],self.a[len(self.a)-1],self.b[len(self.b)-2],self.b[len(self.b)-1])
			self.u.append((self.a[(len(self.a)-1)],self.b[(len(self.b)-1)]))
			self.cercle(self.fond,self.a[-1],self.b[-1],1)
			#print("s = ",self.u)
			#print(self.s/23.5," cm ")
	def digitaliser(self):
		if self.etat_dig==0:
			self.fp.config(cursor="tcross")
			self.s=0
			self.a,self.b,self.u=[],[],[]
			self.bin=self.fp.bind("<Button-1>",self.put)
			self.etat_dig=1
		else:
			self.fp.config(cursor="arrow")
			self.bin=self.fp.bind("<Button-1>",self.rien)
			self.etat_dig=0


	def rien(self,event):
		""
	def distance(self,x1,x2,y1,y2):
		return ((x2-x1)**2+(y2-y1)**2)**0.5
	#Aire avec fonction 
	def aire(self,f,a,b,n):
		s,pas=0,(b-a)/n
		while n>0 :
			u,v=a+pas*n,a+pas*(n-1)
			s+=(pas*(f(u)+f(v)))/2
			n-=1
		return s

	def aire2(self,tab_points):
		res=0
		tab_points=sorted(tab_points)
		for i in range(len(tab_points)-1):
			pas=tab_points[i+1][0]-tab_points[i][0]
			res+=(tab_points[i][1]+tab_points[i+1][1])*pas/2
		return res

	def det_points_part(self,droit_sep,tab_cont):
		parts=([],[])
		for i in range(len(tab_cont)):
			if droit_sep(tab_cont[i][1])>tab_cont[i][1]:
				parts[0].append(tab_cont[i])
			elif droit_sep(tab_cont[i][1])<tab_cont[i][1]:
				parts[1].append(tab_cont[i])
			else:
				parts[0].append(tab_cont[i])
				parts[1].append(tab_cont[i])
		return parts

	def det_pts_separation(self,tab_cont):
		return (min(tab_cont),max(tab_cont))
	def l(self,tx,x):
		res=""
		val=1
		for i in range(len(tx)):
			if tx[i]!=x:
				if tx[i]!=0:
					res+="*(x"+str(-tx[i])+")"
				else:
					res+="*x"
				val*=(x-tx[i])
		return "(1/"+str(val)+")"+res
	def pl(self,t):
		p=""
		tx=[t[i][0] for i in range(len(t))]
		for i in range(len(t)):
			if t[i][1]!=0:
				p+=str(t[i][1])+"*"+self.l(tx,t[i][0])+"+"
		return p[:len(p)-1]
	def calculer (self):
		self.s=0
		print(self.u)

		if len(self.a)+len(self.b)>=4:

			for i in range(len(self.a)-1):

				self.s+=self.distance(self.a[i],self.a[i+1],self.b[i],self.b[i+1])

			perimetre=self.s/23.5
			self.perimetre.configure(text="perimetre = "+str(perimetre)+" cm")
			pts=self.det_pts_separation(self.u)
			ds=lambda x : eval(self.pl(pts))
			p1,p2=self.det_points_part(ds,self.u)
			ap1,ap2,ads=self.aire2(p1),self.aire2(p2),self.aire2([p1[0],p1[-1]])
			self.aire=((ads-ap1)+(ap2-ads))/23.5**2
			self.surface.configure(text="surface = "+str(self.aire)+" cm^2")
			self.longeur.configure(text="Longeur = "+str((perimetre+(perimetre**2-16*self.aire)**0.5)/4)+" cm")
			self.largeur.configure(text="Largeur = "+str((perimetre-(perimetre**2-16*self.aire)**0.5)/4)+" cm")
			self.ccg.configure(text="CCG KG = "+str(0.28*perimetre/self.aire**0.5))


if __name__=="__main__":
	from tkinter import*
	from time import*
	from random import*
	from tkinter.messagebox import askyesno
	import matplotlib.pyplot as pyplot
	import matplotlib.image as mpimg
	from PIL import Image, ImageTk
	from tkinter.filedialog import askopenfilename
	from tkinter.messagebox import *
	HydroDk()

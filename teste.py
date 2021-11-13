#################
# 2021 - PU4THZ #
#################

###################
# SIMULADOR REESA #
###################

import numpy as np
import matplotlib.pyplot as plt

# unidades & constantes
cm = 1e-2 #m
mm = 1e-3 #m

c = 3e8 #m/s
pi = np.pi



class Solver:
   def __init__ (self,N,F,Lx,Ly,unit=mm):
       self.unit = unit
       self.lamb = c/F/self.unit
       self.N = N
       self.Lx = Lx
       self.Ly = Ly
       
       self.dx = self.lamb/20

       self.extent = [self.lamb*-Lx/2,self.lamb*Lx/2,-Ly/2*self.lamb,Ly/2*self.lamb]

       
       self.x,self.y = np.meshgrid(np.arange(self.lamb*-Lx/2,self.lamb*Lx/2,self.dx),np.arange(-Ly/2*self.lamb,Ly/2*self.lamb,self.dx))

       print(self.lamb)
       print(self.unit)
       print(self.dx)
   def setAngle(self,ph):
       self.p0 = ph
       self.ph = (2*pi/self.lamb*self.lamb/2*np.sin(ph/180*pi))*180/pi
       self.phases = [((i+self.N//2)*self.ph%360,((i/2)+2/self.N)*self.lamb) for i in range(-self.N//2,self.N//2)]
      

   def Simulate(self):
       self.pwr = [np.sin(2*pi/self.lamb*np.sqrt((self.x+q)**2+self.y**2)+(pi*p/180)) for p,q in self.phases]
    
       # soma de todas as antenas 
       self.tp = np.sum(self.pwr,axis=0)

   def Plot(self,num=25):
       plt.ion()
       plt.clf()
       self.fig, self.ax = plt.subplots(num=1)
       pwr = np.abs(self.tp)
       plt.imshow(pwr/np.max(pwr),extent=self.extent,origin='lower')
       
       for a in np.linspace(-pi,pi,num)+pi/2:
           x,y = [[0,self.extent[1]*np.cos(a)], [0,self.extent[3]*np.sin(a)]]

           label = f'{np.degrees(a-pi/2):.1f}'
           xylabel = ((x[0]+x[1])/2.0, (y[0]+y[1])/1.5)

           plt.plot(x,y,'k--')
           self.ax.annotate(label, xy=xylabel, ha='center', va='center')

       # plota as antenas (ponto vermelho)
       
       #[plt.plot(q,0,'ro') for p,q in self.phases]
      
       plt.title(f'Ângulo desejado: {self.p0:.1f}',fontsize=20)
       
     
       leng = int(self.tp.shape[0]//2)
       angle = np.linspace(0,2*pi,leng)
       ax,bx = (leng*np.sin(angle)+leng-1).astype(int),(leng*np.cos(angle)+leng-1).astype(int)
       qx = [(ax,bx)]
       power = np.asarray([np.abs(self.tp[xx,yy]) for xx,yy in qx])[0]
       plt.plot(-self.extent[0]*power/np.max(power)*np.cos(angle),-self.extent[0]*power/np.max(power)*np.sin(angle),'r')
       plt.ylim(0,self.extent[1])
       plt.show()
       plt.pause(0.001)

fdtd = Solver(8, 1.7e9, 20, 20)

for i in range(0,360,1):
   fdtd.setAngle(i)
   fdtd.Simulate()
   fdtd.Plot()
   if(i%16==0):
      print(int(i/360*100),"% done.")




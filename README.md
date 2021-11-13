# phasedarray
Python - Phased Array sim.

![image](https://user-images.githubusercontent.com/58897843/141657605-c5da0072-cffd-416e-9f33-741b6cf58d45.png)

example: 

# Cria um solver com 8 antenas, 1.79 GHz, grade 20x20
fdtd = Solver(8, 1.7e9, 20, 20)

# main loop


#for i in range(0,360,1):
   #fdtd.setAngle(i)
   #fdtd.Simulate()
   #fdtd.Plot()
   #if(i%16==0):
      #print(int(i/360*100),"% done.")

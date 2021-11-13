# phasedarray
Python - Phased Array sim.

![image](https://user-images.githubusercontent.com/58897843/141658053-4b2cb75f-d344-4d3c-9eaa-75fd925bad3d.png)


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

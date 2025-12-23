import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate(sim):
  # create fig 
  fig, ax = plt.subplots()

  # set limits
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 100)

  # plot
  vehicle_dot = ax.plot([], [], "bo", label="Vehicle")[0]

  def update(frame):
   sim.step()

   x,y = sim.state.position()
   print(x,y)

   vehicle_dot.set_data([x], [y])

   return [vehicle_dot]

  ani = FuncAnimation(
        fig,
        update,
        frames=50,
        interval=50,
        blit=True
    )
  
  plt.show()
  






  
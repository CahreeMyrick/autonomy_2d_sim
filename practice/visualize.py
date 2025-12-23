import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate():
  # create fig 
  fig, ax = plt.subplots()
  x0, y0 = 10, 10

  # set limits
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 100)

  # plot
  point = ax.plot([x0], [y0], "bo")[0]

  def update(frame):
    x = x0 + frame
    y = y0 + frame ** 2 / 100
    
    point.set_data([x], [y])

    return [point]
  
  ani = FuncAnimation(
        fig,
        update,
        frames=50,
        interval=50,
        blit=True
    )
  
  plt.show()
  
animate()






  
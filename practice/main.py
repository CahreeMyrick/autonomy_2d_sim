from state import VehicleState
from visualize import animate
from simulator import Simulator

def main():
  state = VehicleState(x=10, y=10, theta=.3, v=2.0, v_max=10)

  sim = Simulator(state=state, omega=.1, dt=.1, a=0.2)

  animate(sim)

if __name__ == "__main__":
  main()
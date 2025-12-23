class Simulator:
  def __init__(self, state, omega, dt, a):
    self.state = state
    self.omega = omega
    self.dt = dt
    self.a = a
  
  def step(self):
    self.state.step(self.omega, self.a , self.dt)
    
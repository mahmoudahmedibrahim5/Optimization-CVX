import cvxpy as cp
import math

L = cp.Variable(pos = True)
C = cp.Variable(pos = True)
Fs = cp.Variable(pos = True)

Vi = 10     # 10 V
Io = 10     # 10 A
deltaI = 1.5

# MOSFET Variables
D = 0
RDS = 5.2e-3    # 5 milli ohm
Qrr = 50e-9
TswON = 10e-8
TswOFF = 10e-8
Vf = 0.9

RL = 2 * math.pi * Fs * L
RC = 1 / (2 * math.pi * Fs * C)

PON = (Io**2 + (deltaI**2) / 12) * D * RDS
PSW = Vi * (Io - deltaI / 2) * TswON * Fs + Vi * (Io + deltaI / 2) * TswOFF * Fs

# Power Losses
PQ1 = PON + PSW
Pd = Vf * Io * (1 - D) + Qrr * Vi * Fs
Pind = (Io**2 + (deltaI**2) / 12) * RL
Pcond = ((deltaI**2) / 12) * RC

# Total Power Loss
Pbuck = PQ1 + Pd + Pind + Pcond


objective = cp.Minimize(Pbuck)

constraints = [
    
]

problem = cp.Problem(objective, constraints)

result = problem.solve(gp = True)

print("Optimal power loss: ", result)
print("Optimal Inductance: ", L)
print("Optimal Capacitance: ", C)
print("Optimal Frequency: ", Fs)
import cvxpy as cp
import math

# Optimization variables
L = cp.Variable(pos = True)
C = cp.Variable(pos = True)
Fs = cp.Variable(pos = True)

# Electrical Characteristic
Vi = 10     # 10 V
Io = 10     # 10 A
deltaI = 1.5

# MOSFET Variables
D = 1
RDS = 5.2e-3    # 5 milli ohm
Qrr = 50e-9
TswON = 10e-8
TswOFF = 10e-8
Vf = 0.9

# Impedance
RL = 2 * math.pi * Fs * L
RC = 1 / (2 * math.pi * Fs * C)

# Power Losses
PON = (Io**2 + (deltaI**2) / 12) * D * RDS
PSW = Vi * (Io - deltaI / 2) * TswON * Fs + Vi * (Io + deltaI / 2) * TswOFF * Fs
PQ1 = PON + PSW
Pd = Vf * Io * (1 - D) + Qrr * Vi * Fs
Pind = (Io**2 + (deltaI**2) / 12) * RL
Pcond = ((deltaI**2) / 12) * RC

# Total Power Loss
Pbuck = PQ1 + Pd + Pind + Pcond

if __name__ == "__main__":
    
    objective = cp.Minimize(Pbuck)

    constraints = [
        L >= 0.1e-6,
        L <= 10e-3,
        C >= 0.1e-6,
        C <= 100e-6,
        Fs >= 10000,
        Fs <= 800000
    ]

    problem = cp.Problem(objective, constraints)

    result = problem.solve(gp = True)

    print("Optimal power loss: ", result)
    print("Optimal Inductance: ", L.value)
    print("Optimal Capacitance: ", C.value)
    print("Optimal Frequency: ", Fs.value)
    
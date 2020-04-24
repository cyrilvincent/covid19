import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import functools

#https://interstices.info/modeliser-la-propagation-dune-epidemie/
# Sain Contaminé Infecté Rétabli
class SCIRE:

    def __init__(self, S0 = 1, C0 = 0, I0 = 0, r0 = 3.3, v = 5.1, lmbda = 15, mu = 0.005):
        self.S = S0
        self.C = C0
        self.I = I0
        self.R = 0
        self.DC = 0
        self.beta = r0 / (lmbda / v)
        self.v = v
        self.lmbda = lmbda
        self.mu = mu
        self.fdsdt = lambda S, I: -self.beta * I * S  # ds/dt
        self.fdcdt = lambda S, C, I,: self.beta * I * S - C / v  # dc/dt
        self.fdidt = lambda C, I: C / v - I / self.lmbda - self.mu * I  # dc/dt
        self.fdrdt = lambda I: -I / self.lmbda #dr/dt
        self.fddcdt = lambda I: self.mu * I / lmbda #ddc/dt

    def computedt(self):
        self.S += self.fdsdt(self.S, self.I)
        self.C += self.fdcdt(self.S, self.C, self.I)
        self.I += self.fdidt(self.C, self.I)
        self.R += self.fdrdt(self.I)
        self.DC += self.fddcdt(self.I)

    def compute(self, dt):
        scires = []
        for _ in range(dt):
            self.computedt()
            scires.append(self.clone())
        return scires

    def clone(self):
        scire = SCIRE()
        scire.S = self.S
        scire.C = self.C
        scire.I = self.I
        scire.DC = self.DC
        return scire

if __name__ == '__main__':
    nbfrench = 67000000
    I0 = 10 / nbfrench #Taux Infection
    C0 = I0 * 4 #Taux Contaminé
    S0 = 1 - I0 - C0 #Taux Sain
    beta = 0.22
    lmbda = 15 # Durée d'infection
    v = 5.1 # Nb incubation
    R0 = 3.3
    beta  = R0 / lmbda
    print(beta)
    mu = 0.005 # Taux mortalité
    scire = SCIRE(S0,C0,I0,r0=R0,v=v,lmbda=lmbda,mu=mu)
    scires = scire.compute(250) #45-15 ou #250 pointe à 1300000 infectés, 260000 réa, 500000 morts en 250 jours, pointe à 13000 morts/jour
    ctot = 1 - np.array([x.S for x in scires])
    c = np.array([x.C for x in scires])
    i = np.array([x.I for x in scires])
    dc = np.array([x.DC for x in scires])
    #plt.plot(ctot*nbfrench, label="Contact avec virus")
    plt.plot(i*nbfrench, label="Infectés")
    plt.plot(dc*nbfrench, label="Décès")
    plt.legend()
    plt.show()

    # Confinement
    I0 = 2281 * 10 / nbfrench #Taux Infection
    C0 = I0 * 6 #Taux Contaminé
    S0 = 1 - I0 - C0 #Taux Sain
    scire = SCIRE(S0, C0, I0, r0=0.5,v=v,lmbda=lmbda,mu=mu)
    scires = scire.compute(91-45)
    ctot = 1 - np.array([x.S for x in scires])
    c = np.array([x.C for x in scires])
    i = np.array([x.I for x in scires])
    dc = np.array([x.DC for x in scires]) + 2281 / nbfrench
    plt.plot(i * nbfrench, label="Infectés")
    plt.plot(dc * nbfrench, label="Décès")
    plt.legend()
    plt.show()

    # Déconfinement
    C0 = ((23000 * 100) - 180000) / nbfrench  # Taux Contaminé
    I0 = C0 / 6  # Taux Infection
    S0 = 1 - I0 - C0  # Taux Sain
    scire = SCIRE(S0, C0, I0, r0=0.5,v=v,lmbda=lmbda,mu=mu)
    scires = scire.compute(250)
    ctot = 1 - np.array([x.S for x in scires])
    c = np.array([x.C for x in scires])
    i = np.array([x.I for x in scires])
    dc = np.array([x.DC for x in scires]) + 23000 / nbfrench
    plt.plot(i * nbfrench, label="Infectés")
    plt.plot(dc * nbfrench, label="Décès")
    plt.legend()
    plt.show()


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import functools

#https://interstices.info/modeliser-la-propagation-dune-epidemie/
# Sain Contaminé Infecté Rétabli
class SCIRE:

    def __init__(self, S0 = 1, C0 = 0, I0 = 0, R0 = 0, beta = 1, v = 4.1, lmbda = 14, mu = 0.01):
        self.S = S0
        self.C = C0
        self.I = I0
        self.R = R0
        self.DC = 0
        self.beta = beta
        self.v = v
        self.lmbda = lmbda
        self.mu = mu
        self.fdsdt = lambda S, I: -self.beta * I * S  # ds/dt
        self.fdcdt = lambda S, C, I,: self.beta * I * S - C / v  # dc/dt
        self.fdidt = lambda C, I: C / v - I / self.lmbda - self.mu * I  # dc/dt
        self.fdrdt = lambda I: -I / self.lmbda #dr/dt
        self.fddcdt = lambda I: self.mu * I / l #ddc/dt

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
    beta = 0.22 # Coef contagieusité (aka R0) / tx de contact J45:DC286:Contact:2860:Beta = 0.22
    v = 4.1 # Nb incubation
    l = 14 # Durée d'infection
    mu = 0.01 # Taux mortalité
    scire = SCIRE(S0,C0,I0,beta=beta)
    scires = scire.compute(250) #45 ou #250 pointe à 1300000 infectés, 260000 réa, 500000 morts en 250 jours, pointe à 13000 morts/jour
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
    scire = SCIRE(S0, C0, I0, beta=beta*0.98)
    scires = scire.compute(91-45)  # 250 pointe à 1300000 infectés, 260000 réa, 500000 morts en 250 jours, pointe à 13000 morts/jour
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
    scire = SCIRE(S0, C0, I0, beta=beta * 0.25) # 0.99 0.25 0.1
    scires = scire.compute(250)  # 250 pointe à 1300000 infectés, 260000 réa, 500000 morts en 250 jours, pointe à 13000 morts/jour
    ctot = 1 - np.array([x.S for x in scires])
    c = np.array([x.C for x in scires])
    i = np.array([x.I for x in scires])
    dc = np.array([x.DC for x in scires]) + 2281 / nbfrench
    plt.plot(i * nbfrench, label="Infectés")
    plt.plot(dc * nbfrench, label="Décès")
    plt.legend()
    plt.show()


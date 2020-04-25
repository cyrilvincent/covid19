from __future__ import annotations
from typing import List, Callable
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import functools

class SCIRE:
    """
    SCIRE+ Model
    Sain Contaminé Infecté Rétabli Etendu
    Improvments: dr & fs
    https://interstices.info/modeliser-la-propagation-dune-epidemie/
    :author Cyril Vincent www.CyrilVincent.com
    """

    def __init__(self,
                 S:float = 1,
                 C:float = 0,
                 I:float = 0,
                 R:float = 0,
                 r0:float = 3.3,
                 v:float = 2,
                 lmbda:float = 15,
                 mu:float = 0.005,
                 dr:float = 0,
                 fs:Callable[[float], float] = lambda _: 0):
        """
        :param S: Sain
        :param C: Contaminé
        :param I: Infecté
        :param R: Rétablis
        :param r0: nombre moyen de contaminé par un infecté
        :param v: durée incubation sans être contagieux
        :param lmbda: durée moyenne de contagieusité
        :param mu: taux de mortalité
        :param dr: facteur de décroissance de R par rapport à R0
        :param fs: fonction de saisonalité
        """
        self.S = S
        self.C = C
        self.I = I
        self.R = R
        self.DC = 0
        self.beta = r0 / lmbda
        self.v = v
        self.lmbda = lmbda
        self.mu = mu
        self.dr = dr
        self.fs = fs
        self.i = 0 #dt
        self.fdsdt = lambda S, I: -(self.beta + self.fs(self.i)) * I * S  # ds/dt
        self.fdcdt = lambda S, C, I,: (self.beta + self.fs(self.i)) * I * S - C / v  # dc/dt
        self.fdidt = lambda C, I: C / v - I / self.lmbda - self.mu * I  # dc/dt
        self.fdrdt = lambda I: -I / self.lmbda #dr/dt
        self.fddcdt = lambda I: self.mu * I / self.lmbda #ddc/dt
        self.fdbetadt = lambda : -self.dr / self.lmbda #dbeta/dt

    def _computedt(self):
        """
        Compute the model by adding 1 day
        """
        self.S += np.min(self.fdsdt(self.S, self.I), 0)
        self.C += np.max(self.fdcdt(self.S, self.C, self.I), 0)
        self.I += np.max(self.fdidt(self.C, self.I), 0)
        self.R += self.fdrdt(self.I)
        self.DC += np.max(self.fddcdt(self.I), 0)
        self.beta += self.fdbetadt()
        self.i += 1

    def compute(self, nbday:int)->List['SCIRE']:
        """
        Compute the model
        :param nbday: the number of day to compute
        :return: List[SCIRE]
        """
        scires = []
        for _ in range(nbday):
            self._computedt()
            scires.append(self.clone())
        return scires

    def clone(self)->SCIRE:
        scire = SCIRE()
        scire.S = self.S
        scire.C = self.C
        scire.I = self.I
        scire.DC = self.DC
        return scire

if __name__ == '__main__':
    nbfrench = 67000000
    DC15 = 10
    notdetectedrate = 4
    lmbda = 15 # Durée d'infection contagieuse
    v = 2 # Durée incubation non contagieux
    R0 = 3.3
    beta  = R0 / lmbda
    print(beta)
    mu = 0.005 # Taux mortalité

    #Avant confinement D15->D45
    # I0 = DC15 / nbfrench  # Taux Infection
    # C0 = I0 * notdetectedrate  # Taux Contaminé
    # S0 = 1 - I0 - C0  # Taux Sain
    # scire = SCIRE(S0,C0,I0,r0=R0,v=v,lmbda=lmbda,mu=mu)
    # scires = scire.compute(250) #45-15 250
    # ctot = 1 - np.array([x.S for x in scires])
    # c = np.array([x.C for x in scires])
    # i = np.array([x.I for x in scires])
    # dc = np.array([x.DC for x in scires])
    # plt.plot(ctot*nbfrench, label="Contact avec virus")
    # plt.plot(i*nbfrench, label="Infectés")
    # plt.plot(dc*nbfrench, label="Décès")
    # plt.legend()
    # plt.show()

    # Confinement
    # DC45 = 2281
    # I0 = (DC45 / mu) / nbfrench #Taux Infection
    # notdetectedrate = 6
    # C0 = I0 * notdetectedrate #Taux Contaminé
    # S0 = 1 - I0 - C0 #Taux Sain
    # scire = SCIRE(S0, C0, I0, r0=0.8,v=v,lmbda=lmbda,mu=mu)
    # scires = scire.compute(118-45)
    # i = np.array([x.I for x in scires])
    # dc = np.array([x.DC for x in scires]) + DC45 / nbfrench
    # plt.plot(i * nbfrench, label="Infectés")
    # plt.plot(dc * nbfrench, label="Décès")
    # plt.legend()
    # plt.show()

    # Déconfinement
    DC128 = 23000
    R128 = 180000
    rrate = 0.5 # 0.1 0.5
    r128 = 0.5 #0.5
    C0 = ((DC128 / mu) - R128) / nbfrench * rrate
    I0 = C0 * rrate / notdetectedrate
    S0 = 1 - I0 - C0
    r0 = R0 * r128 * rrate
    fsamort = 4 #1,2,4
    R0 /= fsamort
    fsummer = lambda x : -np.sin((x + 118 - 365 / 4 - 30) * 2 * np.pi / 365) * R0 / fsamort
    print(fsummer(np.arange(365)))
    scire = SCIRE(S0, C0, I0, r0=r0 * rrate, v=v, lmbda=lmbda, mu=mu, dr=-0.2, fs = fsummer) #0.1 0 -0.1
    scires = scire.compute(365)
    ctot = 1 - np.array([x.S for x in scires])
    c = np.array([x.C for x in scires])
    i = np.array([x.I for x in scires])
    dc = np.array([x.DC for x in scires]) + DC128 / nbfrench
    plt.plot(i * nbfrench, label="Infectés")
    plt.plot(dc * nbfrench, label="Décès")
    plt.xlabel("Nb jour depuis le ll mai (J+128)")
    plt.ylabel("Nb cas & décès")
    plt.legend()
    plt.tight_layout()
    plt.show()

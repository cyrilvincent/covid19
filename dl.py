import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neural_network as nn
import warnings

d0 = datetime.date(2020,1,24)
iconf = 56
dconf = d0 + datetime.timedelta(days=iconf)
i10 = 15
d10 = d0 + datetime.timedelta(days=i10)
ilift = 41
dlift = d0 + datetime.timedelta(days=ilift)
print(f"Start date: {d0}")
ideconf = (datetime.date(2020,5,11) - d0).days
ijune = (datetime.date(2020,6,1) - d0).days

df = pd.read_csv("data/covid-france.txt")
print(df.shape)
df10 = df.loc[df.ix >= i10]
dfc = df.loc[df.ix >= iconf]
dflift = df.loc[df.ix >= ilift]
# fig, axs = plt.subplots(2,2, constrained_layout=True)
# axs[0,0].bar(np.arange(len(df.NbCas)), df.NbCas)
# axs[0,0].set_title='Nb cas par jour'
# axs[0,0].set_xlabel(f'jour depuis {d0}')
# axs[0,0].set_ylabel('Nb Cas')
# axs[1,0].bar(np.arange(len(df.DC)), df.DC)
# axs[1,0].set_title='Nb décès par jour'
# axs[1,0].set_xlabel(f'jour depuis {d0}')
# axs[1,0].set_ylabel('Nb Décès')
# axs[0,1].bar(np.arange(len(dflift.NbCas)), dflift.NbCas)
# axs[0,1].set_title='Nb Cas'
# axs[0,1].set_xlabel(f'jour depuis {dlift}')
# axs[0,1].set_ylabel('Nb Décès')
# axs[1,1].bar(np.arange(len(dflift.DC)), dflift.DC)
# axs[1,1].set_title='Nb décès par jour'
# axs[1,1].set_xlabel(f'jour depuis {dlift}')
# axs[1,1].set_ylabel('Nb Décès')
#plt.show()

# fig, axs = plt.subplots(2,1, constrained_layout=True)
# axs[0].bar(np.arange(len(dfc.NbCas)), dfc.NbCas)
# axs[0].set_title='Nb cas par jour'
# axs[0].set_xlabel(f'jour depuis {dconfinement}')
# axs[0].set_ylabel('Nb Cas')
# axs[1].bar(np.arange(len(dfc.DC)), dfc.DC)
# axs[1].set_title='Nb décès par jour'
# axs[1].set_xlabel(f'jour depuis {dconfinement}')
# axs[1].set_ylabel('Nb Décès')
#plt.show()

h=(1,)
#warnings.filterwarnings('ignore')
modelnb10 =nn.MLPClassifier(h)
x10 = df10.ix.values.reshape(-1,1)
y = df10.NbCas
modelnb10.fit(x10, y)
scorenb10 = modelnb10.score(x10,y)
modeldc10 =nn.MLPClassifier(h)
y = df10.DC
modeldc10.fit(x10, y)
scoredc10 = modeldc10.score(x10,y)
modelnblift =nn.MLPClassifier(h)
xlift = dflift.ix.values.reshape(-1,1)
y = dflift.NbCas
modelnblift.fit(xlift, y)
scorenblift = modelnblift.score(xlift,y)
modeldclift =nn.MLPClassifier(h)
y = dflift.DC
modeldclift.fit(xlift, y)
scoredclift = modeldclift.score(xlift,y)
fig, axs = plt.subplots(2,2, constrained_layout=True)
axs[0,0].bar(np.arange(len(df10.NbCas)), df10.NbCas)
axs[0,0].plot(modelnb10.predict(x10))
axs[0,0].set_title='Nb cas par jour'
axs[0,0].set_xlabel(f'jour depuis {d10}, score={scorenb10 * 100:.0f}%')
axs[0,0].set_ylabel('Nb Cas')
axs[1,0].bar(np.arange(len(df10.DC)), df10.DC)
axs[1,0].plot(modeldc10.predict(x10))
axs[1,0].set_title='Nb décès par jour'
axs[1,0].set_xlabel(f'jour depuis {d10}, score={scoredc10 * 100:.0f}%')
axs[1,0].set_ylabel('Nb Décès')
axs[0,1].bar(np.arange(len(dflift.NbCas)), dflift.NbCas)
axs[0,1].plot(modelnblift.predict(xlift))
axs[0,1].set_title='Nb Cas'
axs[0,1].set_xlabel(f'jour depuis {dlift}, score={scorenblift * 100:.0f}%')
axs[0,1].set_ylabel('Nb Décès')
axs[1,1].bar(np.arange(len(dflift.DC)), dflift.DC)
axs[1,1].plot(modeldclift.predict(xlift))
axs[1,1].set_title='Nb décès par jour'
axs[1,1].set_xlabel(f'jour depuis {dlift}, score={scoredclift * 100:.0f}%')
axs[1,1].set_ylabel('Nb Décès')
plt.show()

modelnbc =nn.MLPClassifier(h)
xc = dfc.ix.values.reshape(-1,1)
y = dfc.NbCas
modelnbc.fit(xc, y)
scorenbc = modelnbc.score(xc,y)
modeldcc =nn.MLPClassifier(h)
y = dfc.DC
modeldcc.fit(xc, y)
scoredcc = modeldcc.score(xc,y)
fig, axs = plt.subplots(2,1, constrained_layout=True)
axs[0].bar(np.arange(len(dfc.NbCas)), dfc.NbCas)
axs[0].plot(modelnbc.predict(xc))
axs[0].set_title='Nb cas par jour'
axs[0].set_xlabel(f'jour depuis {dconf}, score={scorenbc * 100:.0f}%')
axs[0].set_ylabel('Nb Cas')
axs[1].bar(np.arange(len(dfc.DC)), dfc.DC)
axs[1].plot(modeldcc.predict(xc))
axs[1].set_title='Nb décès par jour'
axs[1].set_xlabel(f'jour depuis {dconf}, score={scoredcc * 100:.0f}%')
axs[1].set_ylabel('Nb Décès')
plt.show()

print("Prévisions")
print(modelnb10.predict([[ideconf]])[0], modeldc10.predict([[ideconf]])[0])
print(modelnblift.predict([[ideconf]])[0], modeldclift.predict([[ideconf]])[0])
print(modelnbc.predict([[ideconf]])[0], modeldcc.predict([[ideconf]])[0])
print(modelnblift.predict([[ijune]])[0], modelnbc.predict([[ijune]])[0])

plt.bar(np.arange(len(dfc.NbCas)), dfc.NbCas)
plt.plot(modelnbc.predict(np.arange(dfc.ix.values[0], dfc.ix.values[0] + 60).reshape(-1,1)))
plt.title='Nb Cas'
plt.xlabel(f'jour depuis {dconf}, score={scorenbc * 100:.0f}%')
plt.ylabel('Nb cas')
plt.show()

plt.bar(np.arange(len(dfc.DC)), dfc.DC)
plt.plot(modeldcc.predict(np.arange(dfc.ix.values[0], dfc.ix.values[0] + 40).reshape(-1,1)))
plt.title='Nb Décès'
plt.xlabel(f'jour depuis {dconf}, score={scoredcc * 100:.0f}%')
plt.ylabel('Nb cas')
plt.show()

print(f"Nb Cas au déconfinement: {modelnbc.predict([[ideconf]])[0]:.0f}")
print(f"Nb Décès au déconfinement: {modeldcc.predict([[ideconf]])[0]:.0f}")

tx = 0.005
nbdc = sum(df["DC"])
print(f"Nb décès: {nbdc:.0f}")
print(f"Nb infection: {nbdc * 1/tx:.0f}")
print(f"Taux d'infection: {(nbdc * 1/tx) / 670000:.0f}%")
nbdcdeconf = modeldcc.predict(np.arange(ideconf).reshape(-1,1))
nbdcdeconf = sum(np.clip(nbdcdeconf,0,np.inf))
nbnbdeconf = modelnbc.predict(np.arange(ideconf).reshape(-1,1))
nbnbdeconf = sum(np.clip(nbnbdeconf,0,np.inf))
print(f"Nb cas au déconfinement: {nbnbdeconf:.0f}")
print(f"Nb décès au déconfinement: {nbdcdeconf:.0f}")
print(f"Nb infection au déconfinement: {nbdcdeconf * 1/tx:.0f}")
print(f"Taux d'infection au déconfinement: {(nbdcdeconf * 1/tx) / 670000:.0f}%")
nbdcara = 1103
txara = nbdcara / 20796
print(f"Nb décès ARA: {nbdcara:.0f}")
print(f"Nb infection ARA: {nbdcara * 1/tx:.0f}")
print(f"Taux d'infection ARA: {(nbdcara * 1/tx) / 80000:.0f}%")
print(f"Nouveau cas par jour en france: {modelnbc.predict([[ideconf]])[0]:.0f}")

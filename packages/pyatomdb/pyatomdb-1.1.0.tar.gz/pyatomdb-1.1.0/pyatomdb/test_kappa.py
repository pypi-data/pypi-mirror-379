import pyatomdb, numpy
import matplotlib.pyplot as plt

a = pyatomdb.spectrum.KappaSession()
ebins = numpy.linspace(0.1,1.0,1001)

a.set_response(ebins, raw=True)
s=a.return_spectrum(1.0,4.0)
s = numpy.append(s[0],s)

b = pyatomdb.spectrum.CIESession()
b.set_response(ebins, raw=True)
t=b.return_spectrum(1.0)
t = numpy.append(t[0],t)


fig = plt.figure()
fig.show()
ax = fig.add_subplot(111)
ax.plot(ebins, s, drawstyle='steps')
ax.plot(ebins, t, drawstyle='steps')

plt.draw()
zzz=input()

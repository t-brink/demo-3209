#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot

scale, Eorig, pxx_orig, pzz_orig = np.loadtxt("energy.orig.dat", unpack=True)
scale2, Efixed, pxx_fixed, pzz_fixed = np.loadtxt("energy.fixed.dat", unpack=True)

assert np.allclose(scale, scale2)

dE = Eorig - Efixed

pyplot.figure()
pyplot.plot(scale-1, dE*1000, "C0-")

pyplot.xlabel("strain")
pyplot.ylabel("ΔE/atom (meV)")

pyplot.grid()


pyplot.figure()
pyplot.plot(scale-1, pxx_orig*0.0001, "C1-", label="orig")
pyplot.plot(scale-1, pxx_fixed*0.0001, "C2-", label="fixed")

pyplot.xlabel("strain")
pyplot.ylabel("Pxx (GPa)")
pyplot.legend()

pyplot.xlim(0.1, 0.125)
pyplot.ylim(-22.6, -21.9)

pyplot.grid()


pyplot.show()

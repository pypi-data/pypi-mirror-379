import pyatomdb

Z = 6
T = 1e7
T_init='ionizing'
tau = False

dc={}

#d = pyatomdb.apec.calc_full_ionbal(9e4, Zlist=[Z], tau=1e10, cie=False, init_pop='ionizing', datacache=dc)
slow = pyatomdb.apec.return_ionbal(Z, T, init_pop=T_init, tau=tau,\
                       teunit='K', \
                       datacache=dc, fast=False, extrap=True,\
                       allowmulti=True)

fast = pyatomdb.apec.return_ionbal(Z, T, init_pop=T_init, tau=tau,\
                       teunit='K', \
                       datacache=dc, fast=True, extrap=True,\
                       allowmulti=True)
                       
print('slow',slow)
print('fast',fast)

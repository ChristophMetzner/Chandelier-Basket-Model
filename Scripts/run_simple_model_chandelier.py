# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 15:32:44 2017

@author: Christoph Metzner
"""

from simple_model_chandelier_class import simpleModelChandelier


# Parameters
n_ex    = 40  				# number of excitatory cells
n_bask  = 10 				# number of basket cells
n_chand = (n_ex/2)-n_bask# number of chandelier cells

eta     = 5.0  			# 
tau_R   = 0.1 				# 'synaptic rise time'
tau_ex  = 2.0   			# exc. 'synaptic decay time'
tau_bask = 8.0  	 		# inh. 'synaptic decay time'  for basket cell
tau_chand = 28.0          # inh. 'synaptic decay time'  for chandelier cell
    
factor = 1.0/((n_ex/20)**2) # factor to adjust the weights to network sizes different from 20 exc. cells
print factor

g_ee    = 0.015*factor			# E-E weight
g_eb    = 0.025*factor 			# default=0.025 E-B weight
g_ec    = 0.025*factor 			# default=0.025 E-C weight
g_be    = 0.015*factor 			# default=0.015 B-E weight
g_ce    = 0.08*factor 			# default=0.015 C-E weight
g_bb    = 0.02*factor 			# default=0.02 B-B weight
g_cc    = 0.02*factor 			# default=0.02 C-C weight
g_bc    = 0.02*factor 			# default=0.02 B-C weight
g_de    = 0.3                    # default=0.3 Drive-E weight
g_db    = 0.08           		 	# default=0.08 Drive-B weight
g_dc    = 0.08           			# default=0.08 Drive-C weight




#dt = 0.05				# time step
s=2**13
time 	= 500				# simulation stime (in ms) 
dt=float(time)/float(s)
print dt

b_ex    = -0.01 	# default=-0.01 applied current for exc. cells
b_bask   = -0.01 	# default=-0.01 applied current for basket cells
b_chand   = -0.01 	# default=-0.01 applied current for chandelier cells
drive_frequency = 40.0
background_rate = 33.3
A = 0.5 # default=0.5
seed = 1234567

filename = 'test'
directory = ''

model = simpleModelChandelier(n_ex,n_bask,n_chand,eta,tau_R,tau_ex,tau_bask,tau_chand,g_ee,g_eb,g_ec,g_be,g_ce,g_bb,g_cc,g_bc,g_de,g_db,g_dc,dt,b_ex,b_bask,b_chand,drive_frequency,background_rate,A,seed,filename,directory)

meg,ex,bask,chand = model.run(time,0,0,0,0)

pxx,freqs = model.calculatePSD(meg,time)
model.plotPSD(freqs*1000,pxx,50.0,0)



model.rasterPlot(ex,time,0,'ex')
model.rasterPlot(bask,time,0,'bask')
model.rasterPlot(chand,time,0,'chand')
model.plotMEG(meg,time,0)

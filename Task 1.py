#Neural network
import nengo
import numpy as np

model = nengo.Network("my first network")

with model:
    in100 = nengo.Node(100)
    
    layer1 = nengo.Ensemble(100,dimensions=1)
    layer2 = nengo.Ensemble(100,dimensions=1)
       
    nengo.Connection(in100,layer1)
    nengo.Connection(layer1,layer2)

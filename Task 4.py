import nengo
import numpy as np
from nengo.processes import Piecewise 

model = nengo.Network("my fourth network")

with model:
    inFun = nengo.Node(lambda t : t * 0.5)

    def show(t,x):
        if x * 0.5 < 10:
            show._nengo_html_= "<center><h1 style='color:red'>Low "+str(x)+"</h1></center>"
        else:
            show._nengo_html_= "<center><h1 style='color:green'>High "+str(x)+"</h1></center>"
            
    output = nengo.Node(show,size_in=1)
    
    nengo.Connection(inFun,output)

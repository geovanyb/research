import os
import pandas as pd
import numpy as np

def PbFuzzyClustering(data, Nc, m, iter_limit):
# Modelo de clusterização por linha
# O que deve ser feito iterativamente:
        # inicialmento setar os protótipos iniciais
        # calcular os pesos do cluster
        # reajustar os protótipos
    
    Nxy     = data.shape[1]
    Nd      = data.shape[0]
    Nb0     = int(Nd/Nc)
    dtb0    = [(Nb0*i,Nb0*i+1) for i in range(Nc)]
    weights = np.ones(Nc, Nd) # Vetor de pesos Protótipos x Pontos
    dist    = np.ones(Nc, Nd) # Vetor de distâncias Protótipos x Pontos
    betas   = np.empty((Nc,data.shape[1]), float)
    tx      = np.ones(Nc)
    
    i = 0
    for di in dtb0:
        dt      = np.array([data[di[0],:],data[di[1],:]])
        wt      = np.array([[1,1]])
        betas[i],tx[i],ty[i]  = np.array(__nbeta(dt,wt,m))
        i=+1
    
    iL = 0
    lim = 1
    while lim:
        # Cálculo dos novos pesos a partir das distâncias e estatísticas anteriores
        weights = __weightFuzzy(data,tx,ty,betas,m)
        # Cálculo dos novos betas a partir dos pesos e estatísticas
        betas, tx, ty = __nbeta(dt,weights,m)      
     
        iL += 1
        if iL = iter_limit:
            lim = 0
    
    del weights, Nxy,Nd,Nb0,dtb0,dist,tx,ty, iL, lim
    
    return betas
    
## Calculadora dos pesos
    
def __weightFuzzy(data, tx, ty, betas, m): # Função que atribui os pesos uij (ponto j para a protótipo i)
    g2   = np.empty((betas.shape[0],data.shape[0]))
    dad2 = np.empty((betas.shape[0],data.shape[0]))
    dist = np.empty((betas.shape[0],data.shape[0]))
    wt   = np.empty((betas.shape[0],data.shape[0]))
    
    dist = __distance(data,betas)    
    
    for bet in range(betas.shape[0]): 
        g2[bet,:]   = (data[:,0]-tx[bet])**2+(data[:,1]-ty[bet])**2
        dad2[bet,:] = dist[bet,:]**2+g2[bet,:]
        wt[bet,:]   = [(((dad2[bet,d]*dad2[:,d]**(-1))**(np.divide(1,(m-1)))).sum())**(-1) for d in range(dad2.shape[1])]
        
    return wt

## Calculadora dos novos protótipos

def __nbeta(dt,wt,m):
    tx, ty, Sxx, Syy, Sxy = __estatistics(data,Wf,m)
    alp = np.arctan(np.divide(-2*Sxy,(Syy-Sxx),out=np.ones_like(Syy-Sxx)*np.inf,where=(Syy-Sxx)!=0))/2
    rho = tx*np.cos(alp)+ty*np.sin(alp)
    
    return (np.array([[i,c] for i, c in zip(rho,alp)]), tx, ty)
    
## Calculadora das distâncias em relação à reta

def __distance(data,beta):
    d = np.empty((beta.shape[0],data.shape[0]))
    
    for i in range(beta.shape[0]):
        d[i,:] = beta[i,0]-data[:,0]*np.cos(beta[i,1])-data[:,1]*np.sin(beta[i,1])
        
    return d
## Função que entrega as estatísticas dos dados enviados (dados 2D)
def __estatistics(data, wF, m):
    tx  = np.empty((wF.shape[0],0))
    ty  = np.empty((wF.shape[0],0))
    Sxx = np.empty((wF.shape[0],0))
    Syy = np.empty((wF.shape[0],0))
    Sxy = np.empty((wF.shape[0],0))
    
    for bt in range(wF.shape[0]):
        tx  = np.append(tx,np.average(data[:,0],weights=wF[bt,:]**m))
        ty  = np.append(ty,np.average(data[:,1],weights=wF[bt,:]**m))
        Sxx = np.append(Sxx, (wF[bt,:]**m*(data[:,0]-tx[bt])**2).sum())
        Syy = np.append(Syy, (wF[bt,:]**m*(data[:,1]-ty[bt])**2).sum())
        Sxy = np.append(Sxy, (wF[bt,:]**m*(data[:,0]-tx[bt])*(data[:,1]-ty[bt])).sum())
        
    return tx, ty, Sxx, Syy, Sxy       
    

import os
import pandas as pd
import numpy as np

def PbFuzzyClustering(data, Nc, m, iter_limit):
# Modelo de clusterização por linha
# O que deve ser feito iterativamente:
        # inicialmento setar os protótipos iniciais
        # calcular os pesos do cluster
        # reajustar os protótipos
    
    Nc      = data.shape[1]
    Nd      = data.shape[0]
    Nb0     = int(Nd/Nc)
    dtb0    = [(Nb0*i,Nb0*i+1) for i in range(Nc)]
    weights = np.ones(Nc, Nd) # Vetor de pesos Protótipos x Pontos
    dist    = np.ones(Nc, Nd) # Vetor de distâncias Protótipos x Pontos
    betas   = np.array([])
    for di in dtb0:
        dt      = np.concatenate((data[di[0]],data[di[1]]),axis=0)
        betas   = np.append(betas,np.array(__nbeta(dt,weights,m)),axis=0)
    
    for i in range(Nd):
        dist[:i] = betas[:0]-data[:0]*np.cos(betas[:1])-data[:1]*np.sin(betas[:1])
    
    iL = 0
    lim = 1
    while lim:
        # Cálculo dos novos pesos a partir das distâncias e estatísticas anteriores
        Wf = __weightFuzzy(data,betai,g)
        # Cálculo das estatísticas com os novos pesos
        tx, ty, Sxx, Syy, Sxy = __estatistics(data,Wf,m)
        # Cálculo dos novos betas a partir dos pesos e estatísticas
        betas = __nbeta(data,tx,ty,Sxx,Syy,Sxy)
        # Cálculo das distâncias dos dados para os novos betas
        for i in range(Nd):
            dist[:i] = betas[:0]-data[:0]*np.cos(betas[:1])-data[:1]*np.sin(betas[:1])
        iL += 1
        if iL = iter_limit:
            lim = 0
        
def __weightFuzzy(data, tx, ty, dist, betai, betas, m): # Função que atribui os pesos uij (ponto j para a protótipo i)
        
    g2    = (data[:,0]-tx)**2+(data[:,1]-ty)**2
    dad2i = dist**2+g2
    for bet in betas: 
        fj  = bet[0] - row[0]*np.cos(bet[1])-dataj[1]*np.sin(bet[1])
        d2j = fj**2+g**2 
        
    return d

def __nbeta(data, wF, m):
    tx,ty,Sxx,Syy,Sxy = __estatistics(data, wF, m)
    alpi = np.arctan(-2*Sxy/(Syy-Sxx))/2
    rhoi = tx*np.cos(alpi)+ty*np.sin(alpi)
    
    return (rhoi,alpi)

def __distance(data,betai):
    d = betai[0]-data[0]*np.cos(betai[1])-data[1]*np.sin(betai[1])
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
    

import os
import pandas as pd
import numpy as np

def PbFuzzyClustering(data, Nc, m):
# Modelo de clusterização por linha
# O que deve ser feito iterativamente:
        # inicialmento setar os protótipos iniciais
        # calcular os pesos do cluster
        # reajustar os protótipos
    
    cD      = data.columns
    Nd      = data.size[0]
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
        
    while lim:
        # Cálculo dos novos pesos a partir das distâncias e estatísticas anteriores
        Wf = __weightFuzzy(data,betai,g)
        # Cálculo das estatísticas com os novos pesos
        tx  = np.average(data[0],weights=wF)
        ty  = np.average(data[1],weights=wF)
        Sxx = (un**m*(data[0]-tx)**2).sum()
        Syy = (un**m*(data[1]-ty)**2).sum()
        Sxy = (un**m*(data[0]-tx)*(data[1]-ty)).sum()
        # Cálculo dos novos betas a partir dos pesos e estatísticas
        betas = __nbeta(data,tx,ty,Sxx,Syy,Sxy)
        # Cálculo das distâncias dos dados para os novos betas
        for i in range(Nd):
            dist[:i] = betas[:0]-data[:0]*np.cos(betas[:1])-data[:1]*np.sin(betas[:1])
        
def __weightFuzzy(data, tx, ty, dist, betai, betas, m): # Função que atribui os pesos uij (ponto j para a protótipo i)
        
    g2    = (data[:0]-tx)**2+(data[0:1]-ty)**2
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

def __estatistics(data, wF, m):
    tx  = np.average(data[0],weights=wF**m)
    ty  = np.average(data[1],weights=wF**m)
    Sxx = (wF**m*(data[0]-tx)**2).sum()
    Syy = (wF**m*(data[1]-ty)**2).sum()
    Sxy = (wF**m*(data[0]-tx)*(data[1]-ty)).sum()
    return tx, ty, Sxx, Syy, Sxy        
    

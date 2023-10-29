# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:03:17 2023

@author: aile
"""

import numpy as np

class DistanceMeasurementMethods():
      
    #ÖKLİT MESAFESİ  : D(p, q) = √((q1 - p1)^2 + (q2 - p2)^2 + ... + (qn - pn)^2)

    def oklitMesafesi(vektor1,vektor2):
        
        if len(vektor1) != len(vektor2):
            raise ValueError("Vektorler ayni uzunlukta olmalidir!")
               
        mesafe = np.sqrt(sum(pow(x-y,2) for x,y in zip(vektor1,vektor2)))
        return mesafe
    
    
    
    
    #MANHATTAN MESAFESİ : D(p, q) = |q1 - p1| + |q2 - p2|
    
    def ManhattanMesafesi(vektor1,vektor2):
        if len(vektor1) != len(vektor2):
            raise ValueError("Vektorler ayni uzunlukta olmalidir!")
        mesafe = sum(abs(x-y) for x,y in zip(vektor1,vektor2))
        return mesafe
    
    
    
    
    #MİNKOWSKİ MESAFESİ : D(p, q) = (|q1 - p1|^p + |q2 - p2|^p + ... + |qn - pn|^p)^(1/p)
    def MinkowskiMesafesi(vektor1,vektor2,p):
        if len(vektor1) != len(vektor2):
            raise ValueError("Vektorler ayni uzunlukta olmalidir!")
        mesafe = pow(sum(pow(abs(x-y),p)for x,y in zip(vektor1,vektor2)),(1/p))
        return mesafe 
    
    
    
    #COSİNUS BENZERLİĞİ MESAFESİ :Cosine Similarity(A,B)=  (A⋅B) / ∥A∥∥B∥
    def CosinusMesafesi(vektor1,vektor2):
        if len(vektor1) != len(vektor2):
            raise ValueError("Vektorler ayni uzunlukta olmalidir!")
        
        vektor1Norm=np.sqrt(sum(pow(vektor1,2)))
        vektor2Norm=np.sqrt(sum(pow(vektor2,2)))
        icCarpim=  sum(x * y for x, y in zip(vektor1, vektor2))
        mesafe = icCarpim / (vektor1Norm*vektor2Norm)
        return mesafe
    
    
   # Örnek kullanım ve testler
vektor1 = np.array([1, 2, 3])
vektor2 = np.array([4, 5, 6])

# Öklidyen Mesafe Test
oklit_mesafe = DistanceMeasurementMethods.oklitMesafesi(vektor1, vektor2)
print("Öklidyen Mesafe:", oklit_mesafe)

# Manhattan Mesafe Test
manhattan_mesafe = DistanceMeasurementMethods.ManhattanMesafesi(vektor1, vektor2)
print("Manhattan Mesafe:", manhattan_mesafe)

# Minkowski Mesafe Test
p = 2  # Öklidyen mesafe için p=2
minkowski_mesafe = DistanceMeasurementMethods.MinkowskiMesafesi(vektor1, vektor2, p)
print("Minkowski Mesafe:", minkowski_mesafe)

# Cosinus Benzerliği Test
cosinus_mesafe = DistanceMeasurementMethods.CosinusMesafesi(vektor1, vektor2)
print("Cosinus Benzerliği:", cosinus_mesafe)
    
    
    
    
    
    
    
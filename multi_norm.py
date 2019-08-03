#!/usr/bin/env python
# coding: utf-8

# In[51]:


#To Check Multivariate Normality
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import det
import matplotlib.pyplot as plt
from scipy.stats import chi2 
from scipy.interpolate import interp1d


def check_qq(X,q=0.5,plot=False):
    n,p=X.shape
    M=[]
    for i in range(X.shape[0]):
        M.append(list(X.mean(axis=0)))  
    Sigma=X.cov()
    SigmaInv=inv(Sigma)
    diff=(X.values)-M
    GD=[]
    for i in range(len(diff)):
        GD.append(diff[i].dot(SigmaInv).dot(diff[i]))

    chi=chi2.isf(1-q, df=p)
    print('ChiSquare table value is',chi,'\n')

    sum=0
    for i in range(n) :
        if GD[i] <= chi :
            sum=sum+1

    print('Number of Observation below QQ line',sum,'\n')
    print('Percentage of Obs below QQ line :',(sum/n)*100)

    #Plotting
    if(plot==True):
        obs=len(X)
        plt.scatter(range(obs),GD)
        plt.axhline(y=chi, color='r', linestyle='--')
        plt.show()
        
        
        
        
        
        
def check_norm(X):
    n,p=X.shape
    M=[]
    for i in range(X.shape[0]):
        M.append(list(X.mean(axis=0)))  
    Sigma=X.cov()
    SigmaInv=inv(Sigma)
    diff=(X.values)-M
    GD=[]
    for i in range(len(diff)):
        GD.append(diff[i].dot(SigmaInv).dot(diff[i]))
    
    pt=[]
    qq=[]
    for q in np.linspace(0,1,11):
        chi=chi2.isf(1-q, df=p)
        sum=0
        for i in range(n) :
            if GD[i] <= chi :
                sum=sum+1
        pt.append(np.around(q*100))   
        qq.append(np.around((sum/n)*100,decimals=2))
        print('#Percentile:',np.around(q*100),'\t#Percentage of Observations below qq line :',np.around((sum/n)*100,decimals=2))

    
    plt.scatter(pt,qq)
    plt.plot([-10,110],[-10,110],linewidth=1,color='r')
    plt.title('QQ Plot')
    plt.show()


# In[ ]:





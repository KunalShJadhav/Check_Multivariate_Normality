# Check Multivariate Normality of data

## Methodology :
This method is inspired from book **Applied Multivariate Analysis by Richard Johnson and Wichern ( 6 Edition)**.
  In this Method, we convert Multivariate Normal into Chi-Square and then compare Percentile of Chi-square with
  Percentile obtain from calculation
  
## Usage:

```python
from multi_norm import check_qq,check_norm
```
###### To find Number of Observations below certain Percentile:

```python
check_qq(X,q=0.5,plot=False)
```

**X :** Matrix of Observations

**q :** Specified Percentile

**plot :** Whether to plot Graph or not

**Interpretation :** When we specify q=0.5. Method check how many Observations are below Median (50th Percentile) , Since Normal is symmetric Distribution
,Ideally, we should get value near 50%


###### To find Number of Observations below each Percentile (Check Nature of Data):

```python
check_norm(X)
```

**X :** Matrix of Observations

**Interpretation :** In Result, Number of Observations below Percentile should be close to value of Percentile, departure from value 
indicates departure from Normality.Also, In Graph of QQ Plot, All Points should lie on Straight line. Distance between Line and Points 
indicates departure from Normality

## Requirement:
```python
numpy
matplotlib
scipy
```

## Known Issues:
Variance of Matrix X must be non-Singular. In other words, All Variables must be independent.


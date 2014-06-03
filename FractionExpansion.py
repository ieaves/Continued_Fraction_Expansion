from math import *
from decimal import *
from matplotlib import *
from matplotlib.pyplot import *

def FracTerms(frac,num,prec):
	terms=[int(frac)]
	for i in range(num):
		if (frac-int(frac)) > 0+10**(-(prec-1)):
			frac=Decimal(1)/Decimal(frac-int(frac))
			terms.append(int(frac))
		else: break
	return terms

def FractionExp(terms):
	val=Decimal(terms[0])
	frac=Decimal(0)
	for i in range(len(terms)-1):
		if i==0: frac=Decimal(1)/Decimal(terms[len(terms)-1])
		else: frac=Decimal(1)/Decimal(terms[len(terms)-i-1]+frac)
	return val+frac

def PlotName(titlename,x,y):
	title(titlename)
	xlabel(x)
	ylabel(y)

def LogScale(x):
	y=[]
	for i in range(len(x)): y.append(log(float(x[i])))
	return y

def Difference(fract,terms,prec):
	dif=[]
	for i in range(terms): dif.append(abs(fract-FractionExp(FracTerms(fract,i,precision))))
	return dif
	
terms=10
precision=100000
#getcontext.prec=precision

pifract=Decimal(pi)
pidif=Difference(pifract,terms,precision)
logpidif=LogScale(pidif)

goldfract=(Decimal(1)+Decimal(5)**(Decimal(.5)))/Decimal(2)
golddif=Difference(goldfract,terms,precision)
loggolddif=LogScale(golddif)
#print FracTerms(goldfract,terms,precision)

efract=(Decimal(exp(1)))
edif=Difference(efract,terms,precision)
logedif=LogScale(edif)

r2fract=Decimal(2)**(Decimal(.5))
r2dif=Difference(r2fract,terms,precision)
logr2dif=LogScale(r2dif)
#print FracTerms(r2fract,terms,precision)

r3fract=Decimal(3)**(Decimal(.5))
r3dif=Difference(r3fract,terms,precision)
logr3dif=LogScale(r3dif)
#print FracTerms(r3fract,terms,precision)
for i in range(9):
	print FracTerms(Decimal(i+2)**(Decimal(.5)),terms,precision)
	
PlotName('ln(differences) vs. # Terms in Expansion', '# terms in Partial Fraction expansion', "ln|x-x'|")
x=range(1,len(pidif)+1,1)
plot(x,loggolddif,'o-',label='Golden Ratio: '+str((loggolddif[9]-loggolddif[4])/5))
plot(x,logpidif,'o-',label='Pi')
plot(x,logedif,'o-',label='e')
plot(x,logr2dif,'o-',label='root(2): '+str(logr2dif[8]-logr2dif[7]))
plot(x,logr3dif,'o-',label='root(3): '+str(logr3dif[8]-logr3dif[7]))
#legend(loc='0')

show()
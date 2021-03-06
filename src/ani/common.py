from imports import *

ac = FLT_PI/180.0
fa = 0.0
da = 10.0
na = 5
sa = Sampling(fa,da,na)

def main(args):
	goParams1()
	#goParams2()
	vpe = goExact()
	vpw = goWeak()
	plot(vpe,vpw)

def goExact(fi=None):
	if fi: fe = fi
	else: fe = f
	vp = zerofloat(na)
	for ia in range(na):
		t = ac*(ia*da+fa)
		sin2 = sin(t)*sin(t)
		si2n = sin(2.0*t)*sin(2.0*t)
		vp[ia] = sqrt(1.0+eps*sin2-fe/2.0+(fe/2.0)*\
			sqrt(pow(1.0+2.0*eps*sin2/2,2.0)-2.0*(eps-dlt)*si2n/fe))
	return vp
		
def goWeak(fi=None):
	if fi: fe = fi
	else: fe = f
	vp = zerofloat(na)
	for ia in range(na):
		t = ac*(ia*da+fa)
		sin2 = sin(t)*sin(t)
		sin4 = sin2*sin2
		cos2 = cos(t)*cos(t)
		vp[ia] = sqrt(1.0+2.0*dlt*sin2*cos2+2.0*eps*sin4+(4.0/fe)*(eps-dlt)*\
							sin4*cos2*(eps*sin2+dlt*cos2))
	return vp


def goParams1()
	global vpvs,eps,dlt,f,da,na
	global fa,da
	global na
	vpvs = 2.0
	f = 1.0-(1.0/(vpvs*vpvs))
	eps  = 0.6
	dlt = 0.1
	#dlt = 0.3
	#dlt = 0.5

def goParams2()
	global vpvs,eps,dlt,f,da,na
	global fa,da
	global na
	#vpvs = 2.0
	#f = 1.0-(1.0/(vpvs*vpvs))
	#TI model 1:
	eps  = 0.6
	dlt = 0.1
	#TI model 2:
	dlt = 0.5


def plot(x1,x2=None,title=None,png=None):
	pp = PlotPanel()
	l1 = pp.addPoints(sa,x1)
	if x2:
		l2 = pp.addPoints(sa,x2)
		l2.setLineColor(RED)
	if title:
		pp.setTitle(title)
	pp.setVLabel("velocity")
	pp.setHLabel("angle (degrees)")
	

	

#############################################################################
class RunMain(Runnable):
  def run(self):
    main(sys.argv)
if __name__=="__main__":
  SwingUtilities.invokeLater(RunMain()) 

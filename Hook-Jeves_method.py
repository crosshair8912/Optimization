from copy import deepcopy
eps = 0.001
bpt = {'x0':0,'y0':0}
iv = {'x':0.5,'y':0.5}
k = {'x': 0,'y':0}
cval = []
cnt = 0
pts = []
#def f(x1,x2):
#	return ((x1**2+x2-11)**2 + (x1+x2**2-7)**2)
def f(x1,x2):
	return (x1-2)**2+(x2-4)**2
def pattern_move():
	global cnt
	if  cnt == 0:
		bpt['x0'] = 2*iv['x'] - k['x']
		bpt['y0'] = 2*iv['y'] - k['y']
		
	else:
		bpt['x0'] = 2*bpt['x0'] - pts[cnt-1]['x0']
		bpt['y0'] = 2*bpt['y0'] - pts[cnt-1]['y0']
	pts.append(bpt)
	cnt +=1
	return iv
def exploratore_move():
	func = [f(bpt['x0'],bpt['y0']),
	f(bpt['x0']+iv['x'],bpt['y0']),
	f(bpt['x0']-iv['x'],bpt['y0'])]
	
	#checking for the end of discovery
	if min(func) != 0.0:
		cval.append(min(func))
	else:
		return False
		
	#changing basic point per X based on our discovery
	min_index_x = min(xrange(len(func)),key = func.__getitem__)
	if min_index_x == 1:
		bpt['x0'] = bpt['x0']+iv['x']
	elif min_index_x == 2:
		bpt['x0'] = bpt['x0']-iv['x']
		
	func1 = [f(bpt['x0'],bpt['y0']),
			f(bpt['x0'],bpt['y0']+iv['y']),
			f(bpt['x0'],bpt['y0']-iv['y'])]
			
	#checking for the end of discovery
	if min(func1) != 0.0:
		cval.append(min(func1))
	else:
		return False
		
	#changing basic point per Y based on our discovery
	min_index_y = min(xrange(len(func1)),key = func1.__getitem__)
	if min_index_y == 1:
		bpt['y0'] = bpt['y0']+iv['y']
	elif min_index_y == 2:
		bpt['y0'] = bpt['y0']-iv['y']
	print(cval)
while iv['x']>= eps:
	j = exploratore_move()
	if j != False:
		pattern_move()
		b = deepcopy(pts)
		pts = b
		
		print(pts[-1])
	else:
		iv['x'] /= 2
		iv['y'] /= 2
		print(iv)
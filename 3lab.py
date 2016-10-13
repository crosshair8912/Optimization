a = '(x1-2)**2+(x2-4)**1-(x2-4)**2'
tmp = [0 for i in range(0,len(a))]
cnt = 0
for index,i in enumerate(a):
	if i == '(':
		tmp[index] = 1
	elif i ==')':
		tmp[index] = -1
		if tmp[index] == 1:
			cnt+=1
	#if cnt == 2:

def cut(element):
	cnt = 0
	shift = 0
	bl_1 = []
	bl_2 = []
	a_tmp = []
	buf_1 = []
	buf_2 = []
	cnt_1 = 0
	cnt_2 = 0
	for index,i in enumerate(tmp[:]):
		if i == element:
			cnt_1+=1
			buf_1.append(cnt_1)
			if cnt == 0:
				bl_1 = a[index:]
				cnt +=1
				shift = index
			elif cnt == 1:
				bl_2 = bl_1[:index-shift+1]
				cnt +=1
		elif i == -element:
			cnt_2+= 1
			buf_2.append(cnt_2)
		elif cnt == 2:
			a_tmp.append(list(bl_2))
			cnt = 0
			shift = 0
			bl_2 = []
			continue
	print(buf_1,buf_2)
	return a_tmp

for i in cut(1):
	print (i)
print(tmp)
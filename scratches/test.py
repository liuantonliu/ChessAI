def selection_sort(u):
	for i in range(len(u)):
		min_idx = i
		for j in range(i + 1, len(u)):
			if u[min_idx] > u[j]:
				min_idx = j
		u[i], u[min_idx] = u[min_idx], u[i]
	return True

def heapify(u):
	if u==[] or len(u)==1:
		return False
	else:
		reheapify(u,len(u))
		return True

def reheapify(u,end):
	if u==[] or len(u)==1:
		return False
	else:
		for i in range(1,end,1):
			n = i
			switch = True
			while switch:
				p = int((n-1)/2)
				if u[n]>u[p]:
					t = u[n]
					u[n] = u[p]
					u[p] = t
					n = p
				else:
					switch = False
	return True

def heap_sort(u):
	n = 1
	heapify(u)
	while n<len(u):
		t = u[0]
		u[0] = u[len(u)-n]
		u[len(u)-n] = t
		reheapify(u,len(u)-n)
		n+=1
	return True

def merge_sort(u):
	if len(u) > 1:
		mid = len(u) // 2
		L = u[:mid]
		R = u[mid:]
		merge_sort(L)
		merge_sort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				u[k] = L[i]
				i += 1
			else:
				u[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			u[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			u[k] = R[j]
			j += 1
			k += 1
	return True

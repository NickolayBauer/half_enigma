def P(my_date, keys):
	 p_date = []
	 	
	 for i in range(len(my_date)):
	 	p_date.append(my_date[keys[i]])
	 print(p_date)

	 return p_date


def S(my_date):
	matrix = [["a","d"  ,  "c","b"  ]
			, ["d","a"  ,"  b","c"  ]]
	new = []
	my_date = ''.join(my_date)
	for part in my_date:

			if part in matrix[1]:
				print(part, ' заменен на : ',matrix[1][matrix[0].index(part)])
				part = matrix[1][matrix[0].index(part)]
			new.append(part)
	print('S: ',new)
	return new



a = P([elem for elem in input().split()],[0,1,2,3])
a = P(a,  [0,1,3,2])
a = P(a,  [0,3,2,1])

a = S(a) 

a = P(a, [0,3,2,1])
a = P(a, [0,1,3,2])
a = P(a, [0,1,2,3])


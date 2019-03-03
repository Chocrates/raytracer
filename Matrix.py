import re
import math
from Tuple import *

class Matrix:
	def __init__(self, data=None):
		self.data = data

	def __eq__(self,other):
		if isinstance(other,Matrix):
			ret = False
			if len(self.data) == len(other.data):
				for i in range(len(self.data)):
					if len(self.data[i]) == len(other.data[i]):
						for j in range(len(self.data[i])):
							if not math.isclose(self.data[i][j],other.data[i][j],rel_tol=1e-10):
								return False
					else:
						ret = True 

			return ret
		else:
			raise NotImplementedError(f'Matrix equality is not implemented for types {type(other)}')

	def __mul__(self,other):
		if isinstance(other,Matrix):
			result = [[0 for _ in range(len(other.data[0]))] for __ in range(len(self.data))]
			for i in range(len(self.data)):
				for j in range(len(other.data[0])):
					tmp = 0
					for k in range(len(self.data)):
						tmp += self.data[i][k] * other.data[k][j]
					result[i][j] = tmp
			m = Matrix()
			m.data = result
			return m
		elif isinstance(other,Tuple):
			tuple_mat = Matrix([[other.x],[other.y],[other.z],[other.w]])
			result_mat = self * tuple_mat
			return Tuple(result_mat.data[0][0],result_mat.data[1][0],result_mat.data[2][0],result_mat.data[3][0])
		else:
			raise NotImplementedError(f'Matrix equality is not implemented for types {type(other)}')

	@classmethod
	def build_matrix(cls,text):
		matrix = []
		for row in re.sub('\s\s\s\s\s+','\n',text).strip().split('\n'):
			row_list = []
			matrix.append(row_list)
			for col in row.strip('|').split('|'):
				row_list.append(float(col.strip()))
		return Matrix(matrix)
	
	@classmethod
	def identity(cls, matrix=None):
		print('class level identity')
		return Matrix([[1,0,0,0], \
			[0,1,0,0], \
			[0,0,1,0], \
			[0,0,0,1]])

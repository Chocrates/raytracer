import re
import math
import copy
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
							if not math.isclose(round(self.data[i][j],4),round(other.data[i][j],4),rel_tol=1e-4):
								return False
					else:
						return False		
				ret = True 

			return ret
		else:
			raise NotImplementedError(f'Matrix equality is not implemented for types {type(other)}') 
	def __mul__(self,other):
		if isinstance(other,Matrix):
			result = [[0 for _ in range(len(other.data[0]))] for _ in range(len(self.data))]
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

	def transpose(self):
		transposed = [ [ 0 for _ in range(len(self.data[0])) ] for _ in range(len(self.data))]
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				transposed[j][i] = self.data[i][j]
		return Matrix(transposed)

	def determinant(self):
		if len(self.data) > 2:
			det = 0
			for i in range(len(self.data[0])): 
				det += self.data[0][i] * self.cofactor(0,i)
			return det
		else:
			return self.data[0][0] * self.data[1][1] - \
				self.data[0][1] * self.data[1][0]
	
	def submatrix(self, row, col):
		sub = copy.deepcopy(self.data)
		for r in sub:
			del r[col]
		del sub[row]
		return Matrix(sub)

	def minor(self,row,col):
		return self.submatrix(row,col).determinant()
	
	def cofactor(self,row,col):
		m = self.minor(row,col)
		if (row+col)%2 != 0:
			m *= -1

		return m
	
	@property
	def invertible(self):
		return self.determinant() != 0
	
	def inverse(self):
		if not self.invertible:
			raise TypeError('Matrix is not invertible')
		else:
			m2 = [[0 for x in range(len(self.data))] for y in range(len(self.data))]
			for row in range(len(self.data)):
				for col in range(len(self.data[0])):
					if col == 2 and row == 2:
						#import pdb; pdb.set_trace()
						pass
					cof = self.cofactor(row,col)
					m2[col][row] = cof/self.determinant()
			return Matrix(m2)

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

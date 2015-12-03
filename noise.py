import numpy as np
import unittest

def lerp(v0, v1, t):
	return (1.0 - t) * v0 +	(t * v1)
	
def clamp(x, min, max):
	if x < min: return min
	if x > max: return max
	return x
	
def ss3(t):
	return (3 * t**2) - (2 * t**3)
	
def ss5(t):
	return (6 * t**5) - (15 * t**4) + (10 * t**3)
	
class Vector:
	def __init__(self, *components):
		self.components = np.array(components)
	
	def mag(self):
		return np.sqrt(sum(self.components**2))
	
	def __len__(self):
		return len(self.components)
	
	def __iter__(self):
		for x in self.components:
			yield x
	
class Field:
	def __init__(self, d = (32,32), seed = 0):
		np.random.seed(seed)
		self._r = np.random.ranf(d)

	def __call__(self, *pos):
		return self._r[pos]
		
if __name__ == '__main__':
	unittest.main()
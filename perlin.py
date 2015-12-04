# http://scratchapixel.com/old/lessons/3d-advanced-lessons/noise-part-1/
import numpy as np

MAX_VERTICES = 256
MAX_VERTICES_MASK = MAX_VERTICES - 1

r = np.random.ranf(MAX_VERTICES)
perm = [i & MAX_VERTICES_MASK for i in range(MAX_VERTICES * 2)]
np.random.shuffle(perm)

def lerp(v0, v1, t):
	return (1.0 - t) * v0 + (t * v1)

def floor(x):
	return int(x) - (x < 0 and int(x) != x)

def smoothstep(t):
	return t * t * (3 - 2 * t)

def noise2d(x, y):
	xi, yi = floor(x), floor(y)
	tx, ty = x - xi, y - yi
	
	rx0 = xi & MAX_VERTICES_MASK
	rx1 = (rx0 + 1) & MAX_VERTICES_MASK
	ry0 = yi & MAX_VERTICES_MASK
	ry1 = (ry0 + 1) & MAX_VERTICES_MASK 
	
	c00 = r[perm[perm[rx0] + ry0]]
	c10 = r[perm[perm[rx1] + ry0]]
	c01 = r[perm[perm[rx0] + ry1]]
	c11 = r[perm[perm[rx1] + ry1]]
	
	sx = smoothstep(tx)
	sy = smoothstep(ty)
	
	nx0 = lerp(c00, c10, sx)
	nx1 = lerp(c01, c11, sx)
	
	return lerp(nx0, nx1, sy)
	
def fbm(x, y, lacunarity = 2, gain = 0.5, octaves = 5):
	n = 0
	amp = 1
	for i in range(octaves):
		n += noise2d(x, y) * amp
		x *= lacunarity
		y *= lacunarity
		amp *= gain
	return n
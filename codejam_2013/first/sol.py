#!/usr/bin/env python

import io
from decimal import *

f = open("input.txt")

cases = int(f.readline())

for n_c in range(cases):
	[r, t] = [int(num) for num in f.readline().split(" ")]
	a = (2)
	b = (-1 + 2 * r)
	c = (-t)
	res = (-b + ( b ** 2 + 8 * t) ** 0.5)
	print (res / 4)
	n_r = int(res / 4)
	if n_r < 0:
		print "r: %f  t: %f" % (r, t)
		exit	

	print "Case #%d: %d" % ((n_c + 1), n_r)

#!/usr/bin/env python

import io
from decimal import *

f = open("input.txt")

cases = int(f.readline())

for n_c in range(cases):
	[r, t] = [int(num) for num in f.readline().split(" ")]
	a = Decimal(2)
	b = Decimal(-1 + 2 * r)
	c = Decimal(-t)
	res = Decimal((-b + ( b ** Decimal(2) - Decimal(4) * a * c) ** Decimal(0.5))) / Decimal(2 * a)
	n_r = int(res)
	if n_r < 0:
		print "r: %f  t: %f" % (r, t)
		exit	

	print "Case #%d: %d" % ((n_c + 1), n_r)

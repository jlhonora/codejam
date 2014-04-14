#!/usr/bin/env python

import io

def get_fair_score(bn, bk):
	blocks_n = list(bn)
	blocks_k = list(bk)
	score = 0
	for i in range(len(blocks_k)):
		if blocks_k[i] > blocks_n[0]:
			del blocks_n[0]

	return len(blocks_n)

def get_cheat_score(bn, bk):
	blocks_n = list(bn)
	blocks_k = list(bk)
	blocks_n.reverse()
	blocks_k.reverse()

	score = 0
	for i in range(len(blocks_n)):
		for j in range(len(blocks_k)):
			if blocks_n[i] > blocks_k[j]:
				del blocks_k[j]
				score = score + 1
				break

	return score

f = open("input.txt")

cases = int(f.readline())

for case_n in range(cases):
	score_cheat = 0
	score_fair = 0

	n = int(f.readline())

	bsn = [float(num) for num in f.readline().split(" ")]
	bsk = [float(num) for num in f.readline().split(" ")]
	bsn.sort()
	bsk.sort()

	score_fair = get_fair_score(bsn, bsk)	
	score_cheat = get_cheat_score(bsn, bsk)	
	
	print "Case #%d: %d %d" % ((case_n + 1), score_cheat, score_fair)

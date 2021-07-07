#!/usr/bin/env python3

import sys

logfile = sys.argv[1]
with open(lofile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		print(result[1])
		
		return '{} pid:{}'.format(result[1],result[2])
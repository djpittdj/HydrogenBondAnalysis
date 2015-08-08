#!/usr/bin/python
from __future__ import print_function
import re
from collections import defaultdict, Counter

for cutoff in [3.0, 3.5, 4.0]:
  infilename = str("hbonds_res-D1ligD2_cut%s.xvg" % cutoff)
  
  dd = defaultdict(int)
  lines = open(infilename).readlines()
  for line in lines:
    timestep = int(line.split()[0])
    num_hbs = int(line.split()[1])
    print(timestep)

    if num_hbs != 0:
      matched_all = re.findall(r'(\{(\d*) (\d*)\})', line, re.M|re.I)
      hbs = []
      for i in xrange(0, len(matched_all)):
        donor_indx = int(matched_all[i][1])
        acceptor_indx = int(matched_all[i][2])
        hb = (donor_indx, acceptor_indx)
        hbs.append(hb)

      for hb in set(hbs):
        dd[hb] += 1

  counter = Counter(dd).most_common()
  total_num_frames = len(lines)
  print("total_num_frames", total_num_frames)
  outfile = open("hb_counts_res_D1ligD2_cut%s.xvg" % cutoff, 'w')
  for one_hb in counter:
    hb = one_hb[0]
    num_hb = int(one_hb[1])
    outfile.write("%-25s\t%8i%8.3f\n" % (str(hb[0])+str(" ")+str(hb[1]), num_hb, float(num_hb)/total_num_frames))
  
  outfile.close()

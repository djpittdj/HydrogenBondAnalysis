cutoff = 3.0
infilename = str("hbonds_res-D1D2_cut%s.xvg" % cutoff)

raw = []
hb_uniq_lst = set()
lines = open(infilename).readlines()
total_num_frames = 0
for line in lines:
  timestep = int(line.split()[0])
  num_hbs = int(line.split()[1])
  print timestep
  total_num_frames += 1
  
  hb_one_frame = []
  if num_hbs == 0:
    continue
  if num_hbs != 0:
    matched_all = re.findall(r'(\{(\d*) (\d*)\})', line, re.M|re.I)
    for i in xrange(0, len(matched_all)):
      donor_resid = int(matched_all[i][1])
      acceptor_resid = int(matched_all[i][2])
      hb = (donor_resid, acceptor_resid)
      hb_one_frame.append(hb)
      hb_uniq_lst.add(hb)
  one_frame = [timestep, num_hbs, hb_one_frame]
  raw.append(one_frame)

dic = {}
for hb_uniq in hb_uniq_lst:
  dic[hb_uniq] = 0

for one_frame in raw:
  hb_one_frame = one_frame[2]
  for hb_uniq in hb_uniq_lst:
    if hb_uniq in hb_one_frame:
      dic[hb_uniq] += 1

lst_dic_sort = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)
print "total_num_frames", total_num_frames
outfile = open("hb_counts_res_D1D2_cut%s.xvg" % cutoff, 'w')
for one_hb in lst_dic_sort:
  hb = one_hb[0]
  num_hb = int(one_hb[1])
  print>>outfile, "%-25s\t%8i%8.3f" % (str(hb[0])+str(" ")+str(hb[1]), num_hb, float(num_hb)/total_num_frames)
outfile.close()

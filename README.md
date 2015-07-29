# HydrogenBondAnalysis
[![hbond_network](https://cloud.githubusercontent.com/assets/7023606/8961587/1ead392c-35e4-11e5-83d6-4a1340b83512.png)](#features)

Tools needed: VMD (molecular visualization and analysis package), Python (with matplotlib)
Background info: what is a hydrogen bond? It's the case where the electron cloud of a hydrogen is shared between two negatively charged atoms, typically oxygen (O) and nitrogen (N). For example, OH--O, or NH--O. The first O or N is called the hydrogen bond donor and the second O is called the hydrogen bond acceptor. A hydrogen bond can only be treated accurately with quantum mechanics, but here we use some geometrical rules to determine if a hydrogen bond has formed or not. One might expect that a hydrogen bond forms only when the donor and acceptor are within a certain distance, e.g., 3 Angstroms. Also, the angle donor-hydrogen-acceptor should not deviate too much from 180 degrees (i.e., a straight line through donor, hydrogen and acceptor). Here we allow a 20 degrees of deviation. These rules are the default geomtric limits defined in VMD for a hydrogen bond.
Aims: Analyze hydrogen bonding network in a molecular dynamics simulation trajectory, taking a simulation from a water solulble protein as an example. Find the percentage of occurance of specific hydrogen bonds, i.e., to answer the question: how many frames does a particular hydrogen bond appears over the entire simulation?
Subject: This protein has a bilobed structure and the ligand binds to the cleft between the two lobes (lobe 1 & lobe 2). The analysis is to identify ALL the possible hydrogen bonding partners between lobe 1 and lobe 2. However, the hydrogen bonds that are mediated by water or ions are not considered.

The analysis consists of three steps:
* Use VMD to extract all the hydrogen bonds between lobe 1 and lobe for each frame of the simulation trajectory. This step uses the TCL script "calc_hbonds_D1D2.tcl". Example output:
1 2 {184 127} {183 93}

2 0 

3 0 

4 1 {90 175}

5 0 

6 0 

7 0 

8 1 {183 93}

9 5 {90 175} {183 93} {183 93} {220 10} {231 11}

10 2 {90 175} {184 127}

The columns represent: simulation frame number, total number of hydrogen bonds; donor-acceptor pairs of hydrogen bonds in a frame.

* Use Python to process the data and find the percentage of occurance of hydrogen bonds that appeared in the trajectory. This step uses the Python script "hb_counts_res_D1D2.py". Example output:
183 93                   	     536   0.594

231 11                   	     237   0.262

88 201                   	     214   0.237

90 175                   	     178   0.197

128 177                  	     155   0.172

184 127                  	     151   0.167

177 123                  	      92   0.102

220 10                   	      70   0.078

125 177                  	      55   0.061

91 179                   	      26   0.029

The columns represent: donor residue ID, acceptor residue ID, number of frames in which this hydrogen bond appear, the percentage of occurance of this hyodrgen bond (i.e., the 3rd column divided by the total number of frames)

* Assign residue name to the result with "assign_name_hb_res_D1D2.tcl"
ARG 183      : GLU 93       :      536   0.594

GLN 231      : GLU 11       :      237   0.262

LYS 88       : GLU 201      :      214   0.237

GLY 90       : CYX 175      :      178   0.197

ARG 128      : SER 177      :      155   0.172

ARG 184      : GLU 127      :      151   0.167

SER 177      : THR 123      :       92   0.102

TRP 220      : GLN 10       :       70   0.078

ASN 125      : SER 177      :       55   0.061

THR 91       : ASP 179      :       26   0.029

The columns represent: donor residue name and ID, acceptor residue name and ID. The rest of the columns are the same as in the output file of the previous step.

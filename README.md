# HydrogenBondAnalysis
https://cloud.githubusercontent.com/assets/7023606/8961587/1ead392c-35e4-11e5-83d6-4a1340b83512.png
Tools needed: VMD (molecular visualization and analysis package), Python (with matplotlib)
Background info: what is a hydrogen bond? It's the case where the electron cloud of a hydrogen is shared between two negatively charged atoms, typically oxygen (O) and nitrogen (N). For example, OH--O, or NH--O. The first O or N is called the hydrogen bond donor and the second O is called the hydrogen bond acceptor. A hydrogen bond can only be treated accurately with quantum mechanics, but here we use some geometrical rules to determine if a hydrogen bond has formed or not. One might expect that a hydrogen bond forms only when the donor and acceptor are within a certain distance, e.g., 3 Angstroms. Also, the angle donor-hydrogen-acceptor should not deviate too much from 180 degrees (i.e., a straight line through donor, hydrogen and acceptor). Here we allow a 20 degrees of deviation. These rules are the default geomtric limits defined in VMD for a hydrogen bond.
Aims: Analyze hydrogen bonding network in a molecular dynamics simulation trajectory, taking a simulation from a water solulble protein as an example. Find the percentage of occurance of specific hydrogen bonds, i.e., to answer the question: how many frames does a particular hydrogen bond appears over the entire simulation?
Subject: This protein has a bilobed structure and the ligand binds to the cleft between the two lobes (lobe 1 & lobe 2). The analysis is to identify ALL the possible hydrogen bonding partners between lobe 1 and lobe 2. However, the hydrogen bonds that are mediated by water or ions are not considered.

The analysis consists of three steps:
1. Use VMD to extract all the hydrogen bonds between lobe 1 and lobe for each frame of the simulation trajectory. This step uses the TCL script "calc_total_num_hbonds_D1D2.tcl";
2. Use Python to process the data and find the percentage of occurance of hydrogen bonds that appeared in the trajectory. This step uses the Python script "hb_counts_res_D1D2.py";
3. Assign residue name to the result with "assign_name_hb_res_D1D2.tcl".

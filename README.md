# HydrogenBondAnalysis
Tools needed: VMD (molecular visualization and analysis package), Python (with matplotlib)
Background info: what is a hydrogen bond? It's the case where the electron cloud of a hydrogen is shared between two negatively charged atoms, typically oxygen (O) and nitrogen (N). For example, OH--O, or NH--O. The first O or N is called the hydrogen bond donor and the second O is called the hydrogen bond acceptor.
Aims: Analyze hydrogen bonding network in a molecular dynamics simulation trajectory, taking a simulation from a water solulble protein as an example. Find the percentage of occurance of specific hydrogen bonds, i.e., to answer the question: how many frames does a particular hydrogen bond appears over the entire simulation?
Subject: This protein has a bilobed structure and the ligand binds to the cleft between the two lobes (lobe 1 & lobe 2). The analysis is to identify ALL the possible hydrogen bonding partners between lobe 1 and lobe 2. However, the hydrogen bonds that are mediated by water or ions are not considered.

The analysis mainly consists of two steps:
1. Use VMD to extract all the hydrogen bonds between lobe 1 and lobe for each frame of the simulation trajectory;
2. Use Python to process the data and find the percentage of occurance of hydrogen bonds that appeared in the trajectory;


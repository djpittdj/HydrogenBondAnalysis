package require bigdcd

proc calc_hbonds {frame} {
  global outfile1 outfile2 cutoff_dist cutoff_angle
  global D1seltxt D2seltxt

  set sel_D1 [atomselect top $D1seltxt]
  set sel_D2 [atomselect top $D2seltxt]
  set hbonds_vmd1 [measure hbonds $cutoff_dist $cutoff_angle $sel_D1 $sel_D2]
  set hbonds_vmd2 [measure hbonds $cutoff_dist $cutoff_angle $sel_D2 $sel_D1]
  set indices_donors1 [lindex $hbonds_vmd1 0]
  set indices_acceptors1 [lindex $hbonds_vmd1 1]
  set num_hbonds1 [llength $indices_donors1]
  set indices_donors2 [lindex $hbonds_vmd2 0]
  set indices_acceptors2 [lindex $hbonds_vmd2 1]
  set num_hbonds2 [llength $indices_donors2]
  set total_num_hbonds [expr {$num_hbonds1+$num_hbonds2}]
  puts $outfile1 "$frame $total_num_hbonds"

  set hb_resids []

  foreach indx_donor $indices_donors1 indx_acceptor $indices_acceptors1 {
    set donor [atomselect top "index $indx_donor"]
    set resid_donor [lsort -unique [$donor get resid]]
    set acceptor [atomselect top "index $indx_acceptor"]
    set resid_acceptor [lsort -unique [$acceptor get resid]]
    set hb_resid [list $resid_donor $resid_acceptor]
    lappend hb_resids $hb_resid
  }

  foreach indx_donor $indices_donors2 indx_acceptor $indices_acceptors2 {
    set donor [atomselect top "index $indx_donor"]
    set resid_donor [lsort -unique [$donor get resid]]
    set acceptor [atomselect top "index $indx_acceptor"]
    set resid_acceptor [lsort -unique [$acceptor get resid]]
    set hb_resid [list $resid_donor $resid_acceptor]
    lappend hb_resids $hb_resid
  }

  puts $outfile2 "$frame $total_num_hbonds $hb_resids"
}

set D1seltxt "resid 1 to 138 247 to 281"
set D2seltxt "resid 143 to 243"

set cutoff_dist 3.0
set cutoff_angle 20

set outfile1 [open total_num_hbonds-D1D2_cut${cutoff_dist}.xvg w]
set outfile2 [open hbonds_res-D1D2_cut${cutoff_dist}.xvg w]
mol load psf ../../../../01prep/prot.psf
bigdcd calc_hbonds ../files/frames_prot.dcd
bigdcd_wait
close $outfile1
close $outfile2

exit

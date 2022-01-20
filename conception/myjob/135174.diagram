format 224

pseudostatecanvas 128006 pseudostate_ref 134534 // initial 
   xyz 111 20 2000
end
statecanvas 128262 state_ref 134790 // postuler
  
  xyzwh 366 45 2000 113 47
end
statecanvas 128390 state_ref 134918 // refuser
  
  xyzwh 332 236 2000 171 43
end
statecanvas 128518 state_ref 135046 // en attente
  
  xyzwh 57 203 2000 137 59
end
pseudostatecanvas 131334 pseudostate_ref 135302 // final fin
   xyz 636 299 2000
end
statecanvas 132102 state_ref 141574 // fermer
  
  xyzwh 684 185 2000 115 53
end
transitioncanvas 130182 transition_ref 135046 // <transition>
  decenter_begin 934
  decenter_end 578
  
  from ref 128518 z 2001 to ref 128390
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 130310 transition_ref 135174 // creation d'un job
  
  from ref 128006 z 2001 label "creation d'un job" xyz 134 71 2001 to ref 128518
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 130438 transition_ref 135302 // <transition>
  
  from ref 128518 z 2001 to ref 128262
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 131590 transition_ref 142214 // <transition>
  decenter_begin 52
  
  from ref 128390 z 2001 to ref 128518
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 132230 transition_ref 142342 // [when : date_fin>today]
  decenter_begin 920
  
  from ref 128262 z 2001 label "[when : date_fin>today]" xyz 503 129 2001 to ref 132102
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 132358 transition_ref 142470 // <transition>
  decenter_begin 790
  decenter_end 276
  
  from ref 132102 z 2001 to ref 128262
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 132486 transition_ref 142598 // <transition>
  
  from ref 132102 z 2001 to ref 131334
  write_horizontally default show_definition default drawing_language default
end
transitioncanvas 132614 transition_ref 142726 // <transition>
  
  from ref 128390 z 2001 to ref 131334
  write_horizontally default show_definition default drawing_language default
end
end

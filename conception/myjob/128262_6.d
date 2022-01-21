format 224

classcanvas 128006 class_ref 128262 // UserI
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 449.5 12.1 2000 183 237
end
classcanvas 128390 class_ref 128390 // Job
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 1245 595.3 2000 179 319
end
classcanvas 128518 class_ref 128518 // Profiluser
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 280.6 579.6 2000 140 243
end
classcanvas 128646 class_ref 128646 // Formation
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 839.4 213.6 2000 130 157
end
classcanvas 128774 class_ref 128774 // Competence
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 1333.2 169.6 2000 107 115
end
classcanvas 129542 class_ref 128902 // Experience
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyz 1262.4 328.6 2000
end
classcanvas 130950 class_ref 128134 // ProfilRetruteur
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyz 156.2 1078.7 2000
end
classcanvas 131462 class_ref 141958 // Profil
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyzwh 121.3 108.2 2005 179 159
end
note 132486 "ajouter le diagramme de sequence poyr rechercher un job 
plus diagramme de deploiement et
 
 de composant 
diagramme d 'etat d'un job
"
  xyzwh 110.5 1637.3 2000 213 175
classcanvas 133638 class_ref 155398 // Postuler
  classdiagramsettings member_max_width 0 end
  xyz 1007.8 554.7 2000
end
classcanvas 134918 class_ref 148742 // Metier
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyz 809.3 788 2006
end
classcanvas 136070 class_ref 162054 // ProfilUser
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_parameter_dir yes show_parameter_name yes end
  xyz 270.5 869.8 2006
end
classcanvas 136838 class_ref 162310 // JOb
  classdiagramsettings member_max_width 0 end
  xyz 1252.3 970.9 2005
end
classcanvas 138118 class_ref 162566 // User
  classdiagramsettings member_max_width 0 end
  xyzwh 361.9 285.1 2006 141 233
end
classcanvas 138886 class_ref 162694 // FormationI
  classdiagramsettings member_max_width 0 end
  xyz 853.5 8.5 2000
end
relationcanvas 129158 relation_ref 128518 // contenir
  decenter_begin 279
  decenter_end 500
  from ref 128518 z 2001 label "contenir" italic max_width 255 xyz 846 415 2001 to ref 128774
  no_role_a no_role_b
  multiplicity_a_pos 1300 231 3000 multiplicity_b_pos 429 651 3000
end
relationcanvas 132230 relation_ref 136710 // avoir
  decenter_begin 485
  decenter_end 459
  from ref 129542 z 2001 label "avoir" italic max_width 255 xyz 824 528 2001 to ref 128518
  no_role_a no_role_b
  multiplicity_a_pos 429 696 3000 multiplicity_b_pos 1244 410 3000
end
relationcanvas 132358 relation_ref 136838 // <realization>
  decenter_begin 164
  decenter_end 338
  from ref 130950 z 2006 to ref 131462
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 132614 relation_ref 136966 // avoir
  decenter_begin 551
  decenter_end 470
  from ref 128006 z 2006 label "avoir" italic max_width 255 xyz 358 140 2006 to ref 131462
  no_role_a no_role_b
  multiplicity_a_pos 313 188 3000 multiplicity_b_pos 427 147 3000
end
relationcanvas 132742 relation_ref 137094 // postuler
  decenter_begin 666
  decenter_end 279
  from ref 128518 z 2001 label "postuler" italic max_width 255 xyz 805 691 2001 to ref 128390
  no_role_a no_role_b
  multiplicity_a_pos 1227 693 3000 multiplicity_b_pos 429 749 3000
end
relationcanvas 132870 relation_ref 137222 // poster
  decenter_begin 846
  decenter_end 971
  from ref 130950 z 2001 label "poster" italic max_width 255 xyz 736 997 2001 to ref 128390
  no_role_a no_role_b
  multiplicity_a_pos 1212 911 3000 multiplicity_b_pos 280 1134 3000
end
relationcanvas 135174 relation_ref 157446 // demande
  decenter_begin 632
  decenter_end 534
  from ref 134918 z 2007 label "demande" italic max_width 255 xyz 1060 780 2007 to ref 128390
  no_role_a no_role_b
  multiplicity_a_pos 1208 770 3000 multiplicity_b_pos 951 841 3000
end
relationcanvas 135558 relation_ref 157702 // avoir
  decenter_begin 957
  from ref 128518 z 2007 label "avoir" italic max_width 255 xyz 598 797 2007 to ref 134918
  no_role_a no_role_b
  multiplicity_a_pos 790 833 3000 multiplicity_b_pos 429 820 3000
end
relationcanvas 136454 relation_ref 159878 // <realization>
  decenter_begin 563
  decenter_end 429
  from ref 136070 z 2007 to ref 128518
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 136582 relation_ref 160006 // <generalisation>
  decenter_begin 147
  decenter_end 952
  from ref 128518 z 2006 to ref 131462
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 136966 relation_ref 161670 // <realization>
  from ref 136838 z 2006 to ref 128390
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 138758 relation_ref 162310 // <realization>
  decenter_end 164
  from ref 138118 z 2007 to ref 128006
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 139526 relation_ref 162950 // avoir
  from ref 138886 z 2001 label "avoir" italic max_width 255 xyz 617 362 2001 to ref 128518
  no_role_a no_role_b
  multiplicity_a_pos 395 593 3000 multiplicity_b_pos 812 155 3000
end
relationcanvas 139782 relation_ref 163206 // <dependency>
  from ref 128646 z 2001 to ref 138886
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
line 134534 -_-_ decenter_begin 123
  from ref 133638 z 2002 to ref 132742
end

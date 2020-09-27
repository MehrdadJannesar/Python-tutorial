#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Sep 21, 2020 12:32:16 PM +0330  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x450+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4804 1325
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but45" "Button1" vTcl:WidgetProc "Toplevel1" 1
    spinbox $top.spi46 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable spinbox -to 100.0 
    vTcl:DefineAlias "$top.spi46" "Spinbox1" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.tEn47 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$top.tEn47" "TEntry1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.667 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.spi46 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.356 -width 0 -relwidth 0.293 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.tEn47 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.178 -height 0 -relheight 0.058 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}


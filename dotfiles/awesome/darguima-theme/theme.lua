---------------------------------
--  "Darguima" awesome theme   --
-- Forked from "Zenburn" theme --
--    By Dário G. (darguima)   --
---------------------------------

local themes_path = require("gears.filesystem").get_themes_dir()
local dpi = require("beautiful.xresources").apply_dpi

-- {{{ Main
local theme = {}
theme.wallpaper = themes_path .. "darguima-theme/zenburn-background.png"
-- }}}

-- {{{ Styles
theme.font      = "sans 8"

-- {{{ Colors
theme.fg_normal  = "#DCDCCC"
theme.fg_focus   = "#F0DFAF"
theme.fg_urgent  = "#CC9393"
theme.bg_normal  = "#3F3F3F"
theme.bg_focus   = "#1E2320"
theme.bg_urgent  = "#3F3F3F"
theme.bg_systray = theme.bg_normal
-- }}}

-- {{{ Borders
theme.useless_gap   = dpi(0)
theme.border_width  = dpi(2)
theme.border_normal = "#3F3F3F"
theme.border_focus  = "#6F6F6F"
theme.border_marked = "#CC9393"
-- }}}

-- {{{ Titlebars
theme.titlebar_bg_focus  = "#3F3F3F"
theme.titlebar_bg_normal = "#3F3F3F"
-- }}}

-- There are other variable sets
-- overriding the default one when
-- defined, the sets are:
-- [taglist|tasklist]_[bg|fg]_[focus|urgent|occupied|empty|volatile]
-- titlebar_[normal|focus]
-- tooltip_[font|opacity|fg_color|bg_color|border_width|border_color]
-- Example:
--theme.taglist_bg_focus = "#CC9393"
-- }}}

-- {{{ Widgets
-- You can add as many variables as
-- you wish and access them by using
-- beautiful.variable in your rc.lua
--theme.fg_widget        = "#AECF96"
--theme.fg_center_widget = "#88A175"
--theme.fg_end_widget    = "#FF5656"
--theme.bg_widget        = "#494B4F"
--theme.border_widget    = "#3F3F3F"
-- }}}

-- {{{ Mouse finder
theme.mouse_finder_color = "#CC9393"
-- mouse_finder_[timeout|animate_timeout|radius|factor]
-- }}}

-- {{{ Menu
-- Variables set for theming the menu:
-- menu_[bg|fg]_[normal|focus]
-- menu_[border_color|border_width]
theme.menu_height = dpi(15)
theme.menu_width  = dpi(100)
-- }}}

-- {{{ Icons
-- {{{ Taglist
theme.taglist_squares_sel   = themes_path .. "darguima-theme/taglist/squarefz.png"
theme.taglist_squares_unsel = themes_path .. "darguima-theme/taglist/squarez.png"
--theme.taglist_squares_resize = "false"
-- }}}

-- {{{ Misc
theme.awesome_icon           = themes_path .. "darguima-theme/awesome-icon.png"
theme.menu_submenu_icon      = themes_path .. "darguima-theme/submenu.png"
-- }}}

-- {{{ Layout
theme.layout_tile       = themes_path .. "darguima-theme/layouts/tile.png"
theme.layout_tileleft   = themes_path .. "darguima-theme/layouts/tileleft.png"
theme.layout_tilebottom = themes_path .. "darguima-theme/layouts/tilebottom.png"
theme.layout_tiletop    = themes_path .. "darguima-theme/layouts/tiletop.png"
theme.layout_fairv      = themes_path .. "darguima-theme/layouts/fairv.png"
theme.layout_fairh      = themes_path .. "darguima-theme/layouts/fairh.png"
theme.layout_spiral     = themes_path .. "darguima-theme/layouts/spiral.png"
theme.layout_dwindle    = themes_path .. "darguima-theme/layouts/dwindle.png"
theme.layout_max        = themes_path .. "darguima-theme/layouts/max.png"
theme.layout_fullscreen = themes_path .. "darguima-theme/layouts/fullscreen.png"
theme.layout_magnifier  = themes_path .. "darguima-theme/layouts/magnifier.png"
theme.layout_floating   = themes_path .. "darguima-theme/layouts/floating.png"
theme.layout_cornernw   = themes_path .. "darguima-theme/layouts/cornernw.png"
theme.layout_cornerne   = themes_path .. "darguima-theme/layouts/cornerne.png"
theme.layout_cornersw   = themes_path .. "darguima-theme/layouts/cornersw.png"
theme.layout_cornerse   = themes_path .. "darguima-theme/layouts/cornerse.png"
-- }}}

-- {{{ Titlebar
theme.titlebar_close_button_focus  = themes_path .. "darguima-theme/titlebar/close_focus.png"
theme.titlebar_close_button_normal = themes_path .. "darguima-theme/titlebar/close_normal.png"

theme.titlebar_minimize_button_normal = themes_path .. "darguima/titlebar/minimize_normal.png"
theme.titlebar_minimize_button_focus  = themes_path .. "darguima/titlebar/minimize_focus.png"

theme.titlebar_ontop_button_focus_active  = themes_path .. "darguima-theme/titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active = themes_path .. "darguima-theme/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive  = themes_path .. "darguima-theme/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive = themes_path .. "darguima-theme/titlebar/ontop_normal_inactive.png"

theme.titlebar_sticky_button_focus_active  = themes_path .. "darguima-theme/titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active = themes_path .. "darguima-theme/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive  = themes_path .. "darguima-theme/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive = themes_path .. "darguima-theme/titlebar/sticky_normal_inactive.png"

theme.titlebar_floating_button_focus_active  = themes_path .. "darguima-theme/titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active = themes_path .. "darguima-theme/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive  = themes_path .. "darguima-theme/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive = themes_path .. "darguima-theme/titlebar/floating_normal_inactive.png"

theme.titlebar_maximized_button_focus_active  = themes_path .. "darguima-theme/titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active = themes_path .. "darguima-theme/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive  = themes_path .. "darguima-theme/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = themes_path .. "darguima-theme/titlebar/maximized_normal_inactive.png"
-- }}}
-- }}}

return theme

-- vim: filetype=lua:expandtab:shiftwidth=4:tabstop=8:softtabstop=4:textwidth=80

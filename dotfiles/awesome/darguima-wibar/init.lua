-- dotfiles_environment = `desktop`, `laptop` or ...
-- Why? In `desktop`, for example, isn't needed to load battery or brightness widgtes.
local DotfilesEnvironment = require("awesome_modules/dotfiles").get_dotfiles_environment()

local awful = require("awful")
local dpi = require("beautiful.xresources").apply_dpi
local wibox = require("wibox")
local gears = require("gears")

-- https://awesomewm.org/doc/api/classes/awful.wibar.html

local function create(screen, theme)
  screen.mywibox = awful.wibar({
    position = "bottom", -- string The position.
    -- stretch = nil, -- string If the wibar need to be stretched to fill the screen.
    -- border_width = nil, -- integer Border width.
    -- border_color = nil, -- string Border color.
    -- ontop = nil, -- boolean On top of other windows. (default false)
    -- cursor = nil, -- string The mouse cursor.
    -- visible = nil, -- boolean Visibility.
    -- opacity = nil, -- number The opacity, between 0 and 1. (default 1)
    -- type = nil, -- string The window type (desktop, normal, dock, …).
    -- x = nil, -- integer The x coordinates.
    -- y = nil, -- integer The y coordinates.
    -- width = nil, -- integer The width.
    height = dpi(20), -- integer The height.
    screen = screen,  -- screen The wibox screen.
    -- widget = nil, -- wibox.widget The widget that the wibox displays.
    -- shape_bounding = nil, -- The wibox’s bounding shape as a (native) cairo surface.
    -- shape_clip = nil, -- The wibox’s clip shape as a (native) cairo surface.
    -- shape_input = nil, -- The wibox’s input shape as a (native) cairo surface.
    bg = theme.bg_normal, -- color The background.
    -- bgimage = nil, -- surface The background image of the drawable.
    -- fg = nil, -- color The foreground (text) color.
    -- shape = nil, -- gears.shape The shape.
    -- input_passthrough = nil, -- boolean If the inputs are forward to the element below. (default false)

  })

  return screen
end

-- Create a textclock widget
mytextclock = wibox.widget.textclock()

-- Create a wibox for each screen and add it
local taglist_buttons = gears.table.join(
  awful.button({}, 1, function(t) t:view_only() end),
  awful.button({ modkey }, 1, function(t)
    if client.focus then
      client.focus:move_to_tag(t)
    end
  end),
  awful.button({}, 3, awful.tag.viewtoggle),
  awful.button({ modkey }, 3, function(t)
    if client.focus then
      client.focus:toggle_tag(t)
    end
  end),
  awful.button({}, 4, function(t) awful.tag.viewnext(t.screen) end),
  awful.button({}, 5, function(t) awful.tag.viewprev(t.screen) end)
)

local tasklist_buttons = gears.table.join(
  awful.button({}, 1, function(c)
    if c == client.focus then
      c.minimized = true
    else
      c:emit_signal(
        "request::activate",
        "tasklist",
        { raise = true }
      )
    end
  end),
  awful.button({}, 3, function()
    awful.menu.client_list({ theme = { width = 250 } })
  end),
  awful.button({}, 4, function()
    awful.client.focus.byidx(1)
  end),
  awful.button({}, 5, function()
    awful.client.focus.byidx(-1)
  end))

local function add_widgets_to_wibox(screen, theme)
  if DotfilesEnvironment == "laptop" then
    BatteryWidget = require("battery-widget") {}
    BrightnessWidget = require("brightness")({ backend = "xbacklight" }).widget
  end

  -- Each screen has its own tag table.
  awful.tag({ "1", "2", "3", "4", "5", "6" }, screen, awful.layout.layouts[1])

  -- Create a promptbox for each screen
  screen.mypromptbox = awful.widget.prompt()
  -- Create an imagebox widget which will contain an icon indicating which layout we're using.
  -- We need one layoutbox per screen.
  screen.mylayoutbox = awful.widget.layoutbox(screen)
  screen.mylayoutbox:buttons(gears.table.join(
    awful.button({}, 1, function() awful.layout.inc(1) end),
    awful.button({}, 3, function() awful.layout.inc(-1) end),
    awful.button({}, 4, function() awful.layout.inc(1) end),
    awful.button({}, 5, function() awful.layout.inc(-1) end)))
  -- Create a taglist widget
  screen.mytaglist = awful.widget.taglist {
    screen  = screen,
    filter  = awful.widget.taglist.filter.all,
    buttons = taglist_buttons
  }

  -- Create a tasklist widget
  screen.mytasklist = awful.widget.tasklist {
    screen  = screen,
    filter  = awful.widget.tasklist.filter.currenttags,
    buttons = tasklist_buttons
  }

  screen.mywibox:setup {
    layout = wibox.layout.align.horizontal,
    {
      -- Left widgets
      layout = wibox.layout.fixed.horizontal,
      screen.mytaglist,
      screen.mypromptbox,
    },

    screen.mytasklist, -- Middle widget

    {
      -- Right widgets
      layout = wibox.layout.fixed.horizontal,
      wibox.widget.systray(),
      BatteryWidget,
      BrightnessWidget,
      mytextclock,
      screen.mylayoutbox,
    },
  }

  return screen
end

return {
  create = create,
  add_widgets_to_wibox = add_widgets_to_wibox
}

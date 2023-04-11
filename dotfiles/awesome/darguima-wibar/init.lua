local awful = require("awful")
local dpi = require("beautiful.xresources").apply_dpi


-- https://awesomewm.org/doc/api/classes/awful.wibar.html

local function create(screen, theme)
  return awful.wibar({
    position = "bottom",
    screen = screen,
    bg = theme.bg_normal,
  })
end

return {
  create = create
}

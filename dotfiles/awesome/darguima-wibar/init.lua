local awful = require("awful")
local dpi = require("beautiful.xresources").apply_dpi

local function create(theme)
  return awful.wibar({
    position = "bottom",
    screen = s,
    bg = theme.bg_normal
  })
end

return {
  create = create
}

# -*- encoding: utf-8 -*-
# Lk_brightness specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_brightness"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_brightness.rb" ]
  s.icons       = [ "light1.xbm"]

  # Sublet description
  s.description = "show and change brightness"
  s.notes       = <<NOTES
show and change brightness
!! need /sys/class/backlight/acpi_video0/brightness, max_brightness
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "YOUREMAIL"
  s.date        = "Wed May 15 14:57 CST 2013"

  # Sublet config
  s.config = [
    {
      :name        => "interval",
      :type        => "integer",
      :description => "Update interval in seconds",
      :def_value   => "60"
    },
    {
        :name           =>  "path",
        :type           =>  "string",
        :description    =>  "Path to directory containing brightness and max_brightness",
        :def_value      =>  "/sys/class/backlight/acpi_video0"
    }
  ]

  # Sublet grabs
  s.grabs = {
    :BrightCtrl => "Updates the brightness sublet",
    :BrightUp => "up the brightness",
    :BrightDown => "down the brightness"
  }

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

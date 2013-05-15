# -*- encoding: utf-8 -*-
# Lk_temp specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_temp"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_temp.rb" ]
  s.icons       = [ "temp.xbm" ]

  # Sublet description
  s.description = "show temp"
  s.notes       = <<NOTES
show temp
CAUTION: need /sys/class/hwmon and /sys/class/thermal/
ALERT: YOU MUST SET the core, sys value in conf, just type sur config lk_temp
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Tue May 14 16:19 CST 2013"

  # Sublet config
  s.config      = [
    {
      :name        => "core",
      :type        => "array",
      :description => "the monitor string array  in /sys/class/hwmon/hwmon?/device/temp?_input",
      :def_value   => ["/sys/class/hwmon/hwmon0/device/temp2_input", "/sys/class/hwmon/hwmon0/device/temp4_input"]
    },
    {
      :name        => "sys",
      :type        => "array",
      :description => "the monitor string array  in /sys/class/thermal/thermal_zone?/temp",
      :def_value   => [ "/sys/class/thermal/thermal_zone0/temp", "/sys/class/thermal/thermal_zone1/temp"]
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :Lk_tempGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

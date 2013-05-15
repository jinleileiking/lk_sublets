# -*- encoding: utf-8 -*-
# Lk_wifi specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_wifi"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_wifi.rb" ]
  s.icons       = [ "icons/wifi.xbm"]

  # Sublet description
  s.description = "Show the link quality of a wifi device"
  s.notes       = <<NOTES
Show wifi quality and bssid, essid
Caution: need /proc/net/wireless
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Tue May 14 15:26 CST 2013"

  # Sublet config
  s.config      = [
    {
      :name        => "device",
      :type        => "string",
      :description => "Name of the monitored device (like wlan0)",
      :def_value   => "wlan0"
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :Lk_wifiGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

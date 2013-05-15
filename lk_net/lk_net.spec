# -*- encoding: utf-8 -*-
# Lk_net specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_net"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_net.rb" ]
  s.icons       = [ "rx.xbm", "tx.xbm" ]

  # Sublet description
  s.description = "display net rx/tx in KBps"
  s.notes       = <<NOTES
display net rx/tx in KBps
CAUTION: need /sys/class/net
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Tue May 14 15:43 CST 2013"

  # Sublet config
  s.config = [
    {
      :name        => "iface_name",
      :type        => "string",
      :description => "interface name",
      :def_value   => "wlan0"
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :Lk_netGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

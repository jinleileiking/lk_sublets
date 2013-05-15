# -*- encoding: utf-8 -*-
# Lk_uptime specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_uptime"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_uptime.rb" ]
  s.icons       = [ "off.xbm" ]

  # Sublet description
  s.description = "show uptime"
  s.notes       = <<NOTES
show uptime
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "YOUREMAIL"
  s.date        = "Wed May 15 15:55 CST 2013"

  # Sublet config
  #s.config = [
  #  {
  #    :name        => "Value name",
  #    :type        => "Value type",
  #    :description => "Description",
  #    :def_value   => "Default value"
  #  }
  #]

  # Sublet grabs
  #s.grabs = {
  #  :Lk_uptimeGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

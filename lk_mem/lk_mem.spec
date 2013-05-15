# -*- encoding: utf-8 -*-
# Lk_mem specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_mem"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_mem.rb" ]
  s.icons       = [ "memory.xbm" ]

  # Sublet description
  s.description = "show mem"
  s.notes       = <<NOTES
show mem
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Wed May 15 09:56 CST 2013"

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
  #  :Lk_memGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

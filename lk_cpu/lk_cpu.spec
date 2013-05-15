# -*- encoding: utf-8 -*-
# Lk_cpu specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_cpu"
  s.version     = "0.2"
  s.tags        = [ ]
  s.files       = [ "lk_cpu.rb" ]
  s.icons       = [ "cpu.xbm"]

  # Sublet description
  s.description = "show cpu use"
  s.notes       = <<NOTES
show cpu use
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Tue May 14 15:12 CST 2013"

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
  #  :Lk_cpuGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

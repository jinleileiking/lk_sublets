# -*- encoding: utf-8 -*-
# Lk_freq specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_freq"
  s.version     = "0.1"
  s.tags        = [ ]
  s.files       = [ "lk_freq.rb" ]
  s.icons       = [ ]

  # Sublet description
  s.description = "show freq in Ghz"
  s.notes       = <<NOTES
show freq in Ghz
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Mon May 13 17:12 CST 2013"

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
  #  :Lk_freqGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

# -*- encoding: utf-8 -*-
# Lk_clock specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Lk_clock"
  s.version     = "0.0"
  s.tags        = [ ]
  s.files       = [ "lk_clock.rb" ]
  s.icons       = [ "clock.xbm" ]

  # Sublet description
  s.description = "clock with icon"
  s.notes       = <<NOTES
clock
NOTES

  # Sublet authors
  s.authors     = [ "jinleileiking" ]
  s.contact     = "jinleileiking@gmail.com"
  s.date        = "Tue May 14 16:06 CST 2013"

  # Sublet config
	s.config      = [
		{
			:name        => 'time_format',
			:type        => 'string',
			:def_value   => '%H:%M',
			:description => 'Time format. (man date)'
		},
		{
			:name        => 'date_format',
			:type        => 'string',
			:def_value   => '%y/%m/%d',
			:description => 'Date format. (man date)'
		},
		{
			:name        => 'time_color',
			:type        => 'string',
			:def_value   => '#B8B8B8',
			:description => 'Time color.'
		},
		{
			:name        => 'date_color',
			:type        => 'string',
			:def_value   => '#757575',
			:description => 'Date color.'
		}
	]

  # Sublet grabs
  #s.grabs = {
  #  :Lk_clockGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end

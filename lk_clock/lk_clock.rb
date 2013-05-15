# Lk_clock sublet file
# Created with sur-0.2
configure :lk_clock do |s|
	s.interval = s.config[:interval] || 60
	
	s.time_format = s.config[:time_format] || '%H:%M'
	s.date_format = s.config[:date_format] || '%y/%m/%d'
	
	s.time_color = Subtlext::Color.new(s.config[:time_color] || '#B8B8B8')
	s.date_color = Subtlext::Color.new(s.config[:date_color] || '#757575')
    s.icon     = Subtlext::Icon.new("clock.xbm")
end

on :run do |s|
	s.data = s.icon + s.time_color + Time.now().strftime(s.time_format) + ' ' + s.date_color + Time.now().strftime(s.date_format)
end

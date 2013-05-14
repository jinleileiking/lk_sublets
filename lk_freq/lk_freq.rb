# Lk_freq sublet file
# Created with sur-0.2


configure :lk_freq do |s|
  s.interval = 2
end

on :run do |s|
  begin
    data = ""
    file = IO.readlines("/proc/cpuinfo").join

    file.scan(/cpu MHz\s+:\s+([0-9.]+)/) do |freq| 
      data << (Float(freq.first.to_i) / 1000).round(1).to_s + "G "
#       data << freq.first.to_i.to_s + "G "
    end

    s.data = data.chop
  rescue => err # Sanitize to prevent unloading
    s.data = "subtle"
    p err
  end  
end

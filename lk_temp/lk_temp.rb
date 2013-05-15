# Lk_temp sublet file
# Created with sur-0.2
#

helper do
  def read_value(path)
    ret = nil

    if(File.exist?(path))
      ret = IO.readlines(path).first.chop
    end

    ret
  end

  def get_temp(path)
    cur_temp = read_value(path).to_f
    cur_temp = cur_temp / 1000
    return cur_temp
  rescue
    cur_temp = 0.0
    return cur_temp
  end
end



configure :lk_temp do |s|
  s.interval = 60
  s.icon     = Subtlext::Icon.new("temp.xbm")
  s.core = s.config[:core] ||  ["/sys/class/hwmon/hwmon0/device/temp2_input", "/sys/class/hwmon/hwmon0/device/temp4_input"]
  s.sys = s.config[:sys] ||  [ "/sys/class/thermal/thermal_zone0/temp", "/sys/class/thermal/thermal_zone1/temp"]
end

on :run do |s|
  begin
    core = []
    sys = []

    s.core.each do |mon|
        temp = get_temp(mon)
        core << temp.round(0).to_s + "°C"
    end
    
    s.sys.each do |mon|
        temp = get_temp(mon)
        sys << temp.round(0).to_s + "°C"
    end

    if core == nil || sys == nil
        s.data = "ERR"
        return
    end
    s.data = "%s%s|%s" % [ s.icon, core.join("/"), sys.join("/") ]

  rescue => err # Sanitize to prevent unloading
    s.data = "subtle"
    p err, err.backtrace
  end
end

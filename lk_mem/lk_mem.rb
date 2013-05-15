# Lk_mem sublet file
# Created with sur-0.2
configure :lk_mem do |s|
  s.interval = 1
  s.icon     = Subtlext::Icon.new("memory.xbm")
end

on :run do |s|
  file = ""

  begin
    File.open("/proc/meminfo", "r") do |f|
      file = f.read
    end

    # Collect data
    total   = file.match(/MemTotal:\s*(\d+)\s*kB/)[1].to_i || 0
    free    = file.match(/MemFree:\s*(\d+)\s*kB/)[1].to_i || 0
    buffers = file.match(/Buffers:\s*(\d+)\s*kB/)[1].to_i || 0
    cached  = file.match(/Cached:\s*(\d+)\s*kB/)[1].to_i || 0

    used    = (total - (free + buffers + cached)) / 1024
    total   = total / 1024

    s.data = s.icon + "%4d" % used + "/" + "%4d" % total + "M" + "(#{"%3d" % (used.to_f/total.to_f * 100).round(0)}%)"
  rescue => err # Sanitize to prevent unloading
    s.data = "subtle"
    p err
  end
end

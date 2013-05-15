# Lk_net sublet file
# Created with sur-0.2
#
#

helper do
  def read_byte_counters(iface_name)
    rx_bytes = IO.readlines("/sys/class/net/#{iface_name}/statistics/rx_bytes")[0].to_i
    tx_bytes = IO.readlines("/sys/class/net/#{iface_name}/statistics/tx_bytes")[0].to_i
    return rx_bytes, tx_bytes
  end
end

configure :lk_net do |s|
  s.interval = 1
  s.iface_name = s.config[:iface_name] || "wlan0"
  s.last_counters = read_byte_counters(s.iface_name)
  s.icon_tx     = Subtlext::Icon.new("tx.xbm")
  s.icon_rx     = Subtlext::Icon.new("rx.xbm")
end

on :run do |s|
  current_counters = read_byte_counters(s.iface_name)
  rx_speed = (current_counters[0] - s.last_counters[0])/1000/s.interval
  tx_speed = (current_counters[1] - s.last_counters[1])/1000/s.interval
  s.last_counters = current_counters
  s.data = s.icon_rx + "%4dKB/s" % [rx_speed] + s.icon_tx + "%4dKB/s" % [tx_speed]
end

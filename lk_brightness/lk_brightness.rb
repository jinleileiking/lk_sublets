# Lk_brightness sublet file
# Created with sur-0.2
#
#

helper do

  def read_value(path)
    ret = nil

    if(File.exist?(path))
      ret = IO.readlines(path).first.chop
    end

    ret
  end

    def up
        val_before = read_value File.join(self.path, "brightness")

        if (val_before.to_i + 1 > read_value(File.join(self.path, "max_brightness")).to_i)
            return
        end

        system "sudo sh -c 'echo #{val_before.to_i + 1} >>" + self.path.to_s + "brightness'"
    end

    def down
        val_before = read_value File.join(self.path, "brightness")

        if val_before.to_i == 0 
            return
        end

        system "sudo sh -c 'echo #{val_before.to_i - 1} >>" + self.path.to_s + "brightness'"
    end

    def update
        brightness = File.open(File.expand_path("brightness", self.path)).first.to_f
        max_brightness = File.open(File.expand_path("max_brightness", self.path)).first.to_f
        percent = brightness/max_brightness * 100
        percent = (percent.round 0).to_i
        percent_str = "#{percent}%"
#         if percent < 10
#             percent_str = "  #{percent}%"
#         elsif percent < 100
#             percent_str = " #{percent}%"
#         end
        self.data = self.icon + "%3d%" % percent
    end
end


configure :lk_brightness do |s|
  s.interval = s.config[:interval] || 60
  s.path = s.config[:path] || "/sys/class/backlight/acpi_video0/"
  s.icon = Subtlext::Icon.new("light1.xbm")
end

on :run do |s|
    s.update
end

grab :BrightCtrl do |s, c|
    s.update
    s.render
end


on :mouse_down do |s, x, y, b| # {{{
  case b
#     when 1 then s.mixer.toggle
    when 4 then s.up
    when 5 then s.down
  end
  s.update
  s.render

end # }}}



grab :BrightUp do |s, c|
    s.up
    s.render
end

grab :BrightDown do |s, c|
    s.down
    s.render
end

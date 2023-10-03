#!/usr/bin/env ruby
user_in = ARGV[0]
len = 0
check = 0
user_in.each_char do |char|
  if char.match(/[0-9]/)
    len += 1
  else
    check += 1
  end
end

if len == 10 && check == 0
  puts ARGV[0]
else
  puts ""
end

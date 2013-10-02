#/usr/bin/ruby

require "./nik_math.rb"

div = 2
num = 600851475143
while div < num / 2 do
  if num % div == 0
    test = num / div
    if is_prime(test)
      puts test
      break
    end
  end
  div += 1
end

puts "\n"

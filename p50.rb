#/usr/bin/ruby

require "./nik_math.rb"

max = 41
max = 1000
max = 1000000

highest = {
    "count" => 0,
    "sum" => 0,
    "final" => []
}
sum = 2

# build an array of all primes up to max
primes = [2]
number = 3
while number < max
    if is_prime(number)
        primes.push(number)
    end
    number += 2
end

# add primes with a sliding start
primes.each_index do |index|

    if primes[index] <= Math.sqrt(max).to_i

        print "Trying " + primes[index].to_s + ": "

        sum = 0
        final = []

        while index < primes.length
            if (sum + primes[index]) < max
                sum += primes[index]
                final.push(primes[index])
            else
                break
            end
            index += 1
        end

        puts final.length.to_s + " (sum: " + sum.to_s + ")"

        if final.length > highest["count"] && is_prime(sum)
            highest["count"] = final.length
            highest["sum"] = sum
            highest["final"] = final
            puts "New record!"
        end
    end
end

puts "-----"
puts "Count: " + highest["count"].to_s
puts "Sum: " + highest["sum"].to_s
puts "Primes: " + highest["final"].to_s

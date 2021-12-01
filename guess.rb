number = rand(1..20)

puts 'Hello! What is your name?'
name = gets&.chomp

puts "Hi, #{name}. I'm thinking of a number between 1 and 20."

1.upto 6 do |guesses|
  puts "What is your guess? You have #{7 - guesses} more guesses."
  guess = gets&.chomp.to_i

  if guess == number
    puts "Good job, #{name}! You guessed my number in #{guesses} guesses."
    exit
  else
    puts(guess > number ? 'Too high' : 'Too low')
  end
end

puts "Nope. The number I was thinking of was #{number}."

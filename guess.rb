number = rand(1..20)
guesses = 0

puts 'Hello! What is your name?'
name = gets.chomp.to_s

puts "Hi, #{name}. I'm thinking of a number between 1 and 20." 

while guesses < 6

  puts "What is your guess? You have #{6-guesses} more guesses."
  guess = gets.chomp.to_i
  guesses += 1

  unless guess == number
    message = if guess > number
                "Too high"
              else
                "Too low"
              end
    puts message
  else
    puts "Good job, #{name}! You guessed my number in #{guesses} guesses."
    exit
  end

end

puts "Nope. The number I was thinking of was #{number}."


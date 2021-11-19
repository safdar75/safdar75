# Thank you for playing my game and improving it! Peace, love and code ♡ ~cajudeleite

# V2 Update Log
# - Transformed the cards array into a hash
# - Now the player can choose the Ases values between 1 or 11
# - Some bug fixes in multi-argument conditionals
# - Some fixes on informations displayed to the player
# - Fixed player choice of playing again or not
# - Fixed user input information
# - Added a 'Want to play again' screen
# - Added a 'You lost' screen when player doens't have credits anymore

require 'pry-byebug'
system 'clear'
# Card library
cards_hash = { 'A♠' => 11,
               '2♠' => 2,
               '3♠' => 3,
               '4♠' => 4,
               '5♠' => 5,
               '6♠' => 6,
               '7♠' => 7,
               '8♠' => 8,
               '9♠' => 9,
               '10♠' => 10,
               'J♠' => 10,
               'Q♠' => 10,
               'K♠' => 10,
               'A♡' => 11,
               '2♡' => 2,
               '3♡' => 3,
               '4♡' => 4,
               '5♡' => 5,
               '6♡' => 6,
               '7♡' => 7,
               '8♡' => 8,
               '9♡' => 9,
               '10♡' => 10,
               'J♡' => 10,
               'Q♡' => 10,
               'K♡' => 10,
               'A♣' => 11,
               '2♣' => 2,
               '3♣' => 3,
               '4♣' => 4,
               '5♣' => 5,
               '6♣' => 6,
               '7♣' => 7,
               '8♣' => 8,
               '9♣' => 9,
               '10♣' => 10,
               'J♣' => 10,
               'Q♣' => 10,
               'K♣' => 10,
               'A♢' => 11,
               '2♢' => 2,
               '3♢' => 3,
               '4♢' => 4,
               '5♢' => 5,
               '6♢' => 6,
               '7♢' => 7,
               '8♢' => 8,
               '9♢' => 9,
               '10♢' => 10,
               'J♢' => 10,
               'Q♢' => 10,
               'K♢' => 10 }
# Card library

# Credit
credit = 100
# Credit
play = true
while play
  # Set game constants
  game_is_on = true
  player_total_score = 0
  croupier_total_score = 0
  player_cards = ''
  player_new_pick = []
  answer = ''
  croupier_new_pick = []
  croupier_hand = ''
  bet = 0
  bet_valid = false
  double = 1
  cards_hash['A♠'] = 11
  cards_hash['A♡'] = 11
  cards_hash['A♣'] = 11
  cards_hash['A♢'] = 11
  # Set game constants

  # Player makes bets
  puts "Here are your credits : #{credit}$"
  puts 'Make your bets:'
  bet = gets.chomp.to_i

  until bet_valid
    if bet <= credit
      bet_valid = true
    else
      puts 'Invalid bet. Please make a valid bet:'
      bet = gets.chomp.to_i
    end
  end
  # Player makes bets

  # Croupier 1rst pick
  croupier_1rst_pick = cards_hash.to_a.sample
  croupier_2nd_pick = cards_hash.to_a.sample
  croupier_total_score = croupier_1rst_pick[1] + croupier_2nd_pick[1]
  croupier_total_score = 12 if croupier_total_score == 22
  # Croupier 1rst pick

  # Player first pick
  player_1rst_pick = cards_hash.to_a.sample
  player_2nd_pick = cards_hash.to_a.sample
  player_cards = "#{player_1rst_pick[0]} ~~~ #{player_2nd_pick[0]}"
  player_total_score = player_1rst_pick[1] + player_2nd_pick[1]
  player_total_score = 12 if player_total_score == 22
  # Player first pick

  # Show the cards
  puts 'Croupier cards:'
  puts ''
  puts "### ~~~ #{croupier_2nd_pick[0]}"
  puts ''
  puts 'These are your cards:'
  puts ''
  puts player_cards
  puts ''
  puts 'Here is your score:'
  puts player_total_score
  sleep(3)
  # Show the cards

  # If player and/or croupier do Black Jack
  if player_total_score == 21 && croupier_total_score == 21
    puts 'Push! Both did Black Jack'
    game_is_on = false
  elsif player_total_score == 21
    puts 'Black Jack!'
    credit += (bet * 2.5).round
    game_is_on = false
  elsif croupier_total_score == 21
    puts 'Black Jack from the croupier! Better luck next time'
    credit -= bet
    game_is_on = false
  end
  # If player and croupier do Black Jack

  # Ask and choose what to do next
  if game_is_on
    puts 'What do you want to do next?'
    puts ''
    puts 'Draw   ~~~   Double   ~~~   Stick'
    answer = gets.chomp.capitalize
    puts ''
    until answer == 'Draw' || answer == 'Double' || answer == 'Stick'
      puts "I didn't understand, repeat your choice:"
      answer = gets.chomp.capitalize
    end
    system 'clear'
  end
  # Ask and choose what to do next

  # Changing As values to be flexible
  cards_hash['A♠'] = 'flexible'
  cards_hash['A♡'] = 'flexible'
  cards_hash['A♣'] = 'flexible'
  cards_hash['A♢'] = 'flexible'
  # Changing As values to be flexible

  # If player doubles
  if game_is_on && answer == 'Double' && player_total_score < 21
    double = 2
    player_new_pick = cards_hash.to_a.sample
    player_cards = "#{player_cards} ~~~ #{player_new_pick[0]}"
    puts "You chose to #{answer}!"
    puts 'Croupier cards:'
    puts ''
    puts "### ~~~ #{croupier_2nd_pick[0]}"
    puts ''
    puts 'These are your cards:'
    puts ''
    puts player_cards
    puts ''
    if player_new_pick[1] == 'flexible'
      as_constant = false
      until as_constant
        puts "You want your #{player_new_pick[0]} to value as a 1 or a 11?"
        new_as_value = gets.chomp.to_i
        if new_as_value == 11
          player_new_pick[1] = 11
          as_constant = true
        elsif new_as_value == 1
          player_new_pick[1] = 1
          as_constant = true
        end
      end
    end
    player_total_score += player_new_pick[1]
    puts 'Here is your score:'
    puts player_total_score
    sleep(3)
    if player_total_score > 21
      puts 'You burned out! Better luck next time'
      credit -= (bet * double)
      game_is_on = false
    end
  end
  # If player doubles

  # If player draws
  while game_is_on && answer == "Draw" && player_total_score < 21
    player_new_pick = cards_hash.to_a.sample
    player_cards = "#{player_cards} ~~~ #{player_new_pick[0]}"
    system 'clear'
    puts "You chose to #{answer}!"
    puts 'Croupier cards:'
    puts ''
    puts "### ~~~ #{croupier_2nd_pick[0]}"
    puts ''
    puts 'These are your cards:'
    puts ''
    puts player_cards
    puts ''
    if player_new_pick[1] == 'flexible'
      as_constant = false
      until as_constant
        puts "You want your #{player_new_pick[0]} to value as a 1 or a 11?"
        new_as_value = gets.chomp.to_i
        if new_as_value == 11
          player_new_pick[1] = 11
          as_constant = true
        elsif new_as_value == 1
          player_new_pick[1] = 1
          as_constant = true
        end
      end
    end
    player_total_score += player_new_pick[1]
    puts 'Here is your score:'
    puts player_total_score
    sleep(3)
    if player_total_score > 21
      puts 'You burned out! Better luck next time'
      credit -= (bet * double)
      game_is_on = false
    elsif player_total_score < 21
      puts 'What do you want to do next?'
      puts ''
      puts 'Draw   ~~~   Stick'
      answer = gets.chomp.capitalize
      puts ''
      until answer == 'Draw' || answer == 'Stick'
        system 'clear'
        puts "I didn't understand, repeat your choice:"
        answer = gets.chomp.capitalize
      end
      system 'clear'
      puts "You chose to #{answer}!"
      sleep(3)
    end
  end
  # If player draws

  # Show the game
  if game_is_on
    system 'clear'
    puts "You chose to #{answer}!"
    puts 'Croupier cards:'
    puts ''
    croupier_hand = "#{croupier_1rst_pick[0]} ~~~ #{croupier_2nd_pick[0]}"
    puts croupier_hand
    puts ''
    puts 'These are your cards:'
    puts ''
    puts player_cards
    sleep(3)
  end
  # Show the game

  # Croupier plays
  while game_is_on && croupier_total_score < player_total_score && croupier_total_score < 17
    croupier_new_pick = cards_hash.to_a.sample
    croupier_total_score += croupier_new_pick[1]
    croupier_hand = "#{croupier_hand} ~~~ #{croupier_new_pick[0]}"
    system 'clear'
    puts 'Croupier cards:'
    puts ''
    puts croupier_hand
    puts ''
    puts 'These are your cards:'
    puts ''
    puts player_cards
    sleep(3)
  end
  # Croupier plays

  # Game results
  if game_is_on
    if croupier_total_score == player_total_score
      puts 'Push!'
    elsif croupier_total_score > 21
      puts 'Croupier burned out!'
      credit += (bet * double)
      game_is_on = false
    elsif croupier_total_score > player_total_score
      puts "Croupier's score is #{croupier_total_score}! You lost. Better luck next time"
      credit -= (bet * double)
      game_is_on = false
    else
      puts "Croupier's score is #{croupier_total_score}! You won!"
      credit += (bet * double)
      game_is_on = false
    end
  end
  # Game results

  # End game
  sleep(5)
  system 'clear'
  puts "Here are your credits : #{credit}$"
  if credit > 0
    puts 'Want to play again?'
    play_q = gets.chomp.downcase
    if play_q == 'y' || play_q == 'yes'
      play = true
    else
      puts "Are you sure you want to quit?"
      confirmation = gets.chomp
      if confirmation == 'y' || confirmation == 'yes'
        play = false
        puts "Bye bye"
      end
    end
  else
    puts "You lost! You don't have any credits left"
    play = false
  end
  sleep(3)
  system 'clear'
  # End Game
end

# For the next patch:
# Player can't double if (2 * bet) > credit
# Croupier can choose ases values automaticaly
# Player and croupier can change already ases chosen values if it burns out
# ? Player can split if it gets two same card in the beggining (like two queens or two fives) ?

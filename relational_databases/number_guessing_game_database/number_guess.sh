#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

echo -e "Enter your username:"
read USERNAME

USER_INFO=$($PSQL "SELECT games_played, best_game FROM users WHERE username='$USERNAME'")

if [[ -z $USER_INFO ]]
then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  INSERT_USER=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME')")
else
  read GAMES_PLAYED BEST_GAME < <(IFS="|" && echo $USER_INFO) 
  echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
fi

SECRET_NUMBER="$((($RANDOM%1000)+1))"

echo "Guess the secret number between 1 and 1000:"
GUESS=-1
NUM_GUESSES=0

while [[ $SECRET_NUMBER != $GUESS ]]
do
  read GUESS
  if [[ ! $GUESS =~ ^[0-9]+$ ]]
  then
    echo "That is not an integer, guess again:"
  elif [[ $GUESS -lt $SECRET_NUMBER ]]
  then
    echo "It's higher than that, guess again:"
  elif [[ $GUESS -gt $SECRET_NUMBER ]]
  then
    echo "It's lower than that, guess again:"
  fi
  NUM_GUESSES=$(($NUM_GUESSES+1))
done

if [[ -z $BEST_GAME || $NUM_GUESSES -lt $BEST_GAME ]]
then
  UPDATE_INFO=$($PSQL "UPDATE users SET games_played=games_played+1, best_game=$NUM_GUESSES WHERE username='$USERNAME'")
else
  UPDATE_INFO=$($PSQL "UPDATE users SET games_played=games_played+1 WHERE username='$USERNAME'")
fi

echo "You guessed it in $NUM_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"


#!/bin/bash

if [[ $(ls|grep "users.tsv") == "" ]]; then             # To create users.tsv
        touch users.tsv
        echo -e "Username\tPassword" >> users.tsv
fi

# Checking whether the user exists
check_existing_user(){
        grep -q "^$1$(printf '\t')" users.tsv
}

# Hashing the Password
hash_password(){
        echo -n "$1" | sha256sum | cut -d "-" -f 1 | tr -d ' '
}

# Signing up if the player is first time user
signup(){

        while true;
        do
                echo >&2                # echo is used for spacing between read prompts
                read -p "Setup your Username: " new_username

                if [[ "$new_username" == "" ]]; then
                # echo "comment" >&2 is used to print directly to terminal instead of storing in player variable
                        echo -e "\n\033[0;31mUsername cannot be empty.Please Enter valid username.\033[0m" >&2
                        continue
                fi
                if check_existing_user "$new_username"; then                    # Ensuring unique username.
                        echo -e "\n\033[0;31mThis username has already been taken.Try another one.\033[0m" >&2
                        continue
                else
                        break
                fi
        done

        while true;
        do
                echo >&2
                read -s -p "Setup New Password: " password
                echo >&2
                if [[ "$password" == "" ]]; then
                        echo -e "\n\033[0;31mPassword cannot be empty, Please try again.\033[0m" >&2
                        continue
                elif [[ ! "$password" =~ [A-Za-z] ]]; then              # Ensuring password is strong enough.
                        echo -e "\n\033[0;31mPassword isn't strong enough. It should contain atleast 6 characters, 1 digit (0-9) and an alphabet (A-Z or a-z)\033[0m" >&2
                        continue
                elif [[ ! "$password" =~ [0-9] ]]; then
                        echo -e "\n\033[0;31mPassword isn't strong enough. It should contain atleast 6 characters, 1 digit (0-9) and an alphabet (A-Z or a-z)\033[0m" >&2
                        continue
                elif [[ ${#password} -lt 6 ]]; then
                        echo -e "\n\033[0;31mPassword isn't strong enough. It should contain atleast 6 characters, 1 digit (0-9) and an alphabet (A-Z or a-z)\033[0m" >&2
                        continue
                fi

                echo >&2
                read -s -p "Confirm your password: " confirm_password           # Confirming the new Password.
                echo >&2

                if [[ "$password" != "$confirm_password" ]]; then
                        echo -e "\n\033[0;31mPasswords donot match, Please set the password again.\033[0m" >&2
                else
                        break
                fi
        done

        hashed_password=$(hash_password "$password")
        echo -e "$new_username\t$hashed_password" >> users.tsv                  # Storing new user data in users.tsv
        echo -e "\n\033[0;32mYour account has been created successfully\nPlease log in to continue.\n\033[0m" >&2
}

# Checking password during Log in
login_password(){
        username=$1
        while true;
        do
                echo >&2
                read -s -p "Enter your password: " password
                echo >&2
                input_hash=$(hash_password "$password")
                stored_hash=$(grep "^$username$(printf '\t')" users.tsv | cut -f 2 | tr -d ' ')         # Extracting stored password.

                        if [[ "$input_hash" != "$stored_hash" ]]; then                  # Comparing Password with stored data.
                                echo -e "\n\033[0;31mPasswords donot match, Please try again.\033[0m" >&2
                        else
                                echo -e "\n\033[0;32m$username logged in succefully\033[0m" >&2
                        break
                fi
        done
}
# Checking User details during Log in
authenticate_user(){
        while true;
        do
                echo >&2
                read -p "Enter Username (If you are first time user Enter '#') : " username     # Prmopting for login and signup

                if [[ "$username" == "#" ]]; then
                        signup                  # Opening signup form.
                        continue
                fi
                if [[ "$username" == "" ]]; then
                        echo -e "\n\033[0;31mUsername should have atleast 1 character, Please try again.\033[0m" >&2
                        continue
                fi
                if check_existing_user "$username"; then
                        if [[ ${#players[@]} -eq 0 ]]; then                   # Condition for ensuring distinct players.
                                players[0]="$username"
                        elif [[ "$username" != "${players[0]}" ]]; then
                                players[1]="$username"
                        else
                                echo -e "\n\033[0;31mPlayers must be distinct, Please try again.\033[0m" >&2
                                continue
                        fi
                        login_password "$username"
                        return
                else
                        echo -e "\n\033[0;31mThis username does not exist, Please try again.\033[0m" >&2
                fi
        done
}

# Function for keeping text messages at center
center() {
        msg="$1"
        pad=$(( ($(tput cols) - ${#msg}) / 2 ))
        printf "%*s%s\n\n" $pad "" "$msg"
}

echo
echo
center "WELCOME TO THE WORLD OF MINI GAME HUB"

# Storing Usernames in array of players
players=()
center "User Authentication for Player 1"
authenticate_user

center "User Authentication for Player 2"
authenticate_user

echo -e "\n\033[0;32mPlayers logged in succefully!\033[0m\n"
echo -e "Let's start the game between ${players[0]} and ${players[1]}\n"
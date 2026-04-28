#!/bin/bash

touch tmp.csv sorted.csv               # Created temporary files to store intermediate results

get_games(){
        cut -d "," -f 4 history.csv | tail -n +2 | sort | uniq                       # Extract all games from history.csv
}

get_players(){                                                  # Extracting unique players
        awk -F, -v game="$1" '
        $4==game {
        print $1
        print $2
        }' history.csv | sort | uniq
}

# calculating all statistics like wins, losses, wins/loss ratio

generate_statistics(){

        tail -n +2 history.csv > tmp_history.csv              # Read from 2nd line

        while read -r game; do
                while read -r player; do
                        wins=0
                        losses=0
                        ratio=9999                            # default ratio for '0' losses
                        while IFS=',' read -r winner loser date g isdraw; do
                                if [[ "$g" != "$game" ]]; then                 # skip if not current game
                                        continue
                                fi
                                if [[ "$isdraw" == "no" ]];then                # if not draw
                                        if [[ "$winner" == "$player" ]];then
                                                wins=$(awk "BEGIN {print $wins + 1}")
                                        elif [[ "$loser" == "$player" ]]; then
                                                ((losses++))
                                        fi
                                # if the game is draw
                                else
                                        if [[ "$player" == "$winner" || "$player" == "$loser" ]];then
                                                wins=$(awk "BEGIN {print $wins + 0.5}")                     # if draw, 0.5 points for both             
                                        fi
                                fi

                        done < tmp_history.csv

                if [[ "$losses" -eq 0 ]]; then
                        ratio=9999
                else
                        ratio=$(awk "BEGIN {printf \"%.2f\", $wins/$losses}")
                fi

                echo "$game,$player,$wins,$losses,$ratio" >> tmp.csv              # Store results in tmp.csv
        done< <(get_players "$game")
done < <(get_games)

}

# sorting based on given arguement

sort_by_argument(){
        argument="$1"

        if [[ "$argument" == "wins" ]]; then
                sort -t, -k1,1 -k3,3nr tmp.csv > sorted.csv                      # sort by wins

        elif [[ "$argument" == "losses" ]]; then
                sort -t, -k1,1 -k4,4nr tmp.csv > sorted.csv                      # sort by losses

        elif [[ "$argument" == "ratio" ]]; then
                sort -t, -k1,1 -k5,5nr tmp.csv > sorted.csv                      # sort by win/loss ratio

        fi
}

# printing table based on given arguments

print_table(){

        current_game=""

        while IFS=',' read -r game player wins losses ratio; do
                if [[ "$game" != "$current_game" ]]; then
                        echo -e "\n ========== $game ========== \n"
                        echo -e "\nPlayer\t\tWins\tLosses\tWins/Loss\n"
                        current_game="$game"
                fi

                echo -e "$player\t\t$wins\t$losses\t$ratio"
        done < sorted.csv
}

generate_statistics
sort_by_argument "$1"        # argument : w or l or w/l
print_table

rm -f tmp* sorted.csv        # clean up temporary files
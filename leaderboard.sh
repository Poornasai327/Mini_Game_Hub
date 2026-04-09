#!/bin/bash

touch tmp.csv sorted.csv

get_games(){
        cut -d "," -f 4 history.csv | tail -n +2 | sort | uniq
}

get_players(){
        grep ",$1$" history.csv | awk -F, '{print $1"\n"$2}' |sort | uniq
}

statistics(){

        tail -n +2 history.csv > tmp_history.csv

        wins=0
        losses=0

        while IFS=',' read -r winner loser date game; do

                if [[ "$game" != $1 ]]; then
                        continue
                fi
                if [[ "$winner" == "$2" ]];then
                        wins++
                elif [[ "$loser" == "$2" ]]; then
                        losses++
                fi
        done < tmp_history.csv
}

ratio(){
        ratio=$(awk "BEGIN {printf \"%.2f\", $wins/$losses}")
}

generate_statistics(){

        for game in $(get_games); do
                for player in $(get_players "$game"); do
                        statistics "$game" "$player"
                        ratio

                        echo "$game,$player,$wins,$losses,$ratio" >> tmp.csv
                done
        done
}

sort_by_argument(){
        argument="$1"

        while IFS=',' read -r game player wins losses ratio;
        do
                if [[ "$argument" == "wins" ]]; then
                        sort -t, -k1,1 -k3,3nr tmp.csv > sorted.csv

                elif [[ "$argument" == "losses" ]]; then
                        sort -t, -k1,1 -k4,4nr tmp.csv > sorted.csv

                elif [[ "$argument" == "ratio" ]]; then
                        sort -t, -k1,1 -k5,5nr tmp.csv > sorted.csv

                fi
        done < tmp.csv
}

print_table(){

        current_game=""

        while IFS=',' read -r game player wins losses ratio;
        do
                if [[ "$game" != "$current_game" ]]; then
                        echo -e "\n ### $game ### \n"
                        echo "Player" "Wins" "Losses" "w/l ratio"
                        echo
                        current_game="$game"
                fi

                echo "$player" "$wins" "$losses" "$ratio"
        done < sorted.csv
}

statistics
sort_by_argument
print_table

rm tmp_history.csv tmp.csv sorted.csv
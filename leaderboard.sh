#!/bin/bash

touch tmp.csv sorted.csv

get_games(){
        cut -d "," -f 4 history.csv | tail -n +2 | sort | uniq
}

get_players(){
        awk -F, -v game="$1" '
        $4==game {
        print $1
        print $2
        }' history.csv | sort | uniq
}

generate_statistics(){

        tail -n +2 history.csv > tmp_history.csv

        while read -r game; do
                while read -r player; do
                        wins=0
                        losses=0
                        while IFS=',' read -r winner loser date g; do
                                if [[ "$g" != "$game" ]]; then
                                        continue
                                fi

                                if [[ "$winner" == "$player" ]];then
                                        ((wins++))
                                elif [[ "$loser" == "$player" ]]; then
                                        ((losses++))
                                fi

                                if [[ "$losses" -eq 0 ]]; then
                                        ratio="inf"
                                else
                                        ratio=$(awk "BEGIN {printf \"%.2f\", $wins/$losses}")
                                fi

                        done < tmp_history.csv
                echo "$game,$player,$wins,$losses,$ratio" >> tmp.csv
        done< <(get_players "$game")
done < <(get_games)

}

sort_by_argument(){
        argument="$1"

        if [[ "$argument" == "wins" ]]; then
                sort -t, -k1,1 -k3,3nr tmp.csv > sorted.csv

        elif [[ "$argument" == "losses" ]]; then
                sort -t, -k1,1 -k4,4nr tmp.csv > sorted.csv

        elif [[ "$argument" == "ratio" ]]; then
                sort -t, -k1,1 -k5,5r tmp.csv > sorted.csv

        fi
}

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
sort_by_argument "$1"
print_table

rm -f tmp* sorted.csv
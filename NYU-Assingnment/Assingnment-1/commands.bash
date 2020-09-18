sort data_drycanyon_2013.txt -k 3 -n | tail -1 > get_most_common_species.sh

for f in data_*.txt      
do
        echo $f >> all_species_counts.sh
        sort -k 3 -n $f >> all_species_counts.sh
done

# Advanced Python for Data Science Assignment 1
### Do the following using the Linux/Mac shell or GitBash on Windows:


1. We have data on bird communities that we’ve collected that we need to analyze. The data has three columns, a date, a common name, and a count of the number of individuals.

		2013-03-22 bluejay 5
		2013-03-22 mallard 9
		2013-03-21 robin 1

	Download one of these files using the curl command:

	`curl -O https://nyu-cds.github.io/courses/data/data_drycanyon_2013.txt`

	If we wanted to find the least common species in the data file and store that information we could do something like:

	sort data_drycanyon_2013.txt -k 3 -n > sorted_counts.txt
	head -1 sorted_counts.txt > least_common_species.txt

	Now we want to get the most common species at the site. You can do this using the `tail` command. Since we don’t need the intermediate `sorted_counts.txt` file, use a pipe instead of creating the intermediate file.

	Save both the curl command and the one line command for storing the most common species in a text file called `get_most_common_species.sh`.

2. We have data on bird communities that we’ve collected that we need to analyze. The data has three columns, a date, a common name, and a count of the number of individuals.

	2013-03-22 bluejay 5
	2013-03-22 mallard 9
	2013-03-21 robin 1

	Download the data files using the curl command:

		curl -O https://nyu-cds.github.io/courses/data/data_drycanyon_2013.txt
		curl -O https://nyu-cds.github.io/courses/data/data_greencanyon_2013.txt
		curl -O https://nyu-cds.github.io/courses/data/data_logancanyon_2013.txt
	We want to count the total number of individuals of each species that were seen in each data file. We could solve this problem ourselves, but our lab mate has already written some code that does this. Instead of rewriting the code ourselves we can simply add it to a pipeline. Let’s go ahead and download the file:

		curl -O https://nyu-cds.github.io/courses/code/species_counts.py

	To run this code we need to tell the shell to run it using python, which we do by giving it the name of the program that will run it, then the name of our program, and then the input.

		python species_counts.py data_greencanyon_2013.txt

	This can then be integrated into our pipeline. So if we want to sort based on the total number of individuals:

		python species_counts.py data_greencanyon_2013.txt | sort -k 2 -n

	This is great for a single datafile with a particular name, but we’ve been collecting data on birds from a number of different places and we’d like to conduct all of these analyses simultaneously. Write a simple for loop that loops over all of the files in the current directory that have the general form of `data_*.txt`, prints out the name of the datafile, and then runs `species_counts.py` on the datafile. Save this in a text file `called all_species_counts.sh`.

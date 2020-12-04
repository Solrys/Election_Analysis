# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save file to a path
saved_file = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and votes list
candidate_options = []
candidate_votes = {}

# Listed Counties and votes 
counties_list = []
counties_votes = {}

# tracking winning candidate, vote count and percentage.
winnig_candidate = " "
winning_count = 0
winning_percentage = 0

# tracking largest county for challenge
largest_turnout = " "
largest_county_votes = 0

# Open the elecion results to let the file to be read in order to find results
with open(file_to_load) as clrd_election_data:

    # read the file object with csv.reader functions
    file_reader = csv.reader(clrd_election_data)
    print(file_reader)

    # read the header row and skip it
    headers = next(file_reader)

    # using loops to iterate each row to count total votes, unique names, and unique count in the csv file
    for row in file_reader:
        # adds the total vote count
        total_votes += 1

        # evaluates candidates from correct coloumn
        candidate_name = row[2]

        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            
            # adds the name to the list of candidates
            candidate_options.append(candidate_name)

            # setting each unique vote count to zero for each candidate
            candidate_votes[candidate_name] = 0

        # adding vote to a unique candidate by increments
        candidate_votes[candidate_name] += 1

        #evalutaes county name from correct coloumn
        county_name = row[1]

        #if county does not match existing county
        if county_name not in counties_list:

            # adds county name to the list
            counties_list.append(county_name)

            # setting each county count to zero
            counties_votes[county_name] = 0
        
        # adding vote to a unique county by increments
        counties_votes[county_name] += 1

# use open function to write data with 'w' on file and save results
with open(saved_file, "w") as textcomp_file:
    
    #print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"{'-'*40}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{'-'*40}\n"
        f"\nCounty Votes: \n")
    print(election_results)
    
    # saving the printed results in the text file.
    textcomp_file.write(election_results)

    #iterating through county list to count votes
    for counties in counties_votes:

        # retrieve vote count of county
        cvotes = counties_votes[counties]

        # calculating percentage for each county
        county_percentage = float(cvotes)/ float(total_votes) * 100
        
        #Print the county name, vote count and percentage of votes in terminal.
        county_results = (
            f"{counties}: {county_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)
        
        textcomp_file.write(county_results)    

        # finding the largest county turnout and print the result
        if (cvotes > largest_county_votes):

            largest_county_votes = cvotes

            largest_turnout = counties
    
    #printing and writing the results.
    largest_county_votes =(
        f"\n{'-'*40}\n"
        f"Largest County Turnout: {largest_turnout}"
        f"\n{'-'*40}\n")
    print(largest_county_votes)
    
    textcomp_file.write(largest_county_votes)
    
    #adding a little spacing and candidate title before tabulating candidate data
    spacing =(
        f"\nCandidate Votes: \n")
    print(spacing)
    
    textcomp_file.write(spacing)

    # Iterate through the candidate list.
    for candidate in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name, vote count and percentage of votes in terminal.
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        textcomp_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate by checking if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # if true, then will set them equal to each other
            winning_count = votes

            winning_candidate = candidate
            
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"\n{'-'*40}\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{'-'*40}\n")
    print(winning_candidate_summary)

    textcomp_file.write(winning_candidate_summary)
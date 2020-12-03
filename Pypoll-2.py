# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes for each canditate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. path to election_results.csv
    # Resources/election_results.csv

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join ("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# 2. Declare Candidate list.
candidate_options = []
# Declare candidate votes received.
candidate_votes = {}
# declare winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the toal vote count.
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]
        # Add if statement to only add candidates who aren't in list.
        
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)    
            # track candidate votes
            candidate_votes[candidate_name] = 0
        # add a vote to the candidate count.
        candidate_votes[candidate_name] += 1
        
# Save results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the candidate name and % of votes.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------------\n")
    print(election_results, end="")    
    # Save the final vote count to the text file.
    txt_file.write(election_results)            
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
    
        #print each candidates voter count and % to terminal
        print(candidate_results)
        #save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            #if true then set winning count = votes and winning_percentage = 
            #vote_percentage.
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name

    #Print out the winning candidate to the terminal.
    winning_candidate_summary = (
        f"-----------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------\n")
    print (winning_candidate_summary)
    #save to text file.
    txt_file.write(winning_candidate_summary)
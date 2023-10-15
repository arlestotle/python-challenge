# Import Dependencies
import os
import csv
import shutil
from pathlib import Path 

# Read in the CSV
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Open csv
with open(election_csv, newline="", encoding="utf-8") as election:
    electioncsv = csv.reader(election, delimiter = ",")
    next(electioncsv)
    # Find the total number of cast votes

    votes = list(electioncsv)
    count_votes = len(votes)
    count_votes

    # Use the Candidate column of election_data.csv to make a new list of candidates in the poll
    list_candidates = list()
    counter = list()
    for i in range (0, count_votes):
        candi = votes[i][2]
        counter.append(candi)
        if candi not in list_candidates:
            list_candidates.append(candi)
    count_candi_votes = len(list_candidates)
    count_candi_votes

    # Find the total number of votes each candidate recieved and their over all voter percents
    total_votes = list()
    vote_percent = list()
    for j in range (0, count_candi_votes):
        name_candidate = list_candidates[j]
        total_votes.append(counter.count(name_candidate))
        percentofvotes = total_votes[j]/count_votes
        vote_percent.append(percentofvotes)

    # View the total nymber of votes each candidate recieved 
     # A complete list of candidates who revieved votes
        list_candidates
     # The total number of votes each candidate recieved
        total_votes
     # The percentage of votes each candidate won
        vote_percent
     # The winner of the election based on popular vote
        winner_of_election = total_votes.index(max(total_votes))   
        list_candidates[winner_of_election]


# Create print statements to match output
print("Election Results")
print("---------------------")
print(f"Total Votes: {count_votes}")
print("---------------------")
for k in range (0, count_candi_votes):
    print(f"{list_candidates[k]}: {vote_percent[k]:.3%} ({total_votes[k]:,}")
print("---------------------")
print(f"Winner: {list_candidates[winner_of_election]}")
print("---------------------")


# Create new text file for summary output
election_results = open("election_results.txt","w")

election_results.write("Election Results" + "\n")
election_results.write("-----------------------------" + "\n")
election_results.write(f"Total Votes: {count_votes}" + "\n")
election_results.write("-----------------------------" + "\n")

for k in range (0, count_candi_votes):
    election_results.write(f"{list_candidates[k]}: {vote_percent[k]:.3%} ({total_votes[k]:,}" + "\n")

election_results.write("-----------------------------" + "\n")
election_results.write(f"Winner: {list_candidates[winner_of_election]}" + "\n")
election_results.write("-----------------------------" + "\n")
                       
election_results.close()

    

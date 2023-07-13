
#Imports modules csv and os
import csv
import os

#Sets the path for the CSV file with polling data
POLL_CSV_PATH = os.path.join("Resources", "election_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Gets data file
with open(POLL_CSV_PATH) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

#Sets variables total votes and winning votes to 0 for counting
    total_votes = 0
    winning_votes = 0
    winner = ""

#Creates blank dictionary for candidate votes and empty lists for unique candidates and for their total vote counts
    candidate_votes = {}
    candidates = []
    unique_candidate = []

    for row in csvreader:
    #count the total votes for all candidates
    #only count votes for candidates receiving votes >0
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1
    
    #print out the total vote count
    print(f"Election Results")
    print("---------------------")
    print(f"Total votes: {total_votes}")
    print("---------------------")

    #for each candidate, calculate their vote as a percent of the overall vote total
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent_votes = float(votes)/float(total_votes)*100
        
    #for each candidate, print out their name, % of overall votes received, and their vote total
        print(f"{candidate} {percent_votes:0.3f}% ({votes})")

    #winnining candidate is determined based on having highest vote count
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate
            
    #print out the winner      
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")

    #Outputs results to txt file
    output = os.path.join(".", 'output.text')
    with open(output, "w") as new:
        new.write("Election Results")
        new.write("\n")
        new.write("---------------------")
        new.write("\n")
        new.write(f"Total votes: {total_votes}")
        new.write("\n")
        new.write("---------------------")
        for candidate in candidates:
            index = candidates.index(candidate)
            new.write(f"{candidate} {percent_votes:0.3f}% ({votes})\n")
        new.write("\n")
        new.write("---------------------")
        new.write(f"Winner: {winner}")
        new.write("---------------------")
    
    #Prints file to terminal
    with open(output, 'r') as readfile:
        print(readfile.read())





    
    


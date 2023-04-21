

import os 
import csv

csvpath = os.path.join('..', 'Resources','election_data.csv')

with open(csvpath) as csvfile:
	csvreader =csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
	
	#print(csv_header)

	candidate_id_count = {}
	
	ID_count = 0
	candidates =[]
#loop through each row in the CSV file

	for row in csvreader:
		ID_count += 1
		candidate_name = row[2]
		if candidate_name not in candidates: 
			candidates.append(candidate_name)
		if candidate_name in candidate_id_count:
			candidate_id_count[candidate_name] += 1
		else: 
			candidate_id_count[candidate_name] = 1

print(f'total votes is {ID_count}') 
for candidate_name in candidates:
		
	print(f'A complete list of candidates who received votes: {candidate_name}')

print(candidate_id_count)


greatest_count = max(candidate_id_count.values())

#loop through each candidate and their vote counts

for candidate_name, count in candidate_id_count.items():
	vote_percentage = round((count/ID_count) *100,3)
	print (f'{candidate_name} : {vote_percentage}%' )

#check the candidate's votes if more than the current highest vote candidate
for candidates, count in candidate_id_count.items():
	if count == greatest_count:
		print(f'the winner :{candidates}')

# write the results to a text file

file_to_output = os.path.join("..","analysis", "poll_analysis.txt")
with open(file_to_output, "w") as txt_file:

	txt_file.write(f"total votes is {ID_count}'\n")


	for candidate_name, count in candidate_id_count.items():
		vote_percentage = round((count/ID_count) *100,3)   
		txt_file.write(f"{candidate_name} : {vote_percentage}%\n")

	for candidate, count in candidate_id_count.items():
		if count == greatest_count:
			txt_file.write(f"Winner: {candidate}\n")






    

#print(charles_count)
	



	
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------


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


for candidate_name, count in candidate_id_count.items():
	vote_percentage = round((count/ID_count) *100,3)
	print (f'{candidate_name} : {vote_percentage}%' )

for candidates, count in candidate_id_count.items():
	if count == greatest_count:
		print(f'the winner :{candidates}')











    

#print(charles_count)
	



	
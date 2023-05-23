import requests
import json
import random


def random_vote_percentages_generator(parties):
    overall_percentage = 100
    vote_percentages = {}

    for party in parties[:-1]:
        percentage_rand = random.randint(0, overall_percentage)
        vote_percentages[party] = percentage_rand
        overall_percentage = overall_percentage - percentage_rand

    vote_percentages[parties[-1]] = overall_percentage

    return vote_percentages


#Main function 
if __name__ == "__main__":

    res = requests.get('http://127.0.0.1:5000/election/parties')
    print("Initial Party List: ", res.text, end= "\n\n") # Print part list

    # Put party's list into database. 
    # Add ”Party1”, ”Party2”, ”Party3” and ”Party4” to the list successively
    for i in range(1,5):
        data = {
        'party_name':f'Party{i}'
        }
        res = requests.put('http://127.0.0.1:5000/election/parties', json=data)
        print(f"Status Code after Party{i} Addition to database: ", res.status_code) # Check that party was added successfully or show the error message 
        print(f"Response Message after Party{i} Addition to database: ", res.text, end="\n\n") # Show message of the response object


    # Addiyion of Part1, Part2, Part3, Part4
    res = requests.get('http://127.0.0.1:5000/election/parties')
    print("List of Parties after Adding 4 Parties: ", end="")
    json_response = json.loads(res.content.decode("utf-8"))

    for message in json_response:
        if message != json_response[-1]:
            print(message["party_name"], end=", ")
        else:
            print(message["party_name"], end="\n\n")


    # Re-Addition of Party4
    data = {
        'party_name':'Party4'
        }

    res = requests.put('http://127.0.0.1:5000/election/parties', json=data)
    json_response = json.loads(res.content.decode("utf-8"))
    print(f"Status Code after Re-Addition of Party4 to database: ", res.status_code) # Check that party was added successfully or show the error message 
    print(f"Response Message after Re-Addition of Party4 to database: ", json_response["message"], end="\n\n") # Show message of the response object


    # Deletion of Party4
    data = {
        'party_name':'Party4'
        }
    res = requests.delete('http://127.0.0.1:5000/election/parties', json=data)
    print("Status Code after Deletion of Party4 from database: ", res.status_code) # Check that party was added successfully or show the error message 
    print("Response Message after Deletion of Party4 from database: ", res.text, end="\n\n") # Show message of the response object


    # Show remaining parties
    res = requests.get('http://127.0.0.1:5000/election/parties')
    print("List of Parties after Deletion of Party4: ", end="")
    json_response = json.loads(res.content.decode("utf-8"))

    for message in json_response:
        if message != json_response[-1]:
            print(message["party_name"], end=", ")
        else:
            print(message["party_name"], end="\n\n\n")


    # Request remaining parties
    res = requests.get('http://127.0.0.1:5000/election/parties')
    parties = json.loads(res.content.decode("utf-8"))
    parties = [i["party_name"] for i in parties] # ['Party1', 'Party2', 'Party3']


    # Request remaining parties
    res = requests.get('http://127.0.0.1:5000/election/regions')
    regions = json.loads(res.content.decode("utf-8"))
    random_region = random.sample(regions, 3)

    for i in range(len(random_region)):

        # Generate random percentages for parties
        parties_and_votes = random_vote_percentages_generator(parties) 
        # Generate random vote percentages for each region
        print(parties_and_votes)

        random_region_name = random_region[i]["region_name"]

        data = {
            "region" : random_region_name,
        }

        # Updates and extends dictionary object with another dictionary object
        data.update(parties_and_votes)
        # Post parties, region and i
        res = requests.post('http://127.0.0.1:5000/election/simulate', json=data)
        print(f'Region: {random_region[i]["region_name"]}, Total Seat Num: {random_region[i]["seats"]}')
        print(f"MP distribution: {res.text}")
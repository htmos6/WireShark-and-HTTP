# WireShark-and-HTTP

###  HTTP Requests with Python

* We will implement a simple HTTP client using Python and
talk with the provided server written with Flask. The server runs a simple D’Hondt-style
election simulator with region and seat information for an example-country election. It has
2 APIs, one for adding/deleting parties for the election and another for running the D’Hondt
simulation with party votes provided by the client.

### 1- Getting the Server Up and Running

* In order to use the provided server, you need to install Flask, which is a Python library that
handles HTTP requests. You can install it by running:

```pip install -r requirements.txt```

* Or you can install Flask and requests manually using pip install.
After extracting the given server code, head into the folder and run:

```flask --app election init-db```

* This resets the SQL database, it is sufficient to run this only once but if you want to
clear the database you can run it again.

```flask --app election run```

* This will start your server at the stated address (by default, 127.0.0.1:5000).

### 2- Connecting to the Server

* In another Python file, we are going to write a client code in order to connect and pull the
required information. We are going to use the requests library. We can check the supplied
example code for a simple fetch of the regions. In order to fully complete this project,
please read the documentation on the request library.

### 2.1- Server APIs

* ```/election/regions```: Returns a list of dictionaries that contains region information.
* ```/election/parties```: Has 3 methods (’GET’, ’PUT’, ’DELETE’).

  - ```GET```: Returns a list of dictionaries where keys are all ”party name” and values
are party names such as ”party A” or whatever you ```PUT```.
  - ```PUT```: Adds a new party to the database in the body you should send a JSON
which contains a single entry dictionary like {”party name”: ”party A”}
  – ```DELETE```: Deletes a party, requires the same JSON file format as ```PUT```.

* ```/election/simulate```: Has one method ```:PUSH``` that calculates the D’Hondt algorithm.
Requires a dictionary with a key ”region” that has a valid region name and multiple
keys for parties that contains the percentages.

(e.g. { ”region”: ”Region1”, ”Party1”: 50, ”Party2”: 50 })

### Client

* In our client code, following operations completed:  
  • Pull the list of the parties that are currently in the list.  
  • Print the party list on the console (at this stage, it should be empty).      
  • Add ”Party1”, ”Party2”, ”Party3” and ”Party4” to the list by using ```POST``` method.  
  • Print the list of the parties by re-fetching the data.  
  • Try to re-add ”Party4” and print the error message and status code.  
  • Delete ”Party4” from the party list.  
  • Print the remaining parties.
  
After we set up the party list, we are going to run the D’Hondt simulation for three
different provinces with the vote percentages of our choice. Regions are going to be selected
by a random number generator in our code after fetching the region list. Prints the resulting
MP distribution.













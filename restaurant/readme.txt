Table reservation system
In this exercise you are going to create a table  reservation system for restaurants. You are going to create at least 2 classes - Table and TableReservationSystem.

Your system should serve hostesses in a restaurant and should store and provide information about the current state of all the tables in the restaurant.

In general, your system should be able to provide the following functionality:
•	Check whether there are available tables and which ones are available (new guests have arrived at a restaurant and the hostess needs to seat them down). Return all the available tables with enough seats for the group of guests that has just arrived. Consider sorting the returned available tables by the number of seats, such that the hostess will be able to choose the available table with the minimum number of seats.
•	Reserve a table (guests has arrived to a restaurant and were seated at a table)
•	Release a table (guests has left the restaurant, hence left the table)
•	Allow restaurant setting maximum time limit for  guests to occupy the table 
    (for example, maximum of 1h 30min)
•	If there are no available tables, get a table that will be available in the shortest 
    amount of time. Don’t forget that you should take into account the number of guests 
    that should be seated!

Table
This class stores information about a single table in a restaurant and provides 
actions relevant to a single table.

Data:
•	Table ID
•	Seats number
•	Is occupied
•	Occupied seats (if occupied)
•	Reservation start time
•	Table location in the restaurant:
o	Bar
o	Terrace
o	Indoors
o	Floor number (if relevant)
o	VIP room (if relevant)
o	Is located at less preferred place:
	Near toilet
	Near exit
	Near kitchen

Methods:
•	The class should be initialized with the number of seats
•	is_available()
•	reserve_a_table() - given number of guests, seat them down at the table
•	release_a_table() - the guests have finished their meal, release the table for the next ones
•	time_left() - in case the table is occupied, get amount of time left for the 
    guest to dine (return timedelta)
•	get_available_hour() - in case the table is occupied, get the exact time (datetime) 
     the table will become available


TableReservationSystem
This class should store information about all the tables in the restaurant, including the current state of all the tables, and should provide actions that will serve the hostess in her job.
Data:
•	Collection of the tables in the restaurant (collection of Table objects)
•	Restaurant name
•	Max time limit to occupy a table

Methods:
•	get_available_tables  - return available tables for the given number of guests, sorted by amount of seats, ascending
•	get_soonest_available_tables - return tables that will be available soon for the given number of guests, sorted by time from the soonest to latest + amount of seats ascending
•	reserve a table - given a table id, reserve the table starting from now
•	release a table - given a table id, release the table starting from now
•	get_tables_with_less_than_x_minutes_left - given a seats number, and amount of minutes, return all the tables that will be available for the provided seats number in the upcoming X minutes
•	get_tables_time_limit
•	update_tables_time_limit

Advanced:
1.	Add an option to reserve tables in advance for a specific amount of guests and for a specified date and time.
2.	Make sure to take these reservations into account when making new reservations or seating guests.
3.	Think about additional fields that should be stored for each table to allow multiple reservations for a single table
4.	Provide a user interface (command-line interface) that will allow hostess to interact with your system.




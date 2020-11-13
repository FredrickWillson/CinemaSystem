from time import sleep
from os import system
from json import dump, load
from datetime import datetime
import random
import string

def print_menu():
	print_header("CINEMA OPERATOR")
	for menu in menu_list:
		print(menu)

def print_header(msg):
	system("cls")
	print(msg+"\n")

def process_input(char):
	if char == "q":
		print ("shutting down...")
		sleep(1)
		system('cls')
		return True
	elif char == "1":
		add_new_booking()
	elif char == "2":
		find_booking()
	elif char == "3":
		see_all_booking()
	elif char == "4":
		change_booking()
	elif char == "5":
		cancel_booking()

def add_new_booking():
	print_header("ADD NEW BOOKING")
	room = input("Room\t: ")
	time = input("Time\t: ")
	film = input("Film\t: ").upper()
	price = input("Price\t: ")
	seat = input("Seat\t: ").upper()
	code = generate_code()
	ID = generate_id(code)
	booking_data[ID] = {"code": code, "room": room, "time": time, "film": film, "price": price, "seat": seat}
	if save_data():
		input(f"\nBOOKING SUCCESSFULLY ADDED\nYOUR CODE FOR THIS BOOKING IS {code}\n\nPress ENTER to go back to MENU")
	else:
		input("\nTHERE IS AN ERROR IN THE SAVING PROCESS\n\nPress ENTER to go back to MENU")

def see_all_booking():
	print_header("LIST OF BOOKING(S)")
	if len(booking_data) != 0:
			print_booking(print_all=True)
	else:
		print("NO BOOKING AVAILABLE\n")
	input("\nPress ENTER to go back to MENU.")

def searching(search_type, searched_code=None, searched_room=None, searched_time=None, searched_seat=None):
	if search_type == "room time seat":
		searched_dict = {"room" : searched_room, "time" : searched_time, "seat" : searched_seat}
		for booking in booking_data:
			if {booking_data[booking]["room"]} == {searched_dict["room"]} and {booking_data[booking]["time"]} == {searched_dict["time"]} and {booking_data[booking]["seat"]} == {searched_dict["seat"]}:
				return booking
	elif search_type == "code":
		searched_dict = {"code" : searched_code}
		for booking in booking_data:
			if {booking_data[booking]["code"]} == {searched_dict["code"]}:
				return booking
	print("DATA NOT FOUND!")
	return "no data"

def find_booking():
	print_header("FIND BOOOKING")
	searched_room = input("Room: ")
	searched_time = input("Time: ")
	searched_seat = input("Seat: ").upper()
	booking = searching(search_type="room time seat", searched_room=searched_room, searched_time=searched_time, searched_seat=searched_seat)
	if booking != "no data":
		print("\nBOOKING DATA FOUND!\n")
		print_booking(booking=booking)
		input("\nPRESS ENTER TO CONTINUE.")
	else:
		input("PRESS ENTER TO CONTINUE.")

def cancel_booking():
	print_header("CANCEL BOOKING")
	searched_code = input("Code: ").upper()
	booking = searching(search_type="code", searched_code=searched_code)
	if booking != "no data":
		print("\nARE YOU SURE YOU WANT TO CANCEL THIS BOOKING?\n")
		print_booking(booking=booking)
		if question():
			del booking_data[booking]
			input("\nBOOKING HAS BEEN CANCELED. PRESS ENTER TO CONTINUE.")
		else:
			print("\nCANCELATION HAS BEEN CANCELED. PRESS ENTER TO CONTINUE.")
	else:
		input("PRESS ENTER TO CONTINUE")
	save_data()

def change_booking():
	print_header("CANCEL BOOKING")
	searched_code = input("Code: ").upper()
	booking = searching(search_type="code", searched_code=searched_code)
	if booking != "no data":
		print_booking(booking=booking)
		print("\nEDIT BOOKING\n[1] Room\n[2] Time\n[3] Film\n[4] Price\n[5] Seat")
		respond = input("\nINPUT: ")
		update_data(booking, respond)
		save_data()
	else:
		input("PRESS ENTER TO CONTINUE")

def update_data(booking):
	if respond == "1":
		new_data = input("\nNEW ROOM: ")
		print(f"\nARE YOU SURE YOU WANT TO CHANGE THE ROOM FROM ROOM {booking_data[booking]['room']} TO ROOM {new_data}?")
		if question():
			del booking_data[booking]["room"]
			booking_data[booking] = {"room": new_data}
			input("\nPRESS ENTER TO CONTINUE.")
		else:
			print("\nUPDATE CANCELED. PRESS ENTER TO CONTINUE.")
	elif respond == "2":
		new_data = input("\nNEW TIME: ")
		print(f"\nARE YOU SURE YOU WANT TO CHANGE THE TIME FROM {booking_data[booking]['time']} TO {new_data}?")
		if question():
			del booking_data[booking]["time"]
			booking_data[booking] = {"time": new_data}
			input("\nPRESS ENTER TO CONTINUE.")
		else:
			print("\nUPDATE CANCELED. PRESS ENTER TO CONTINUE.")
	elif respond == "3":
		new_data = input("\nNEW FILM: ")
		print(f"\nARE YOU SURE YOU WANT TO CHANGE THE FILM FROM {booking_data[booking]['film']} TO {new_data}?")
		if question():
			del booking_data[booking]["film"]
			booking_data[booking] = {"film": new_data}
			input("\nPRESS ENTER TO CONTINUE.")
		else:
			print("\nUPDATE CANCELED. PRESS ENTER TO CONTINUE.")
	elif respond == "4":
		new_data = input("\nNEW PRICE: ")
		print(f"\nARE YOU SURE YOU WANT TO CHANGE THE PRICE FROM {booking_data[booking]['price']} TO {new_data}?")
		if question():
			del booking_data[booking]["price"]
			booking_data[booking] = {"price": new_data}
			input("\nPRESS ENTER TO CONTINUE.")
		else:
			print("\nUPDATE CANCELED. PRESS ENTER TO CONTINUE.")
	elif respond == "5":
		new_data = input("\nNEW SEAT: ")
		print(f"\nARE YOU SURE YOU WANT TO CHANGE THE SEAT FROM {booking_data[booking]['seat']} TO {new_data}?")
		if question():
			del booking_data[booking]["seat"]
			booking_data[booking] = {"seat": new_data}
			input("\nPRESS ENTER TO CONTINUE.")
		else:
			print("\nUPDATE CANCELED. PRESS ENTER TO CONTINUE.")

def print_booking(booking=None, print_all=False):
	if not print_all:
		print(f"### {booking}")
		print(f'Code\t: {booking_data[booking]["code"]}')
		print(f'Room\t: {booking_data[booking]["room"]}')
		print(f'Time\t: {booking_data[booking]["time"]}')
		print(f'Film\t: {booking_data[booking]["film"]}')
		print(f'Price\t: {booking_data[booking]["price"]}')
		print(f'Seat\t: {booking_data[booking]["seat"]}')
	elif print_all:
		for booking in booking_data:
			print(f"### {booking}")
			print(f'Code\t: {booking_data[booking]["code"]}')
			print(f'Room\t: {booking_data[booking]["room"]}')
			print(f'Time\t: {booking_data[booking]["time"]}')
			print(f'Film\t: {booking_data[booking]["film"]}')
			print(f'Price\t: {booking_data[booking]["price"]}')
			print(f'Seat\t: {booking_data[booking]["seat"]}\n')

def generate_id(code):
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	counter = len(booking_data) + 1
	generated_id = ("%04d-%04d%02d%02d-%s" % (counter, year, month, day, code))
	return generated_id

def generate_code():
	generated_code = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
	return generated_code

def question():
	answer = input("\nYES [Y]/ NO [N]\n").lower()
	if answer == "y":
		return True
	elif answer == "f":
		return False

def load_data():
	with open(file_path, "r") as file:
		data = load(file)
	return data

def save_data():
	with open(file_path, "w") as file:
		dump(booking_data, file)
	return True

menu_list = [
	"[1] New Booking",
	"[2] Find Booking",
	"[3] See All Booking",
	"[4] Change Booking",
	"[5] Cancel Booking",
	"[Q] Quit"]

file_path = "booking_data.json"
ongoing = False
booking_data = []
booking_data = load_data()

while not ongoing:
		print_menu()
		user_input = input("\nChoice : ").lower()
		ongoing = process_input(user_input)
import pandas as pd
from util import cateringItem,booking,room

def main():
	inp = 1
	df = pd.DataFrame()
	del df
	while inp != 0:
		print("Welcome")

		inp=input("1. Room\n2. Item\n3. Booking\n4. Bill\n0. Exit\n>> ")
		if inp==1:
			in2=input("1. View Rooms\n2. Edit Rooms\n>> ")
			r1=room.Room()
		elif inp==2:
			in2=input("1. View Items\n2. Edit Items\n>> ")
		elif inp==3:
			in2=input("1. View Bookings\n2. Edit Bookings\n>> ")
		elif inp==4:
			in2=input("1. View Bills\n2. Edit Bills\n>> ")
		elif inp==0:
			break
		else:
			print("Enter correct option\n>> ")

if __name__ == '__main__':
	main()

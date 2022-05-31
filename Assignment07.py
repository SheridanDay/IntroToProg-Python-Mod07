# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickle data
#              Create and handle exception errors
# ChangeLog (Who,When,What):
# # Sheridan Day,05.30.2022,Started and completed script
# ---------------------------------------------------------------------------- #

import pickle, shelve

print("I have pickled the Star Wars Trilogies!")
OT = ["ANH", "ESB", "ROTJ"]
PT = ["TPM", "AOTC", "ROTS"]
ST = ["TFA", "TLJ", "ROS"]
f = open("SWTrilogies.dat", "wb")
pickle.dump(OT, f)
pickle.dump(PT, f)
pickle.dump(ST, f)
f.close()

s = shelve.open("SWTrilogy.dat")
s["OT"] = ["ANH", "ESB", "ROTJ"]
s["PT"] = ["TPM", "AOTC", "ROTS"]
s["ST"] = ["TFA", "TLJ", "ROS"]
s.sync()

print("\nThe Star Wars Trilogies, unpickled:")
f = open("SWTrilogies.dat", "rb")
OT = pickle.load(f)
PT = pickle.load(f)
ST = pickle.load(f)
print("Original Trilogy: ", s["OT"])
print("Prequel Trilogy: ", s["PT"])
print("Sequel Trilogy: ", s["ST"])
f.close()


print("\n\nHere is a question for you: ")
print("""
The Star Wars franchise has three trilogy movie series.
1 - The Original Trilogy (OT) consists of A New Home (ANH), The Empire Strikes Back (ESB), and The Return of the Jedi (ROTJ).
2 - The Prequel Trilogy (PT) consists of The Phantom Menace (TPM), Attack of the Clones (AOTC), and Revenge of the Sith (ROTS).
3 - The Sequel Trilogy (ST) consists of The Force Awakens (TFA), The Last Jedi (TLJ), and The Return of Skywalker (TROS).
""")

while True:
	try:
		movie = int(input("Which Star Wars trilogy is the highest rated amongst online rating aggregators? (Please choose 1-3 from above): "))
		if movie == 1:
			print("That is correct! The Original Trilogy is still the highest-rated trilogy of the Star Wars franchise.")
			break
		elif movie > 3:
				print("Please choose 1, 2, or 3!")
		else:
			print("That is not correct. Please try again!")
			continue
	except ValueError:
		print("That was not a number. Please try again.")
		continue

input("Press enter to exit. Thanks!")
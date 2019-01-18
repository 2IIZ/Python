import pickle

score = {
	"Player 1": 8,
	"Player 2": 2222,
	"Player 3": 7,
	"Player 4": 3,
}

with open('data', 'wb') as file: # open file 'data' in binary writing
	# pickle
	my_pickle = pickle.Pickler(file)
	my_pickle.dump(score) # save the score into the file

with open('data', 'rb') as file:
	# and now unpickle
	my_pickle = pickle.Unpickler(file)
	print(my_pickle.load())

import quiz_data

def new_game():
	current_score= 0
	for i,v in enumerate(questions.keys()):
		print(f"  {i+1}.{v} ")
		for n in options[i]:
			print(f"  {n}")
		while True:
			guess = input(" Enter (A,B,C or D):	").upper()
			letters = ["A","B","C","D"]
			if guess in letters:
				current_score+=check_ans(guess, questions.get(v))
				break
			else:
					print("	Invalid option❗")
	print(f" \n\n 	YOUR FINAL SCORE IS: {current_score/len(questions)*100}%")
					
		

def check_ans(guess,answer):
	if guess == answer:
		print("	CORRECT✅")
		return 1
	else:
		print("	WRONG ❌")
		return 0
		
 

questions = quiz_data.questions()
options= quiz_data.options()
new_game()

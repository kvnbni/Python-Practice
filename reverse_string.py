# This program is to reverse a string using two functions first_word and second_word and using recursive calls in the third function.



input_string=raw_input('Enter string:') 
length= len(input_string)



#Function to give the first word of the string
def first_word(text):
	word=''
	for letter in text:
		if letter!=' ':
			word+=letter
		else:
			break
	return word

#Function to give the rest of the string
def second_word(text):
	word=''
	i=0
	for letter in text:
		i=i+1
		if letter==' ':
			start_position=i
			break
	second_word_updated=text[start_position:length]
	return second_word_updated


#Function to return the reverse of the string
def reverse_string(phrase):
	word_count=0
	for l in phrase:
		if l == ' ':
			word_count+=1
	first = ''
	second = ''
	
	first=first_word(phrase)
	if word_count!=0:
		second=second_word(phrase)
	
	if word_count==0:   # Base case for the recursive call
		return first
	else:
		return reverse_string(second) + " " + first  #B
		



print reverse_string(input_string)  #A

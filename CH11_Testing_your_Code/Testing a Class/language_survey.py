from survey import AnonymousSurvey            # call the class (AnonymousSurvey) from survey file.

# Define a question, and make a survey.        
question = "What language did you first learn to speak?" 
language_survey = AnonymousSurvey(question)   # AnonymousSurvey( ) function is used to create an instance of the class.            

# Show the question, and store responses to the question.
language_survey.show_question()         # show_qiuestion() method is used to show the question.
print("Enter 'q' at any time to quit.\n")

'''while loop is used to run the porgram white all responses are givenuntil the user types q.'''
while True:                           
    response = input("Language:")
   # if response == 'q':
       # break
language_survey.store_response(response) 
'''store_response( ) method is used to store the response to the question 
    which is defined as input( ) function for the language.'''

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()          # show_results() method is used to show the reusults.           


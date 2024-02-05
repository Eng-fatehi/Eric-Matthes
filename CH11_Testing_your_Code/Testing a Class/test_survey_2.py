from survey import AnonymousSurvey
""" Test that a single response is stored properly.  خزنت بشكل صحيح"""
def test_store_single_response():
    question = "What Language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert 'English' in language_survey.responses

""" Test that three individual responses are stored properly.  خزنت بشكل صحيح"""
def test_store_three_response():
    question = "What Language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spnish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
""" Test that a single response is stored properly.  خزنت بشكل صحيح"""
from survey import AnonymousSurvey

def test_store_single_response():
    question = "What Language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert 'English' in language_survey.responses
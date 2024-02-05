
import pytest
from survey import AnonymousSurvey

""" A survey that will be available to all test functions."""
@pytest.fixture             # creat a fixture for the fllowing test functions
def language_survey():
    question = "What language did you first learn to apeak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

""" Test that a single response is stored properly.  خزنت بشكل صحيح"""
def test_store_single_response(language_survey):
    language_survey.store_response("English")
    assert 'English' in language_survey.responses


""" Test that three individual responses are stored properly.  خزنت بشكل صحيح"""
def test_store_three_responses(language_survey):
    responses = ['English', 'Spnish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
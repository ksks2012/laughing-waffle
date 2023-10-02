import time

from control.training import Training

def test_click_training():
    training = Training()
    time.sleep(5)
    training.click_training()


def test_click_training_back():
    training = Training()
    time.sleep(5)
    training.click_training_back()

def test_survey_training_abilities():
    training = Training()
    time.sleep(5)
    training.csurvey_training_abilitieslick_training_back()

if __name__ == "__main__":
    test_click_training()
    test_survey_training_abilities()
    test_click_training_back()

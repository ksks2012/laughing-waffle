from script.minst import MINSTModel

def test_load_model():
    minst_model = MINSTModel()
    minst_model.load_model()
    minst_model.test_model()

if __name__ == "__main__":
    test_load_model()
import unittest
from azure.scoring import score
import os
from timeit import default_timer as timer
import json

class TestScore(unittest.TestCase):

    def test_score(self):
        os.environ["AZUREML_MODEL_DIR"] = "./"

        with open('test/sample-request.json') as json_file:
            json_str = json_file.read()
    
        print("json: "+json_str)
        start = timer()
        score.init()
        end = timer()
        print("init: ",end - start)

        for i in range(2):
            start = timer()
            output = score.run(json.loads(json_str))
            end = timer()
            print("score: ",end - start)
            print(output)
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    

if __name__ == '__main__':
    unittest.main()
import os
import logging
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TFAutoModelWithLMHead
from timeit import default_timer as timer

def init():
    global model
    global tokenizer
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)

    logging.info("init!!!!")
    logging.info("cwd!!!: "+ os.getcwd())    
    # format will be something like "azureml-models/gpt2-model/1/model"
    model_dir = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "gpt2-model")
    
    logging.info("model_dir!!!:" + model_dir)
    #logging.info("dir!!!: ")
    #logging.info(os.listdir(model_dir))
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = TFAutoModelWithLMHead.from_pretrained(model_dir, pad_token_id=tokenizer.eos_token_id)    

def run(raw_data):
    try:
        start = timer()        
        logging.info("request received!")
        prompt = json.loads(raw_data)["data"]
        #print("raw_data!!: "+raw_data)
        #prompt = raw_data["data"]
        logging.info("prompt!!: "+prompt)
        
        #prompt = "Today the weather is really nice and I am planning on "
        inputs = tokenizer.encode(prompt, add_special_tokens=False , return_tensors="tf")
        prompt_length = len(tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))        
        outputs = model.generate(inputs, max_length=30 , do_sample=True, top_p=0.95, top_k=60)        
        generated = prompt + tokenizer.decode(outputs[0])[prompt_length:]
        logging.info("generated!!!: "+generated)
        end = timer()
        #logging.info("execution time(secs): {0}".format(end - start))
                
        return [generated]
    except Exception as e:
        error = str(e)
        return error

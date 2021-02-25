# GPT2 on Azure ML managed Inference

## Step 0: Setup CLI & Azure ML Workspace

Please follow the instructions here for [Install](https://azure.github.io/azureml-v2-preview/_build/html/overview/installation.html) and [setup](https://azure.github.io/azureml-v2-preview/_build/html/overview/setup.html)

## Step 1: Setup project locally
a. Clone this repo
`git clone https://github.com/rsethur/gpt2.git`

b. Clone the gpt2 model from hugging face repo inside a `gpt2-model` directory inside your project folder (created in above step)
`git clone https://huggingface.co/gpt2`

## Step 2: Create an Endpoint simply by using executing the command
`az ml endpoint create -n gpt2 -f azure/endpoint/yaml`

That's it! All set - you have successfully deployed GPT2 model and it is ready to be scored.

## Step 3: Invoke the endpoint
`az ml endpoint invoke -n gpt2 --request-file test/sample-request.json`

If you want to use your favourite REST client, you can get the scoring uri and auth keys using the below:

`az ml endpoint show -n gpt2`

`az ml endpoint list-keys -n gpt2`

## Acknowledgements
This demo uses [huggingface openai gpt2 model](https://huggingface.co/transformers/model_doc/gpt2.html) ([licence](https://github.com/huggingface/transformers/blob/master/LICENSE)).
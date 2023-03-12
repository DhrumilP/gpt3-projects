import logging
import os
import openai
import azure.functions as func

# sample request body
# {"model": "text-davinci-003", "prompt": "This is a test", "max_tokens": 5, "temperature": 0.9}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # check if the request is valid
    error = []

    if not req.get_json():
        return func.HttpResponse(
            "request body is required",
            status_code=400
        )

    if not req.get_json().get("model"):
        error.append("model is required")
    if not req.get_json().get("prompt"):
        error.append("prompt is required")
    if not req.get_json().get("max_tokens"):
        error.append("max_tokens is required")
    if not req.get_json().get("temperature"):
        error.append("temperature is required")

    if error:
        return func.HttpResponse(
            ", ".join(error),
            status_code=400
        )

    # give openai secret key
    openai.api_key = os.getenv("OPENAI_SECRET_KEY")

    # get variables from the http request body
    req_body = req.get_json()

    # call the openai api
    response = openai.Completion.create(
        model=req_body["model"],
        prompt=req_body["prompt"],
        max_tokens=req_body["max_tokens"],
        temperature=req_body["temperature"],
    )

    # format the response
    response = response["choices"][0]["text"]

    # return the response
    return func.HttpResponse(
        response,
        status_code=200
    )

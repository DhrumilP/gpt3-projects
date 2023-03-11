import logging
import os
import openai
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
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

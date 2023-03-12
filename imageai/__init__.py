import logging
import os
from tkinter import N
import openai
import azure.functions as func

# sample request body
# {"model": "text-davinci-003", "prompt": "This is a test", "max_tokens": 5, "temperature": 0.9}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # check if the request is valid
    error = []

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
    # response = openai.Image.create(
    #     prompt=req_body["prompt"],
    #     n=req_body["n"],
    #     size=req_body["size"],
    # )

    list_of_url = ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-6nGThjrCJzk6m3z8NYzv8ELE/user-QP8JUIZMYGQoBFTNPwRlCNCe/img-7eFcIbNJJFh2dwJ00JrSWtC7.png?st=2023-03-11T21%3A41%3A21Z&se=2023-03-11T23%3A41%3A21Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-11T20%3A47%3A35Z&ske=2023-03-12T20%3A47%3A35Z&sks=b&skv=2021-08-06&sig=vyOGOGjOT%2BJwULTYWWmVsB8XLbuUSUUrJyDoqB6YfO4%3D',
                   'https://oaidalleapiprodscus.blob.core.windows.net/private/org-6nGThjrCJzk6m3z8NYzv8ELE/user-QP8JUIZMYGQoBFTNPwRlCNCe/img-daWpoaxWIzEaHYa5TtxIpX8d.png?st=2023-03-11T21%3A41%3A21Z&se=2023-03-11T23%3A41%3A21Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-11T20%3A47%3A35Z&ske=2023-03-12T20%3A47%3A35Z&sks=b&skv=2021-08-06&sig=6TUguQFpZZgPYHf6PdcUWEMM41Si0g5xoGO4RIYXmhA%3D']
    # for i in range(len(response["data"])):
    #     list_of_url.append(response["data"][i]["url"])

    logging.info(list_of_url)

    # return list_of_url as a response
    return func.HttpResponse(
        ",".join(str(x) for x in list_of_url),
        status_code=200
    )

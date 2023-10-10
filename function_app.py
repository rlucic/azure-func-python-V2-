import azure.functions as func
import logging

from modules.timer_triggered import trigger_boilerplate, mySecondTimer_blueprint

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

#register the function defined in the other file
app.register_functions(trigger_boilerplate)
app.register_functions(mySecondTimer_blueprint)

#@app.route(route="SimpleHTTP01V2")
@app.route(route="simplehttp")
@app.function_name(name="SimpleHTTP01V2")
def SimpleHTTP01V2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function: /simplehttp processed a request.')

    name = req.params.get('name')
    print(f"request parameters: {req.params}")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            print("no name passed in querry param or the body!!!")
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"(V2) Hello, {name}. This HTTP triggered function on route /simplehttp executed successfully.")
    else:
        return func.HttpResponse(
             "(V2) This HTTP triggered function on route simplehttp executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    



@app.route(route="secondhttp", auth_level=func.AuthLevel.ANONYMOUS)
def secondhttp(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger '/secondhttp' function processed a request.")

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"(V2) Hello, {name}. This HTTP triggered function on route '/secondhttp' executed successfully.")
    else:
        return func.HttpResponse(
             "(V2) This HTTP triggered function on route second http executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


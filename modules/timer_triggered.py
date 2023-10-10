
import azure.functions as func
import logging
import datetime
   
#this needs to be a blueprint to be registered later in the main file
trigger_boilerplate = func.Blueprint()

@trigger_boilerplate.function_name(name="myTimer")
@trigger_boilerplate.timer_trigger(schedule="*/10 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def test_TimerTrigger01_function(myTimer: func.TimerRequest) -> None:
    #print(f'myTimer argument content: {myTimer}')
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info(f'Python timer <myTimer> function executed @{get_my_time()}.')


# Second timer to be registered in the main function
mySecondTimer_blueprint = func.Blueprint()

@mySecondTimer_blueprint.function_name(name="mySecondTimer")
@mySecondTimer_blueprint.timer_trigger(schedule="*/7 * * * * *", arg_name="mySecondTimer", run_on_startup=True,
              use_monitor=False) 
def second_timer_trigger_function(mySecondTimer: func.TimerRequest) -> None:
    
    if mySecondTimer.past_due:
        logging.info('The timer is past due!')

    logging.info(f'Python timer <mySecondTimer> function executed @{get_my_time()}!')


def get_my_time() -> str:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    return utc_timestamp
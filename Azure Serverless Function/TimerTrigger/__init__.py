import datetime
import logging
import pandas as pd
import traceback

import azure.functions as func
from . import ingest
from . import sentiment
from . import topic
from . import preprocess
from . import postdata

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    print("Trail")
    tags = ["thameslink","TLUpdates","gtrailuk", "TLRailUK","Govia Thameslink Railway", "Govia Thameslink",
    "GTR thameslink"]
    frames = []

    logging.info('Starting Ingestion...')
    for tag in tags:
        db1 = ingest.ingestion(tag)
        logging.info(f'{tag} Ingestion complete.')
        frames.append(db1)
    df = pd.concat(frames)
    df.drop_duplicates(inplace=True)
 
    logging.info('Detecting Sentiments...')
    try:
        df = topic.topic_detect(df)
    except Exception as e:
            logging.error(traceback.format_exc())
            raise
    
    try:
        df = sentiment.sentiment_detect(df)
    except Exception as e:
        logging.error(traceback.format_exc())
        raise

    logging.info('Processing Data...')
    try:
        df = preprocess.preprocess_data(df)
    except Exception as e:
        logging.error(traceback.format_exc())
        raise

    logging.info('Persisting to Database...')
    try:
        postdata.write_to_database(df)
    except Exception as e:
        logging.error(traceback.format_exc())
        raise

    logging.info('Process Pipeline Complete.')

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

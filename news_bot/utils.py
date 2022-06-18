# code required for interacting with dialogflow agent
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client.json"

from google.cloud import dialogflow 
dialogflow_session_client = dialogflow.SessionsClient() 
PROJECT_ID = "newsbot-yirn"

from gnewsclient import gnewsclient
client = gnewsclient.NewsClient()

def detect_intent_from_text(text, session_id, language_code = 'en'): 
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id) 
    text_input = dialogflow.types.TextInput(text = text, Language_code = language_code) 
    query_input = dialogflow.types.QueryInput(text = text_input) 
    response = dialogflow_session_client.detect_intent(session = session, query_input = query_input) 
    return response.query_result


# takes any query from the user and the chat id, this function replaces the echoing thing
def get_reply(query, chat_id): 
    # detect_intent_from_text is called to get some response from dialogflow
    response = detect_intent_from_text(query, chat_id)

    if response.intent.display_name == 'get_news':
        return "get_news", dict(response.parameters)
    else:
        return "small talk", response.fulfillment_text

# response.parameters looks like this
# {'language': 'English', 'topic': 'Business', 'geo-country': 'United States of America'}

# the parameters are the same (response.parameters) which we are getting from the intent
def fetch_news(parameters):
    # changing the configuration of news client
    client.language = parameters.get('language')
    client.location = parameters.get('location')
    client.topic = parameters.get('topic')

    # showing first 5 news articles
    return client.get_news[:5]

topics_keyboard = [
    ['Top Stories', 'World', 'Nation'],
    ['Business', 'Technology', 'Entertainment'],
    ['Sports', 'Science', 'Health']
]
# keyboard is in the form of a grid, inner list is rows and outer list is columns 
import json
import argparse

from environs import Env
from google.cloud import dialogflow
from google.api_core.exceptions import InvalidArgument


def crate_intention(topic_answer, topic_questions, parent, intents_client):
    training_phrases = []
    for training_phrases_part in topic_questions:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[topic_answer])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=topic, training_phrases=training_phrases, messages=[message]
    )
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )
    return response


def create_parser():
    parser = argparse.ArgumentParser(description='create intention')
    parser.add_argument('questions', help='questions in json format', default='questions.json', nargs='?')
    return parser


if __name__ == '__main__':
    env = Env()
    env.read_env()
    project_id = env('PROJECT_ID')
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    parser = create_parser()
    args = parser.parse_args()

    with open(args.questions, 'r', encoding='UTF-8') as file:
        questions = file.read()
    questions = json.loads(questions)

    for topic in questions:
        topic_questions = questions[topic]['questions']
        topic_answer = questions[topic]['answer']
        try:
            response = crate_intention(topic_answer, topic_questions, parent, intents_client)
            print("Intent created: {}".format(response))
        except InvalidArgument as err:
            print(err)

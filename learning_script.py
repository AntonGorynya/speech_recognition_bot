import json
import argparse

from environs import Env
from google.cloud import dialogflow
from google.api_core.exceptions import InvalidArgument
from dialog_flow_common import crate_intention


def create_parser():
    parser = argparse.ArgumentParser(description='create intention')
    parser.add_argument('questions', help='questions in json format', default='questions.json', nargs='?')
    return parser


if __name__ == '__main__':
    env = Env()
    env.read_env()
    project_id = env('GOOGLE_CLOUD_PROJECT')
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    parser = create_parser()
    args = parser.parse_args()

    with open(args.questions, 'r', encoding='UTF-8') as file:
        questions = file.read()
    questions = json.loads(questions)

    for topic, qa_pair in questions.items():
        topic_questions = qa_pair['questions']
        topic_answer = qa_pair['answer']
        try:
            response = crate_intention(topic, topic_answer, topic_questions, parent, intents_client)
            print("Intent created: {}".format(response))
        except InvalidArgument as err:
            print(err)

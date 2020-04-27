#!usr/bin/python3

from os.path import exists
from os import getenv, mkdir
from dotenv import load_dotenv
import sys
import json
import email
import base64
from pprint import pprint

sys.path.append('lib')
from gmailauthentication import readOnlyGmailAuth
load_dotenv()

class importFile:
    def __init__(self):
        self.file_location = 'imported.json'
        if not exists(self.file_location):
            print('no imported.json file located - creating...')
            file = open('imported.json', 'w+')
            j = '{"lastImport": "2000-01-01", "importedProblems": []}'
            file.write(j)
            file.close()

    def _getData(self, k):
        file = open(self.file_location, 'r')
        data = json.load(file)
        file.close()

        return data.get(k)

    def lastImport(self):
        return self._getData('lastImport')

    def importedProblems(self):
        return self._getData('importedProblems')

    def updateImported(self, new_imports):
        file = open(self.file_location, 'r')
        data = json.load(file)
        data['importedProblems'] = data.get('importedProblems') + new_imports
        file = open(self.file_location, 'w')
        json.dump(data, file, indent=4)
        file.close()

    def updateImportDate(self, new_date):
        file = open(self.file_location, 'r')
        data = json.load(file)
        data['lastImport'] = new_date
        file = open(self.file_location, 'w')
        json.dump(data, file, indent=4)
        file.close()


def listMessages(service, last_import):
    query = f'after:{last_import} from:(daily@techseries.dev) subject:([Daily Problem])'
    response = service.users().messages().list(userId='me',
                                            q=query,
                                            #labelIds=label_ids,
                                            includeSpamTrash=False
                                            ).execute()

    messages = []
    if 'messages' in response: messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me',
                                                  q=query,
                                                  #labelIds=label_ids,
                                                  pageToken=page_token,
                                                  includeSpamTrash=False
                                                  ).execute()

        messages.extend(response['messages'])
        if len(messages) > 1000:
            print("you're getting too many god damn messages and I'm stopping this shit")
            return messages

    return messages


def getMessage(service, msg_id):
    '''
    Get raw message and meta data from a given message id
    '''
    try:
        message = service.users().messages().get(userId='me',
                                              id=msg_id,
                                              format='raw'
                                              ).execute()

        meta_data = service.users().messages().get(userId='me',
                                                id=msg_id,
                                                format='metadata',
                                                metadataHeaders=['Subject', 'X-SES-Outgoing']
                                                ).execute()

        message['metaData'] = meta_data
        return message
    except:
        raise



def getProblemName(headers):
    import re
    # subject should always be "[Daily Problem] Problem Name" and this will
    # take the problem name, make it lowercase, and replace spaces with a dash
    subject = [i['value'] for i in headers if i['name'] == 'Subject'][0]
    subject = re.sub('[^A-Za-z0-9|\s]+', '', subject)
    subject = subject.replace('Daily Problem ', '').replace(' ', '-').lower()

    return subject


def getProblemDate(headers):
    # date value in this field is expected to be YYYY.MM.DD-IP and this pulls
    # the date into YYYY-MM-DD format for the problem prefix
    date = [i['value'] for i in headers if i['name'] == 'X-SES-Outgoing'][0]
    date = date.split('-')[0].replace('.', '-')

    return date


def createProblemFile(problem_content, problem_name, target_folder):
    file = open(target_folder + problem_name + '.py', 'w')
    print(f'creating {problem_name}')
    file.write(problem_content)
    file.close()


def createProblemContent(message):
    #msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
    #mime_msg = email.message_from_string(msg_str)
    #mime_msg = email.message_from_string(message['raw'])
    #e = mime_msg.keys()

    #pprint(mime_msg.get_body(preferencelist=('related', 'html', 'plain')))

    #pprint(e)
    #pprint(mime_msg.as_string())
    #exit()
    problem_content = 'placeholder text'

    return problem_content

def main():
    target_folder = 'imported-from-gmail/'
    if not exists(target_folder): mkdir(target_folder)

    importInfo = importFile()
    last_import = importInfo.lastImport()
    imported_problems = importInfo.importedProblems()

    # get gmail service object
    gmail = readOnlyGmailAuth(getenv('GOOGLE_CLIENT_SECRETS_FILE'))

    messages = listMessages(gmail, last_import)

    if not messages: print('No messages to import.')
    if messages: print(f"Importing {len(messages)} dailyinterview messages after {last_import}.'")

    max_date_imported = last_import
    files_imported = []
    try:
        for m in messages:
            message = getMessage(gmail, m['id'])
            msg_headers = message['metaData']['payload']['headers']

            problem_date = getProblemDate(msg_headers)
            problem_subject = getProblemName(msg_headers)
            problem_name = problem_date + '-' + problem_subject

            if problem_name not in imported_problems:
                # check if date is greater than current max
                if problem_date > max_date_imported: max_date_imported = problem_date

                # create the file - create imported/ directory if doesn't exist
                if not exists(target_folder): mkdir(target_folder)
                problem_content = createProblemContent(message)
                createProblemFile(problem_content, problem_name, target_folder)

                # append file name to imported files list
                files_imported.append(problem_name)

        # if and only if it makes it through the full message loop does it update the last import date
        importInfo.updateImportDate(max_date_imported)
    except:
        raise
    finally:
        # always logs if the file was created so it skips it in the future
        importInfo.updateImported(files_imported)


if __name__ == '__main__':
    main()

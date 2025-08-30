import dotenv
dotenv.load_dotenv()
import requests
from requests.auth import HTTPBasicAuth
import json
import os


url = "https://whatsapptojira.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("apitesting521@gmail.com", os.environ.get('JIRA_API_KEY'))

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


def create_jir_issue(title, desc, issue_type_id, priority_id, labels):
    payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": desc,
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },

    "issuetype": {
      "id": issue_type_id
    },

    "project": {
      "key": "SCRUM"
    },

    "summary": title,
    "labels": labels,
    "priority": {
      "id": priority_id   # 1 = Highest, 2 = High, 3 = medium, 4 = Low, 5 = Lowest
    }
    },

  "update": {}
} )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response

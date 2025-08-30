import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://whatsapptojira.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("apitesting521@gmail.com", "ATATT3xFfGF0p26M2HlAbmGNYZpiUGctAnrprzlL5hDvFnIerTS3H_6uN1QJ5OzeWR9e1oDznQEI9HhpYU2y4wiWU2Y_udgSn5_7cNsAjwZnBXKOvERqL_8xF8U-y_l2dFQ6GwA8Ld8_pfAWpIg0bDwqJFcoILHIVS8ep3rF9nzoDnXVTDcxaJU=101F902C")

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

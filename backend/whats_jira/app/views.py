import dotenv
dotenv.load_dotenv()
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .gemini_llm import gemini_response
from .models import JiraTicket
import json
from .jira_issue import create_jir_issue
from google.cloud import speech
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
import os

@csrf_exempt
def index(request):
    if request.method == "POST":
        message_json = twilio_test()
        message = message_json.content.decode('utf-8')
        message = json.loads(message)['message']
        print(message)
        prompt = (
                "Suppose you are a WhatsApp message extractor. I have configured Twilio with Python so "
                "'Hello twilio' and its related words should be ignored. Extract actual professional details "
                "from the prompt. Output in JSON format: "
                "{'title': '', 'description': '', 'priority': '', 'labels': 'list of labels'}. "
                "Message is: " + message
            )
        result = gemini_response(prompt).text
        result = result.strip("```json").strip("```").strip()
        print(result)
        json_res = json.loads(result)
        
        json_res["labels"] = [item.replace(' ', '') for item in json_res["labels"]]
        print(json_res)
        if json_res["priority"] == "1":
            json_res["priority"] = "Highest"
        elif json_res["priority"] == "2":
            json_res["priority"] = "High"
        elif json_res["priority"] == "3":
            json_res["priority"] = "Medium"
        elif json_res["priority"] == "4":
            json_res["priority"] = "Low"
        elif json_res["priority"] == "5":
            json_res["priority"] = "Lowest"

        create_draf_ticket = JiraTicket.objects.create(
            title=json_res["title"],
            description=json_res["description"],
            issue_type_id="10003",
            priority_id=json_res["priority"],
            labels=json_res["labels"],
            approved=False
        )
        create_draf_ticket.save()
        return JsonResponse({"status": "success", "message": "Draft ticket created"})
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)


def fetch_draft_tickets(request):
    draft_tickets = JiraTicket.objects.filter(approved=False).order_by('-id')
    tickets_list = []
    for ticket in draft_tickets:
        tickets_list.append({
            "id": ticket.id,
            "title": ticket.title,
            "description": ticket.description,
            "issue_type_id": ticket.issue_type_id,
            "priority_id": ticket.priority_id,
            "labels": ticket.labels,
            "approved": ticket.approved
        })
    return JsonResponse({"status": "success", "draft_tickets": tickets_list})

@csrf_exempt
def jira_issue_creation(request):
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        print(data)
        ticket_id = data.get("id")
        title = data.get("title")
        desc = data.get("description")
        issue_type_id = data.get("issue_type_id", "10003")  
        priority_id = data.get("priority", "3")  
        labels = data.get("labels", [])

        update_ticket = JiraTicket.objects.get(id=ticket_id)
        update_ticket.title = title
        update_ticket.description = desc
        update_ticket.priority_id = priority_id
        update_ticket.labels = labels

        update_ticket.approved = True
        update_ticket.save()

        if priority_id == "Highest":
            priority_id = "1"
        elif priority_id == "High":
            priority_id = "2"
        elif priority_id == "Medium":
            priority_id = "3"
        elif priority_id == "Low":
            priority_id = "4"
        elif priority_id == "Lowest":
            priority_id = "5"

        jira_issue_create = create_jir_issue(title, desc, issue_type_id, priority_id, labels)
        return JsonResponse({"status": "success", "response": "created"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)
    

def twilio_test():
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Add new feature in which user can see all the report of their customers and can perform crud operation on it',
        from_='whatsapp:+14155238886',  # Twilio sandbox WhatsApp number
        to='whatsapp:+917568170690'  # Your WhatsApp number in E.164 format
    )

    # messages = client.messages.list(limit=20, to='whatsapp:+917568170690')
    # actual_msg = ""
    # for record in reversed(messages):
    #     actual_msg+= record.body +" "
    # print(actual_msg)

    # print(message.sid)
    return JsonResponse({"status": "success", "message": "actual_msg"})


# WhatsJira

WhatsJira is a Django-based backend service that integrates WhatsApp messaging (via Twilio), Google Gemini LLM, and Jira ticket management. It allows users to create, review, and approve Jira tickets using WhatsApp messages.

## Features

- Extracts professional details from WhatsApp messages using Gemini LLM.
- Creates draft Jira tickets from WhatsApp messages.
- Allows review and approval of draft tickets before creating them in Jira.
- Integrates with Twilio for WhatsApp messaging.
- Supports CRUD operations on Jira tickets.

## Setup

### Prerequisites

- Python 3.8+
- Django
- Twilio account (for WhatsApp integration)
- Jira account and API access

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MadhubanKhatri/whatsapp-jira.git
   cd whats_jira
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:

   ```
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_credentials.json
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Send a WhatsApp message to your Twilio sandbox number.
- The backend extracts ticket details and creates a draft Jira ticket.
- Review and approve tickets via the provided API endpoints.

## API Endpoints

- `POST /` : Extracts ticket info from WhatsApp message and creates a draft ticket.
- `GET /fetch_draft_tickets/` : Lists all draft tickets.
- `POST /jira_issue_creation/` : Approves and creates a Jira ticket.



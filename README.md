Automated Email Sender

This Python script sends automated emails to a list of HR contacts using Gmail's SMTP service. The email content is customizable, and it securely sends messages to the recipients.

## Features
- Sends emails to multiple contacts from a predefined dictionary.
- Customizes the email content for each recipient.
- Uses Gmail's SMTP service for secure email delivery.

## Requirements
- Python 3.x
- An active Gmail account with "App Password" enabled (required for authentication).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/email-sender.git
   cd email-sender
   ```

2. **Install dependencies:**
   The script uses Python's built-in libraries, so no external dependencies are needed.

3. **Modify the script:**
   Update the following fields in the script:
   - `your_email`: Your Gmail address.
   - `your_password`: Your Gmail App Password.
   - `hr_contacts`: Add or modify HR contacts in the dictionary.

   ```python
   your_email = 'your-email@gmail.com'
   your_password = 'your-app-password'

   hr_contacts = {
       "contact_name1": "contact1@example.com",
       "contact_name2": "contact2@example.com"
   }
   ```

4. **Run the script:**
   ```bash
   python email_sender.py
   ```

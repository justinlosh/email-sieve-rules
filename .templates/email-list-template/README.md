## Email List Template Explanation

This template defines the structure for specifying email filtering rules in JSON format. Below is a breakdown of each field:

### Top-Level Fields

- **name**: The name of the email list or rule set.
- **domain**: The domain associated with the email addresses.
- **friendly_name**: A human-readable name for easy identification.

### email_criteria (Array)

Each object in this array represents a single filtering rule:

- **field**: The email field to check (e.g., "subject", "from", "to").
- **contains**: The string or keyword to look for in the specified field.
- **action**: The action to take when the criteria match (e.g., "move", "delete", "flag").
- **folder**: The folder to move the email to (used if action is "move").

### Example

```json
{
    "name": "Work Emails",
    "domain": "example.com",
    "friendly_name": "Work",
    "email_criteria": [
        {
            "field": "from",
            "contains": "boss@example.com",
            "action": "move",
            "folder": "Important"
        }
    ]
}
```

Use this template to define custom email filtering rules for your application.

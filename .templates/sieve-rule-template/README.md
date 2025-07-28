## Configuration Schema Breakdown

This section describes each part of the configuration JSON used for email sieve rules.

### Top-Level Fields

- **name**:  
    The unique identifier for the rule.

- **domain**:  
    The domain to which this rule applies.

- **friendly_name**:  
    A human-readable name for the rule.

- **description**:  
    A brief explanation of what the rule does.

- **enabled**:  
    Boolean value (`true` or `false`) indicating if the rule is active.

- **priority**:  
    An integer specifying the rule's execution order (lower numbers run first).

- **tags**:  
    An array of labels for categorizing the rule.

- **created_at** / **updated_at**:  
    Timestamps for when the rule was created and last modified.

### Criteria Section

- **criteria_type**:  
    Specifies how multiple criteria are evaluated (`all` means all must match, `any` means at least one must match).

- **email_criteria**:  
    An array of conditions to match incoming emails. Each object includes:
    - **field**: The email field to check (e.g., `from`, `subject`).
    - **contains**: The value to look for in the specified field.
    - **actions**: List of actions to perform if the criteria match. Example:
        - **action**: The operation to execute (e.g., `fileinto`).
        - **folder**: The target folder for the action.

### Testing Section

- **test_emails**:  
    An array of sample emails for testing the rule.

---

This schema allows you to define, categorize, and test email filtering rules in a structured way.
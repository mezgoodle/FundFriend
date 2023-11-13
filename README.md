# FundFriend

```mermaid
stateDiagram-v2
    [*] --> Site
    Site --> Login/Registration
    Login/Registration --> Profile/Settings
    Profile/Settings --> DB_on_Backend
    Profile/Settings --> Role
    Role --> Customer
    Role --> Banker
    Banker --> Bank_Documents
    Banker --> Chatbot
    Banker --> User_Documents
    Bank_Documents --> Code_base_on_Azure
    Customer --> Chatbot
    Customer--> User_Documents
    User_Documents --> DB_on_Backend
    Chatbot --> LUIS
    LUIS --> QNA
    QNA --> Code_base_on_Azure
    QNA --> Chatbot
```

# FundFriend

[![codecov](https://codecov.io/gh/mezgoodle/FundFriend/graph/badge.svg?token=6t72TDeS24)](https://codecov.io/gh/mezgoodle/FundFriend)
[![wakatime](https://wakatime.com/badge/user/13631fc5-0ee5-4aed-920d-b02dc1546d51/project/018b812c-f504-4813-900d-fc64320b8527.svg)](https://wakatime.com/badge/user/13631fc5-0ee5-4aed-920d-b02dc1546d51/project/018b812c-f504-4813-900d-fc64320b8527)

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

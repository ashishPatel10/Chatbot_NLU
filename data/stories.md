## happy path
* greet
  - action_hello_world
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## package reply
* package{"company_name":"infosys"}
  - utter_package
  
## bond reply
* bond{"company_name":"infosys"}
- utter_bond

## packagebond reply
* package+bond
- utter_package_bond

## happy path
* greet
  - utter_greet
  
## response reply
* response
  - utter_thanks

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
* package
  - action_package
  
## bond reply
* bond
- action_bond

## packagebond reply
* package+bond
- action_packagebond

## location reply
* location
- action_location

## locationbond reply
* location+bond
- action_locationbond

## package location
* package+location
- action_packagelocation

## bondlocationpackage reply
* bond+location+package
- action_bondlocationpackage

## process reply
* process
- action_process

## roundwise reply
* roundwise
- action_roundnumber


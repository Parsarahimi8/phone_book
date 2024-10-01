import json
from behave import given, when, then
import requests

BASE_URL = "http://127.0.0.1:8000/contacts"

@given("the API is running")
def step_api_running(context):
    context.base_url = BASE_URL

@when("I create a contact with first name {first_name}, last name {last_name}, phone number {phone_number}, and description {description}")
def step_create_contact(context, first_name, last_name, phone_number, description):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "description": description
    }
    response = requests.post(f"{context.base_url}/create", json=data)
    context.response = response
    context.contact_id = response.json().get("id")

@then("the contact should be created successfully")
def step_contact_created(context):
    assert context.response.status_code == 200

@then("the response should contain the contact's id")
def step_response_contains_id(context):
    assert "id" in context.response.json()

@when("I retrieve the contact by first name {first_name} and last name {last_name}")
def step_retrieve_contact(context, first_name, last_name):
    response = requests.get(f"{context.base_url}/search?first_name={first_name}&last_name={last_name}")
    context.response = response

@then("the contact should be found")
def step_contact_found(context):
    assert context.response.status_code == 200

@then("the contact's phone number should be {phone_number}")
def step_contact_phone_number(context, phone_number):
    assert context.response.json()["phone_number"] == phone_number

@when("I update the contact's first name to {new_first_name}")
def step_update_contact(context, new_first_name):
    data = {
        "first_name": new_first_name
    }
    response = requests.put(f"{context.base_url}/{context.contact_id}/update", json=data)
    context.response = response

@then("the contact's first name should be {expected_name}")
def step_contact_first_name(context, expected_name):
    assert context.response.json()["first_name"] == expected_name

@when("I delete the contact by first name {first_name} and last name {last_name}")
def step_delete_contact(context, first_name, last_name):
    # Retrieve the contact to get its ID first
    response = requests.get(f"{context.base_url}/search?first_name={first_name}&last_name={last_name}")
    if response.status_code == 200:
        contact_id = response.json()["id"]
        context.response = requests.delete(f"{context.base_url}/{contact_id}/delete")

@then("the contact should not be found")
def step_contact_not_found(context):
    assert context.response.status_code == 404

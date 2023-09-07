"""
This below set of function will do the task they have been assigned of sending the paload further on the client
application or ONDC network.
"""


def retial_to_client(ch, method, properties, body):
    payload = body.decode("utf-8")
    print("\n\n>>>>>retial_to_client>>>>")
    print(">>>>>>>payload>>>>>>>>>", payload)


def retail_to_network(ch, method, properties, body):
    payload = body.decode("utf-8")
    print("\n\n>>>>>retail_to_network>>>>")
    print(">>>>>>>payload>>>>>>>>>", payload)


def logistic_to_client(ch, method, properties, body):
    payload = body.decode("utf-8")
    print("\n\n>>>>>logistic_to_client>>>>")
    print(">>>>>>>payload>>>>>>>>>", payload)


def logistic_to_network(ch, method, properties, body):
    payload = body.decode("utf-8")
    print("\n\n>>>>>logistic_to_network>>>>")
    print(">>>>>>>payload>>>>>>>>>", payload)


# generate_narrative.py

def generate_narrative(data):
    """
    This function takes input data and generates a narrative.

    :param data: Input data, typically a list or a dictionary containing the necessary details.
    :return: Generated narrative as a string.
    """

    # Example logic to generate a narrative (customize this as per your needs)
    narrative = "Narrative generated based on the following data:\n"

    # Iterate over the data and append the details to the narrative (for example purposes)
    if isinstance(data, dict):
        for key, value in data.items():
            narrative += f"{key}: {value}\n"
    elif isinstance(data, list):
        for item in data:
            narrative += f"- {item}\n"
    else:
        narrative += "Invalid data format."

    return narrative

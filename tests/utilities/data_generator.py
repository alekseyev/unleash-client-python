def generate_context():
    return {"userId": 'test@test.zakaz.ua'}


def generate_email_list(num):
    """
    Generates an unleash-style list of emails for testing.

    :param num:
    :return:
    """
    first_email = 'test@test.zakaz.ua'
    email_list_string = first_email

    context = {"userId": first_email}

    for i in range(num - 1):
        email_list_string += "," + 'test_%d@test.zakaz.ua' % i

    return (email_list_string, context)

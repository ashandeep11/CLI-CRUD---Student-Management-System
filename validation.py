def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print(
            "Input cannot be empty. Please try again."
        )


def get_positive_integer(prompt):
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:
            print(
                "Invalid input. Please enter a whole number."
            )


def get_valid_email(prompt):
    while True:
        email = input(prompt).strip()

        if (
            "@" in email
            and "." in email.split("@")[-1]
            and " " not in email
        ):
            return email

        print(
            "Invalid email. Please enter a valid email address."
        )


def get_optional_value(prompt, current_value):
    value = input(
        f"{prompt} [{current_value}]: "
    ).strip()

    if value:
        return value

    return current_value
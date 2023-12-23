from django.core.validators import RegexValidator


class PhoneNumberValidator(RegexValidator):
    regex = r"^(90|91|93|94|95|97|98|99|77|88|55|33)\d{7}$"
    message = "The phone number must consist of 9 digits and start."
    code = "invalid_phone_number"

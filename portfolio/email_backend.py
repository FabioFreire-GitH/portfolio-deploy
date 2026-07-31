import ssl
from django.core.mail.backends.smtp import EmailBackend
from django.utils.functional import cached_property

class SSLEmailBackend(EmailBackend):
    @cached_property
    def ssl_context(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context

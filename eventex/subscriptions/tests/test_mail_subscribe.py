from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Allan Silva', cpf='12345678911', email='allan.sbo@hotmail.com', phone='11-93231-3231')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'allan.sbo@hotmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['allan.sbo@hotmail.com', 'allan.sbo@hotmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Allan Silva',
            '12345678911',
            'allan.sbo@hotmail.com',
            '11-93231-3231',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

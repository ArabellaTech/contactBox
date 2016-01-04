from django.test import TestCase
from django.core.management import call_command
from django.core import mail

from contactbox.models import Message, Receiver


class MainTestCase(TestCase):
    def setUp(self):
        Receiver.objects.create(
            name='test',
            email='foo@bar.com',
            active=True)
        Receiver.objects.create(
            name='test',
            email='foo1@bar.com',
            active=True)
        Receiver.objects.create(
            name='test',
            email='foo2@bar.com',
            active=False)

    def test_sending(self):
        message = Message.objects.create(
            email='a@a.com',
            message='message',
        )
        self.assertEqual(mail.outbox, [])
        self.assertIsNone(message.notification_date)
        call_command('remind_contact')
        self.assertIsNorNone(message.notification_date)
        self.assertEqual(len(mail.outbox), 1)

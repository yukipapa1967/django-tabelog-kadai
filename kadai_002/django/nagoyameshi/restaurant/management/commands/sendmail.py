from typing import Any
from django.core.management.base import BaseCommand
from django.core.mail import BadHeaderError, send_mail


class Command(BaseCommand):
    help = "メール送信テスト"

    def handle(self, *args, **options):
        print('メール送信')

        """題名"""
        subject = "メール送信テスト"

        """本文"""
        message = "こんにちは。メールを送信しました"

        """送信元メールアドレス"""
        from_email = "tg.wara0810@gmail.com"

        """宛先メールアドレス"""
        recipient_list = [
            "tg.wara0810@gmail.com"
        ]

        send_mail(subject, message, from_email, recipient_list)


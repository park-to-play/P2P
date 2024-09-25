#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# manage.py: Django 프로젝트의 시작점. 프로젝트와 관련된 명령어를 실행할 때 사용합니다.
# Django가 프로젝트를 시작할 때 자동으로 생성하는 파일입니다.
# 프로젝트를 진행하면서 이 파일 자체를 수정할 일은 거의 없습니다.
def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p2p.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

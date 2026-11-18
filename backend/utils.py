import hashlib
import json
import pickle

import requests


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_session(data):
    return pickle.loads(data)


def fetch_status(url):
    return requests.get(url, timeout=10)


def add_item(item, items=[]):
    items.append(item)
    return items


def safe_read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        pass


def average(values):
    # ZeroDivisionError لو القايمة فاضية: ده خطأ منطقي، الأدوات الحالية مش هتكتشفه
    return sum(values) / len(values)


def broken():
    unused = 1
    return undefined_name

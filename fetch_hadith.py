# scripts/fetch_ali_hadiths.py
import requests
from django.conf import settings
import django
import os
import time

# تنظیمات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ghadir.settings")
django.setup()

from hadiths.models import Hadith

API_URL = "https://api.keybit.ir/hadis"

def fetch_and_save_ali_hadiths(limit=100):
    count = 0
    tries = 0
    max_tries = limit * 10

    while count < limit and tries < max_tries:
        tries += 1
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                data = response.json()
                result = data.get("result", {})
                person = result.get("person", "")
                if "امام علی" in person:
                    text = result.get("text", "").strip()
                    source = result.get("source", "").strip()

                    # بررسی تکراری نبودن بر اساس متن حدیث
                    if not Hadith.objects.filter(text=text).exists():
                        Hadith.objects.create(
                            person=person.strip(),
                            text=text,
                            source=source
                        )
                        count += 1
                        print(f"{count}. ✅ Saved: {text[:50]}...")
                    else:
                        print("🔁 Duplicate - Skipped")
                else:
                    print("⏩ Not from Imam Ali")
            else:
                print("❌ API Error:", response.status_code)
        except Exception as e:
            print("⚠️ Exception:", str(e))
        time.sleep(0.5)

    print(f"✅ Done. {count} unique hadiths saved.")

# اجرا
if __name__ == "__main__":
    fetch_and_save_ali_hadiths(limit=50)

!pip install langdetect

from langdetect import detect, DetectorFactory, LangDetectException

# برای ثبات در تشخیص زبان
DetectorFactory.seed = 0

# دیکشنری نگاشت کد زبان به نام کامل
LANG_CODES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'sq': 'Albanian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tl': 'Tagalog',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)'
}

def detect_language_from_text(text):
    try:
        code = detect(text)
        language = LANG_CODES.get(code.lower(), code)
        print(f"زبان متن: {language}")
    except LangDetectException:
        print("نمی‌توان زبان متن را تشخیص داد.")

def detect_language_from_file(file_path):
    encodings = ['utf-8', 'cp1256', 'latin1']  # اول utf-8، سپس CP1256 (فارسی ویندوز)، سپس latin1
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                text = f.read()
            print(f"خواندن فایل با کدگذاری: {enc}")
            detect_language_from_text(text)
            return
        except UnicodeDecodeError:
            continue
    print("فایل را نتوانستیم بخوانیم. کدگذاری نامعتبر است.")

# ---- ورودی کاربر ----
choice = input("می‌خواهید متن را مستقیم وارد کنید یا فایل بدهید؟ (text/file): ").strip().lower()

if choice == "text":
    user_text = input("لطفا متن خود را وارد کنید:\n")
    detect_language_from_text(user_text)
elif choice == "file":
    file_path = input("لطفا مسیر فایل متنی خود را وارد کنید:\n")
    detect_language_from_file(file_path)
else:
    print("ورودی نامعتبر. لطفا 'text' یا 'file' وارد کنید.")


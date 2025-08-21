!pip install langdetect hazm
!pip install --quiet hazm

import re
from hazm import Normalizer, word_tokenize
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0
normalizer = Normalizer()

# دیکشنری هوشمند برای افعال و اصطلاحات رایج
smart_replacements = {
    r"\bاومد\b": "آمد",
    r"\bمیخوای\b": "می‌خواهی",
    r"\bمیخوایم\b": "می‌خواهیم",
    r"\bمیخواین\b": "می‌خواهید",
    r"\bمیخوان\b": "می‌خواهند",
    r"\bنمیخوام\b": "نمی‌خواهم",
    r"\bنمیتونم\b": "نمی‌توانم",
    r"\bنمیتونه\b": "نمی‌تواند",
    r"\bنمیخوان\b": "نمی‌خواهند",
    r"\bداره\b": "دارد",
    r"\bدارم\b": "دارم",
    r"\bداری\b": "داری",
    r"\bداریم\b": "داریم",
    r"\bدارین\b": "دارید",
    r"\bبزار\b": "بگذار",
    r"\bبده\b": "بدهد",
    r"\bمیدم\b": "می‌دهم",
    r"\bمیدن\b": "می‌دهند",
    r"\bمیبینم\b": "می‌بینم",
    r"\bمیبینه\b": "می‌بیند",
    r"\bمیبینن\b": "می‌بینند",
    r"\bمی کنه\b": "می کند",
    r"\bمیگن\b": "می‌گویند",
    r"\bنمیدونم\b": "نمی‌دانم",
    r"\bچیکار\b": "چه‌کار",
    r"\bجذابه\b": "جذاب است",
    r"\bکی\b": "چه‌کسی",
    r"\bکجا\b": "در کجا",
    r"\bحالا\b": "اکنون",
    r"\bالان\b": "در حال حاضر",
    r"\bآره\b": "بله",
    r"\bنه\b": "خیر",
    r"\bباشه\b": "باشد",
    r"\bخوبه\b": "خوب است",
    r"\bهمینه\b": "همین است",
    r"\bچرا\b": "به چه دلیل",
    r"\bکردن\b": "انجام دادن",
    r"\bمیکنم\b": "می‌کنم",
    r"\bنیمخوانم\b": "نمی‌خوانم",
    r"\bآبجی\b": "خواهر",
}

# بررسی زبان فارسی
def is_farsi(text: str) -> bool:
    try:
        return detect(text) == 'fa'
    except LangDetectException:
        return False

# رسمی‌سازی متن با اعمال جایگزینی هوشمند
def auto_formalize_full(text: str) -> str:
    text = normalizer.normalize(text)
    tokens = word_tokenize(text)
    new_tokens = []
    for token in tokens:
        token_new = token
        for pattern, replacement in smart_replacements.items():
            token_new = re.sub(pattern, replacement, token_new)
        new_tokens.append(token_new)
    formal_text = " ".join(new_tokens)
    return formal_text

# شماره‌گذاری خطوط
def formalize_lines_full(text: str) -> str:
    lines = text.strip().split('\n')
    formal_lines = []
    for idx, line in enumerate(lines, 1):
        line = line.strip()
        if line:
            formal_line = auto_formalize_full(line)
            formal_lines.append(f"{idx}. {formal_line}")
    return "\n".join(formal_lines)

# --- متن ورودی ---
text = """
ممنون تلوبیون
من از این فیلم خیلی خوشم اومد خیلی هم ممنون
آبجی من ۲۱ ساله‌اش ولی پونی نگاه می‌کنه
آخ اخ از بهاره افشاری عزیز که انقدر عالی بود
آخ جونم
آخر خنده
آخرت فیلم
آخرت ٱنیمیشن کمدی خیلی خیلی باحال و جذابه
"""

# اعمال رسمی‌سازی
if is_farsi(text):
    formal_text = formalize_lines_full(text)
    print("متن رسمی شده:\n")
    print(formal_text)
else:
    print("متن فارسی نیست.")

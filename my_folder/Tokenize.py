from hazm import word_tokenize, Normalizer

normalizer = Normalizer()

def tokenize(text):
    """
    نرمال‌سازی و توکنایز کردن متن فارسی.

    Args:
        text (str): متن فارسی که می‌خوای توکنایز بشه.

    Returns:
        list: لیست کلمات توکنایز شده با فاصله درست.
    """
    # نرمال‌سازی اولیه متن
    text = normalizer.normalize(text)

    # توکنایز کردن متن
    tokens = word_tokenize(text)

    return tokens

# --- نمونه استفاده ---
my_text = "میخوام برم سینما ولی نمیتونم."
tokens = tokenize(my_text)
print(tokens)

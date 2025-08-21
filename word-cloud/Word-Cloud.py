import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# مسیر فونت وزیر
font_path = "/content/Vazirmatn[wght] (1).ttf"   # یا جایی که فونت رو گذاشتی

# بارگذاری تصویر ماسک (سفید = پس‌زمینه، سیاه = محل کلمات)
mask = np.array(Image.open("/content/pngtree-gradient-circle-text-box-prmotion-sale-banner-png-image_4852602.png"))   # اینجا هر شکلی می‌تونی بذاری

text = """
زبان فارسی یکی از زیباترین زبان‌های دنیاست
ابر کلمات روشی جذاب برای نمایش داده‌های متنی است
هوش مصنوعی و یادگیری ماشین ابزارهای قدرتمندی هستند
"""

# ساخت ابرکلمات با ماسک
wordcloud = WordCloud(
    font_path=font_path,
    mask=mask,
    background_color="white",
    width=1000,
    height=600,
    max_words=300,
    min_font_size=10
).generate(text)

# نمایش
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

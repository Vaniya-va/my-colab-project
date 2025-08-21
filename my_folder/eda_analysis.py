import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# بارگذاری فایل اکسل
df = pd.read_excel("/content/Sentiment Analysis data (2) (1).xlsx")

# حذف ردیف اول که در واقع عنوان ستون‌هاست
df = df.iloc[1:].copy()

# نامگذاری ستون‌ها
df.columns = ['comment', 'label']

# تبدیل نوع برچسب‌ها به عدد صحیح
df['label'] = df['label'].astype(int)

# تبدیل ستون کامنت به رشته (در صورت وجود مقادیر عددی)
df['comment'] = df['comment'].astype(str)

# محاسبه طول متن‌ها
df['char_length'] = df['comment'].apply(len)
df['word_count'] = df['comment'].apply(lambda x: len(x.split()))

# ---------------------------
# 🔍 بررسی آماری اولیه
# ---------------------------
print("✅ تعداد کل نمونه‌ها:", len(df))
print("\n✅ تعداد نمونه در هر کلاس:")
print(df['label'].value_counts())

print("\n✅ تعداد داده‌های تکراری:", df.duplicated().sum())
print("✅ تعداد مقادیر خالی در هر ستون:\n", df.isnull().sum())

# ---------------------------
# 📊 رسم نمودارها
# ---------------------------
plt.figure(figsize=(15, 4))

# نمودار تعداد برچسب‌ها
plt.subplot(1, 3, 1)
sns.countplot(x='label', data=df)
plt.title('تعداد نمونه در هر برچسب')
plt.xlabel('برچسب (1=مثبت, 0=خنثی, -1=منفی)')

# نمودار توزیع طول کاراکتری نظرات
plt.subplot(1, 3, 2)
sns.histplot(df['char_length'], bins=50, kde=True, color='skyblue')
plt.title('توزیع طول نظرات (کاراکتر)')

# نمودار توزیع تعداد کلمات
plt.subplot(1, 3, 3)
sns.histplot(df['word_count'], bins=50, kde=True, color='orange')
plt.title('توزیع تعداد کلمات در نظرات')

plt.tight_layout()
plt.show()

# ---------------------------
# 📝 نمایش چند نمونه تصادفی
# ---------------------------
print("\n🔍 چند نمونه تصادفی از داده‌ها:")
print(df.sample(5))

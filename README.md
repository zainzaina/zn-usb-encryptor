# Secure USB Encryption Tool

برنامج بسيط بواجهة رسومية لحماية الملفات باستخدام مفتاح موجود على فلاش USB وكلمة مرور محلية.

**وصف المشروع:**
- أداة GUI تعتمد على `tkinter` لتشفير/فك تشفير ملفات باستخدام مكتبة `cryptography`.
- يعتمد التشفير على مفتاح ثانوي محفوظ على فلاش USB (`usb.key`) بالإضافة إلى كلمة المرور: المفتاح مشتق من دمج كلمة المرور ومحتوى ملف المفتاح.

**مميزاته:**
- قفل/فتح التطبيق باستخدام كلمة مرور + ملف مفتاح على USB.
- تشفير ملف واحد ثم استبداله بالنسخة المشفرة.
- فك تشفير ملف مشفّر إذا كان المفتاح وكلمة المرور صحيحين.
- إقفال تلقائي عند إزالة الفلاش.
- سجل نشاطات بسيط في `activity.log`.

**المتطلبات:**
- Python 3.8+
- الحزم: `cryptography` (ثبّتها باستخدام `pip install cryptography`).
- `tkinter` عادةً مثبتة مع بايثون على معظم الأنظمة.

**تثبيت وتشغيل (Windows):**
1. أنشئ بيئة افتراضية (اختياري):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install cryptography
```

2. شغّل الواجهة:

```powershell
python secure_encryptor_gui.py
```

**إعداد مفتاح USB (مفتاحك):**
- افصل فلاش USB وارْفع حرف محرك الأقراص (مثلاً `E:`). الملف المطلوب هو `usb.key` ويجب وضعه في جذر الفلاش أو تعديل مسار `USB_KEY_PATH` في ملف `secure_encryptor_gui.py`.

مثال إنشاء ملف مفتاح عشوائي باستخدام بايثون:

```powershell
python - <<'PY'
import os
open('E:/usb.key','wb').write(os.urandom(32))
print('usb.key created on E:')
PY
```

أو باستخدام PowerShell:

```powershell
$bytes = New-Object byte[] 32; (New-Object System.Security.Cryptography.RNGCryptoServiceProvider).GetBytes($bytes); [IO.File]::WriteAllBytes('E:\usb.key',$bytes)
```

بعد إنشاء `usb.key`، تأكد من تعديل السطر العلوي في `secure_encryptor_gui.py` إذا كان حرف الفلاش مختلفًا:

```python
USB_KEY_PATH = "E:/usb.key"   # غيّري حرف الفلاشة عندك
```

**كيفية الاستخدام داخل الواجهة:**
- أدخل **كلمة المرور** في الحقل ثم اضغط `Unlock` بعد توصيل فلاش USB (وموجود فيه `usb.key`).
- بعد فتح التطبيق يمكنك استخدام `Encrypt File` و`Decrypt File` لاختيار ملف وتطبيق العملية.
- اضغط `Lock` لقفل التطبيق يدوياً. التطبيق سيقفل أوتوماتيكياً عند إزالة الفلاش.

**ملاحظات أمان مهمة:**
- لا تستخدم كلمات مرور ضعيفة. الأمان يعتمد على كلمة المرور ومحتوى `usb.key` معًا.
- احتفظ بنسخة احتياطية من `usb.key` في مكان آمن إذا فقدت الفلاش فلن تتمكن من فك ملفاتك المشفّرة.
- الملف يجري استبداله بالنسخة المشفّرة عند التشفير—أجرِ نسخاً احتياطية قبل التجربة إن لزم.

**سجل النشاطات:**
- الأنشطة تُسجَّل في `activity.log` داخل مجلد المشروع.

**المساهمة:**
- تحسين تجربة المستخدم، إضافة دعم لتشفير مجلدات، أو إضافة خيار لفصل الملفات المشفّرة عن الملف الأصلي مرحب بها.

**الرخصة:**
- حرّ المشروع للاستخدام الشخصي والتعليمي. أضف رخصة واضحة إذا تريد نشره عامّاً.

---
إن أردت، أقدر أضيف مثال سكربت صغير لإنشاء `usb.key` تلقائياً أو ملف `requirements.txt`، أو أترجم الملف للإنجليزية أيضاً.

**أوامر مساعدة وملفات إضافية**
- أضفت ملف `requirements.txt` وملفين لإنشاء `usb.key`:
	- `create_usb_key.py` (بايثون)
	- `create_usb_key.ps1` (PowerShell)
- لتثبيت الحزم بسرعة استخدم:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- لإنشاء `usb.key` باستخدام السكربت بايثون (مثال مع الفلاش على حرف `E:`):

```powershell
python create_usb_key.py --drive E:
```

- أو باستخدام سكربت PowerShell (كمسؤول أو من موجه PowerShell):

```powershell
.\create_usb_key.ps1 -Drive 'E:'
```

تأكد من تعديل `USB_KEY_PATH` في `secure_encryptor_gui.py` إذا كان حرف محرك الفلاش مختلفاً.

**بناء ملف exe قابل للتشغيل (Windows)**
- أضفت سكربتين لمساعدتك على بناء exe محلياً: `build_exe.ps1` و`build_exe.bat`.
- المتطلبات: Python + `pip install -r requirements.txt` (يشتمل على `pyinstaller`).
- لبناء EXE شغّل (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\build_exe.ps1
```

- أو من موجه أوامر Windows (cmd):

```bat
\.venv\Scripts\activate.bat
pip install -r requirements.txt
build_exe.bat
```

- بعد نجاح البناء ستجد الملف التنفيذي في المجلد `dist\SecureEncryptor.exe`.
- ملاحظة: لا يمكنني إضافة ملف exe مضغوط هنا تلقائياً — السكربتات توفر طريقة سهلة لبناءه محلياً على جهازك.

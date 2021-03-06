"""
    配置
"""

sentry_dsn = ""

sender = ""
email_password = ""
receiver = ""

# crawler
AREA = "china/beijing/chaoyang-district"

# image
IMAGE_FILE_PATH = ""
XINGZUOWU_URL = "https://www.xzw.com/fortune/cancer/"
ONE_URL = "http://wufazhuce.com/"

# says
HITOKOTO_URL = "https://v1.hitokoto.cn/?type=b"
JINRISHICI_URL = "https://v1.jinrishici.com/shuqing/aiqing"

# custom says
CONTENT_TITLE = ""
EMAIL_SUBJECT = "嘿"

# DB
DB_PATH = "music.db"

try:
    from local_settings import *
except ImportError:
    pass

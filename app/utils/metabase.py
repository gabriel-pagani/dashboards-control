import jwt
import time
import os
import dotenv

dotenv.load_dotenv()


def generate_dashboard_url(dashboard_id):
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": {},
        "exp": round(time.time()) + (60)
    }

    token = jwt.encode(payload, os.getenv(
        'METABASE_SECRET_KEY'), algorithm="HS256")

    url = f"{os.getenv('METABASE_SITE_URL')}/embed/dashboard/{token}#bordered=true&titled=true"

    return url

import requests
from datetime import datetime

SUPABASE_URL = "https://lksnivjjkxqlsogrlxon.supabase.co/functions/v1/validate-license"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxrc25pdmpqa3hxbHNvZ3JseG9uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg2NTk1NjMsImV4cCI6MjA3NDIzNTU2M30.Jw_iCkb5UilWnvx5UZUoamgo9-dgS4TgXnk-Bv-f-zo"

class LicenseValidator:
    @staticmethod
    def validate_license(tier, license_key):
        if tier == 'community':
            return True
        
        try:
            # Intenta validación remota
            response = requests.post(
                f"https://{SUPABASE_URL}/functions/v1/validate-license",
                json={'license_key': license_key},
                headers={'Authorization': f'Bearer {SUPABASE_ANON_KEY}'},
                timeout=3
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('valid', False)
        except:
            pass
        
        # Fallback offline
        try:
            parts = license_key.split('-')
            year, month, day = int(parts[1]), int(parts[2]), int(parts[3])
            expiry = datetime(year, month, day)
            return datetime.now() <= expiry
        except:
            return False
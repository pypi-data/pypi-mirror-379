# license_validator.py

import os
import requests
from datetime import datetime

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")

class LicenseValidator:
    @staticmethod
    # <-- MEJORA 1: Añadir el parámetro 'sdk_name'
    def validate_license(tier: str, license_key: str, sdk_name: str) -> bool:
        """
        Valida una licencia para un SDK específico.
        """
        if tier == 'community':
            return True

        if not SUPABASE_URL or not SUPABASE_ANON_KEY:
            print("Warning: Validation server credentials not configured. Using offline validation only.")
            return LicenseValidator._offline_validate(tier, license_key)

        try:
            headers = {
                'apikey': SUPABASE_ANON_KEY,
                'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
            }
            
            # <-- MEJORA 2: Incluir 'sdk_name' en el cuerpo de la petición
            json_payload = {
                'license_key': license_key,
                'sdk_name': sdk_name 
            }
            
            response = requests.post(
                f"https://{SUPABASE_URL}/functions/v1/validate-license",
                json=json_payload,
                headers=headers,
                timeout=5
            )
            
            response.raise_for_status()
            
            data = response.json()
            return data.get('valid', False)

        except requests.exceptions.RequestException:
            print("Warning: Could not connect to validation server. Attempting offline check.")
            return LicenseValidator._offline_validate(tier, license_key)

    @staticmethod
    def _offline_validate(tier: str, license_key: str) -> bool:
        # La validación offline no puede verificar el SDK, pero mantiene la funcionalidad básica.
        if not license_key:
            return False
            
        try:
            parts = license_key.split('-')
            if len(parts) < 4: return False
                
            tier_prefix = parts[0]
            if (tier == 'professional' and tier_prefix != 'PRO') or \
               (tier == 'enterprise' and tier_prefix != 'ENT'):
                return False

            year, month, day = int(parts[1]), int(parts[2]), int(parts[3])
            expiry_date = datetime(year, month, day, 23, 59, 59)
            return datetime.now() <= expiry_date
        except (ValueError, IndexError):
            return False
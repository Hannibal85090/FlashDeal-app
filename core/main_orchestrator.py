from security_engine import FlashDealSecurityEngine
from voice_processor import FlashDealVoiceProcessor

class FlashDealOrchestrator:
    """
    FlashDeal Main Orchestrator (The Brain):
    المنسق العام الذي يربط الصوت بالأمان لضمان تنفيذ الشعار:
    Talk. Pay. Done.
    """
    def __init__(self):
        self.security = FlashDealSecurityEngine()
        self.voice = FlashDealVoiceProcessor()

    def run_transaction_flow(self):
        # 1. المرحلة الأولى: Talk (الاستماع للأمر)
        command_text = self.voice.capture_command()
        tx_data = self.voice.parse_command(command_text)
        
        self.voice.notify_user(f"تم استقبال طلب: {tx_data['action']} {tx_data['amount']} {tx_data['currency']}")

        # 2. المرحلة الثانية: Security (المصادقة الثلاثية)
        self.voice.notify_user("يرجى تأكيد الهوية (صوت، وجه، حركة)...")
        
        # محاكاة لبيانات حيوية ناجحة
        success, token = self.security.execute_triple_auth("v_data", "f_data", "m_data")

        if success:
            # 3. المرحلة الثالثة: Done (توليد التوكن النهائي للتنفيذ)
            self.voice.notify_user(f"تمت المصادقة بنجاح! التوكن المتبادل: {token}")
            self.voice.notify_user("العملية مكتملة. Pay. Done.")
            return True
        else:
            self.voice.notify_user("فشلت المصادقة. تم إلغاء العملية لأسباب أمنية.")
            return False

# لتشغيل النظام بالكامل:
if __name__ == "__main__":
    flash_deal = FlashDealOrchestrator()
    flash_deal.run_transaction_flow()


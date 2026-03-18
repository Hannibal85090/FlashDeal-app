# تعديل الاستدعاءات لضمان عملها داخل بيئة Streamlit و GitHub
try:
    # المحاولة الأولى: الاستدعاء من داخل مجلد core (للعمل عبر app_interface.py)
    from core.security_engine import FlashDealSecurityEngine
    from core.voice_processor import FlashDealVoiceProcessor
except ModuleNotFoundError:
    # المحاولة الثانية: الاستدعاء المباشر (للتشغيل المحلي أو الاختبارات)
    from security_engine import FlashDealSecurityEngine
    from voice_processor import FlashDealVoiceProcessor

class FlashDealOrchestrator:
    """
    FlashDeal Main Orchestrator (The Brain):
    المنسق العام الذي يربط الصوت بالأمان لضمان تنفيذ الشعار:
    Talk. Pay. Done.
    """
    def __init__(self):
        # إنشاء نسخ من المحركات الأمنية والصوتية
        self.security = FlashDealSecurityEngine()
        self.voice = FlashDealVoiceProcessor()

    def run_transaction_flow(self):
        # 1. المرحلة الأولى: Talk (الاستماع للأمر وتحليله)
        command_text = self.voice.capture_command()
        tx_data = self.voice.parse_command(command_text)
        
        # إشعار المستخدم باستلام الطلب المالي
        self.voice.notify_user(f"تم استقبال طلب: {tx_data['action']} {tx_data['amount']} {tx_data['currency']}")

        # 2. المرحلة الثانية: Security (المصادقة الثلاثية البيومترية)
        self.voice.notify_user("🔒 جاري بدء المصادقة الثلاثية لـ FlashDeal Star...")
        self.voice.notify_user("يرجى تأكيد الهوية (صوت + وجه + حركة)...")
        
        # تنفيذ بروتوكول الأمان وتوليد التوكن المتبادل
        success, token = self.security.execute_triple_auth("v_data", "f_data", "m_data")

        if success:
            # 3. المرحلة الثالثة: Done (إتمام العملية بنجاح)
            self.voice.notify_user(f"✅ تمت المصادقة بنجاح! التوكن المتبادل: {token}")
            self.voice.notify_user("✨ العملية مكتملة وآمنة. Pay. Done.")
            return True
        else:
            # في حالة فشل أي طبقة أمنية
            self.voice.notify_user("⚠️ فشلت المصادقة. تم إلغاء العملية فوراً لحماية حسابك.")
            return False

# اختبار النظام داخلياً
if __name__ == "__main__":
    flash_deal = FlashDealOrchestrator()
    flash_deal.run_transaction_flow()

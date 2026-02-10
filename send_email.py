import os
import django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

# 1. EMAIL CONFIGURATION
if not settings.configured:
    settings.configure(
        DEBUG=True,
        EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
        EMAIL_HOST='smtp.gmail.com',
        EMAIL_PORT=587,
        EMAIL_USE_TLS=True,
        EMAIL_HOST_USER='rajagokilavivek@gmail.com', 
        EMAIL_HOST_PASSWORD='eaaw smdg xdtz gnhv', 
    )
django.setup()

def send_invitation():
    husband_email = "rajagokilab@gmail.com"
    
    # 🔴 PASTE THE LINK YOU GOT FROM THE BLACK TERMINAL HERE 🔴
    # It should look like: "https://v4-123-xyz.localhost.run"
    # Ensure there are NO spaces inside the quotes!
    magic_link = "https://cf990e90a6f2d1e2-78-82-28-27.serveousercontent.com"
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body style="background-color: #fce7f3; font-family: sans-serif; text-align: center; padding: 40px;">
        <div style="background: white; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h1 style="color: #db2777;">I have a question... 💌</h1>
            <p style="font-size: 18px; color: #555;">I coded a special surprise for you.<br>Promise to answer honestly!</p>
            <a href="{magic_link}" style="display: inline-block; background-color: #e11d48; color: white; padding: 16px 32px; text-decoration: none; border-radius: 50px; font-weight: bold; font-size: 18px; margin-top: 25px;">Tap to Open ❤️</a>
        </div>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject="For my Valentine... 💌", body="Open this email!", from_email=settings.EMAIL_HOST_USER, to=[husband_email])
    msg.attach_alternative(html_content, "text/html")
    
    try:
        msg.send()
        print("✅ SUCCESS! Email sent.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    send_invitation()
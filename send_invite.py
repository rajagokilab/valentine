import os
import django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

# 1. CONFIGURE SETTINGS
# We check if settings are already configured to avoid errors if you run it twice.
if not settings.configured:
    settings.configure(
        DEBUG=True,
        # EMAIL CONFIGURATION
        EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
        EMAIL_HOST='smtp.gmail.com',
        EMAIL_PORT=587,
        EMAIL_USE_TLS=True,
        EMAIL_HOST_USER='rajagokilavivek@gmail.com', 
        
        # 🔴 PASTE YOUR APP PASSWORD BELOW (The one starting with 'eaaw...')
        EMAIL_HOST_PASSWORD='eaaw smdg xdtz gnhv', 
        
        # TEMPLATE CONFIGURATION (This fixes the error you had!)
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
            'OPTIONS': {},
        }],
    )

# 2. INITIALIZE DJANGO
django.setup()

def send_valentine():
    # --- CUSTOMIZE THESE DETAILS ---
    husband_email = "rajagokilab@gmail.com"  # <--- PUT HUSBAND'S EMAIL HERE
    
    # I added a cute GIF as a placeholder. You can replace this link with your own photo!
    hero_image_url = "https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif"
    
    # Replace this with your YouTube or Drive link
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    
    # Your Phone Number for the "Yes" button SMS
    # my_phone_number = "123456789"

    # --- THE HTML EMAIL DESIGN ---
    html_template_string = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Question for You ❤️</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            background-color: #fce7f3; /* Pink-100 */
            font-family: 'Georgia', serif;
            overflow: hidden; /* Prevent scrolling when button moves */
        }
        .btn-transition {
            transition: all 0.3s ease;
        }
    </style>
</head>
<body class="h-screen flex flex-col items-center justify-center relative">

    <div id="main-card" class="text-center z-10 p-8 bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl border border-pink-200 max-w-md mx-4">
        
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDdtZ2JiZDR0a3czb3Z2Z3Ftc2Y5Z3Ftc2Y5Z3Ftc2Y5Z3Ftc2Y5Z3Ftc2Y5ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/3o7TKoWXm3okO1kgHC/giphy.gif" 
             alt="Cute Heart" 
             class="w-32 h-32 mx-auto mb-6 object-cover rounded-full border-4 border-pink-500 shadow-lg">

        <h1 class="text-4xl text-pink-700 font-bold mb-4">Will you be my Valentine?</h1>
        <p class="text-gray-600 mb-8 text-lg">Please say yes... 🥺</p>

        <div class="flex justify-center gap-4 relative h-16">
            <button onclick="playVideo()" 
                    class="bg-pink-600 hover:bg-pink-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transform hover:scale-110 transition duration-200 z-20">
                YES! ❤️
            </button>

            <button id="no-btn" 
                    class="bg-gray-400 hover:bg-gray-500 text-white font-bold py-3 px-8 rounded-full shadow-lg absolute transition-all duration-300 ease-out"
                    style="left: 60%;">
                No
            </button>
        </div>
    </div>

    <div id="video-modal" class="fixed inset-0 bg-black/90 hidden z-50 flex items-center justify-center p-4">
        <div class="w-full max-w-4xl bg-black rounded-lg overflow-hidden shadow-2xl relative">
            
            <button onclick="closeVideo()" class="absolute top-4 right-4 text-white text-2xl font-bold z-50 hover:text-pink-500">&times;</button>
            
            <div class="aspect-video w-full">
                <iframe id="youtube-frame"
                        class="w-full h-full"
                        src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" 
                        title="Valentine Video" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen>
                </iframe>
            </div>
            
            <div class="p-6 text-center">
                <h2 class="text-white text-2xl font-bold mb-2">I knew you'd watch it! 😉</h2>
                <p class="text-pink-300">Happy Valentine's Day, my love!</p>
            </div>
        </div>
    </div>

    <script>
        const noBtn = document.getElementById('no-btn');
        const videoModal = document.getElementById('video-modal');
        let attempts = 0;
        const maxAttempts = 4; // Moves 4 times, then gives up

        // Function to move the button randomly
        function moveButton() {
            // Get window dimensions
            const maxX = window.innerWidth - noBtn.offsetWidth - 50;
            const maxY = window.innerHeight - noBtn.offsetHeight - 50;

            // Generate random position
            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY;

            // Apply new position (using fixed positioning to let it fly anywhere on screen)
            noBtn.style.position = 'fixed';
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
        }

        // Interaction Logic
        const handleInteraction = () => {
            attempts++;
            
            if (attempts <= maxAttempts) {
                // Run away!
                moveButton();
            } else {
                // Gave up / Caught
                playVideo();
            }
        };

        // Trigger on hover (desktop) and click (mobile)
        noBtn.addEventListener('mouseover', handleInteraction);
        noBtn.addEventListener('click', handleInteraction);

        // Function to show video
        function playVideo() {
            videoModal.classList.remove('hidden');
            // Optional: You can play confetti animation here too!
        }

        // Function to close video
        function closeVideo() {
            videoModal.classList.add('hidden');
            // Stop video playback by resetting src
            const iframe = document.getElementById('youtube-frame');
            const currentSrc = iframe.src;
            iframe.src = '';
            iframe.src = currentSrc;
        }
    </script>
</body>
</html>
    """

    # --- RENDER AND SEND ---
    print("🎨 Rendering email template...")
    template = Template(html_template_string)
    context = Context({
        'hero_image': hero_image_url,
        'video_link': video_url,
        # 'phone_number': my_phone_number
    })
    html_content = template.render(context)
    
    subject = "A Special Question for You... 💌"
    from_email = settings.EMAIL_HOST_USER
    to_email = [husband_email]

    msg = EmailMultiAlternatives(subject, "Please view this email in a modern email client.", from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    
    print(f"🚀 Sending email to {husband_email}...")
    try:
        msg.send()
        print("✅ SUCCESS! Email sent successfully.")
    except Exception as e:
        print(f"❌ ERROR: Could not send email. Details:\n{e}")

if __name__ == "__main__":
    send_valentine()
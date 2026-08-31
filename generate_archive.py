import os
from pathlib import Path

# Base structure of archive.html
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Archive - Ratgal Janamastami 2026</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        .lang-en {{ display: none; }}
        .lang-hi {{ display: inline; }}
        body.lang-english .lang-en {{ display: inline; }}
        body.lang-english .lang-hi {{ display: none; }}
        /* Masonry Grid */
        .masonry {{
            column-count: 2;
            column-gap: 1rem;
        }}
        @media (min-width: 768px) {{
            .masonry {{ column-count: 3; }}
        }}
        @media (min-width: 1024px) {{
            .masonry {{ column-count: 4; }}
        }}
        .masonry-item {{
            break-inside: avoid;
            margin-bottom: 1rem;
        }}
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans overflow-x-hidden w-full">

    <!-- Header / Navigation -->
    <header class="w-full bg-gradient-to-r from-red-600 to-orange-500 text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-2 hover:text-yellow-200 transition">
                <i class="fa-solid fa-arrow-left text-xl"></i>
                <span class="font-bold text-lg hidden sm:block">Back to Home</span>
            </a>
            
            <h1 class="text-2xl md:text-3xl font-extrabold tracking-wide text-center flex-1">
                EVENT ARCHIVE
            </h1>

            <div class="flex items-center gap-3">
                <button onclick="toggleLanguage()" class="bg-white/20 hover:bg-white/30 px-3 py-1 rounded-full text-sm font-semibold transition flex items-center gap-1">
                    <i class="fa-solid fa-language"></i> <span id="langBtnText">A/अ</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="w-[95%] max-w-[2400px] mx-auto px-4 py-12">
        
        <!-- Header Title -->
        <div class="text-center mb-12">
            <h2 class="text-4xl font-bold text-gray-800 inline-block border-b-4 border-red-500 pb-2 mb-4">
                <span class="lang-hi">पुरानी यादें (Archive)</span>
                <span class="lang-en">Past Memories (Archive)</span>
            </h2>
            <p class="text-gray-600 text-lg max-w-2xl mx-auto">
                <span class="lang-hi">पिछले आयोजनों की शानदार झलकियां, वीडियोज़ और आधिकारिक बुकलेट।</span>
                <span class="lang-en">Glimpses, videos, and official booklets from our past events.</span>
            </p>
        </div>

        <!-- Official Booklet Download Section -->
        <section class="bg-white rounded-3xl shadow-xl overflow-hidden mb-16 border-2 border-gray-100 flex flex-col md:flex-row max-w-5xl mx-auto">
            <div class="bg-red-50 p-8 md:w-1/3 flex flex-col items-center justify-center text-center">
                <i class="fa-solid fa-file-pdf text-6xl text-red-500 mb-4"></i>
                <h3 class="text-2xl font-bold text-gray-800 mb-2">Event Booklet 2025</h3>
                <p class="text-gray-500 font-semibold mb-6">Read the full story & information</p>
            </div>
            <div class="p-8 md:w-2/3 flex flex-col justify-center items-center md:items-start bg-gray-50">
                <p class="text-gray-700 text-lg mb-6 text-center md:text-left">
                    Download the official booklet containing all the details from our 2025 event, including our Janmashtami and Dussehra celebrations, from preparation to the Chief Guest and more.
                </p>
                <a href="ratgal-events-2025.pdf" target="_blank" class="inline-flex items-center gap-2 bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition transform hover:scale-105 text-lg">
                    <i class="fa-solid fa-download"></i> Download PDF
                </a>
            </div>
        </section>

        <!-- 2025 ARCHIVE -->
        <div class="text-center mb-10 mt-20">
            <h2 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-orange-500 mb-4">2025 EVENT MEMORIES</h2>
            <p class="text-gray-500 font-semibold text-lg">A journey through our amazing Janamastami celebration</p>
            <div class="mt-4 border-t-2 border-dashed border-gray-300 w-1/2 mx-auto"></div>
        </div>

        {sections_2025}

        <!-- 2024 ARCHIVE -->
        <div class="text-center mb-10 mt-24">
            <h2 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-yellow-500 mb-4">2024 EVENT MEMORIES</h2>
            <p class="text-gray-500 font-semibold text-lg">Where it all began...</p>
            <div class="mt-4 border-t-2 border-dashed border-gray-300 w-1/2 mx-auto"></div>
        </div>

        {sections_2024}

    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-8 text-center mt-12">
        <p class="mb-2">Made with <i class="fa-solid fa-heart text-red-500 mx-1 animate-pulse"></i> by <strong><span class="lang-en">PRINCE SAINI / RATGAL YUVA SANGH</span> <span class="lang-hi">Prince Saini / रतगल युवा संघ</span></strong></p>
        <p class="text-sm">RATGAL JANAMASHTAMI 2026</p>
    </footer>

    <!-- Scripts -->
    <script>
        // Language Toggle Logic
        let isEnglish = false;
        function toggleLanguage() {{
            isEnglish = !isEnglish;
            if(isEnglish) {{
                document.body.classList.add('lang-english');
            }} else {{
                document.body.classList.remove('lang-english');
            }}
        }}

        // Lazy load video metadata to prevent browser crashing while still showing thumbnails
        document.addEventListener("DOMContentLoaded", function() {{
            let videoObserver = new IntersectionObserver(function(entries, observer) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        let video = entry.target;
                        if(video.preload !== "metadata") {{
                            video.preload = "metadata";
                        }}
                        // Stop observing once metadata is set
                        observer.unobserve(video);
                    }}
                }});
            }}, {{ rootMargin: "200px" }});

            document.querySelectorAll("video").forEach(function(video) {{
                videoObserver.observe(video);
            }});
        }});
    </script>
</body>
</html>
"""

def generate_section(title, folder_path, is_2025=True):
    videos = []
    images = []
    
    if os.path.exists(folder_path):
        for root, _, files in os.walk(folder_path):
            for file in files:
                ext = file.lower().split('.')[-1]
                # Convert backslashes to forward slashes for URLs
                rel_path = os.path.relpath(os.path.join(root, file), start="p:/hash-lab/testproject").replace("\\", "/")
                if ext in ['mp4', 'mov', 'webm']:
                    videos.append(rel_path)
                elif ext in ['jpg', 'jpeg', 'png', 'gif']:
                    images.append(rel_path)
                    
    if not videos and not images:
        return ""

    html = f'''
        <section class="mb-16 bg-white p-8 rounded-3xl shadow-lg border border-gray-100">
            <div class="flex items-center justify-center gap-3 mb-10">
                <i class="fa-solid fa-star text-3xl text-orange-500"></i>
                <h3 class="text-3xl font-bold text-gray-800 border-b-4 border-orange-500 pb-1">{title}</h3>
            </div>
    '''
    
    if videos:
        col_class = "columns-1 md:columns-2 lg:columns-3"
        if len(videos) == 1:
            col_class = "max-w-3xl mx-auto columns-1"
        elif len(videos) == 2:
            col_class = "columns-1 md:columns-2 max-w-5xl mx-auto"
            
        html += f'<div class="{col_class} gap-6 mb-12 space-y-6">'
        for vid in videos:
            html += f'''
                <div class="break-inside-avoid bg-black rounded-2xl overflow-hidden shadow-lg">
                    <video controls class="w-full h-auto object-cover rounded-xl" preload="metadata">
                        <source src="{vid}" type="video/mp4">
                    </video>
                </div>
            '''
        html += '</div>'
        
    if images:
        html += '<div class="masonry">'
        for img in images:
            html += f'''
                <div class="masonry-item rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300">
                    <img src="{img}" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-500" loading="lazy" alt="{title} Photo">
                </div>
            '''
        html += '</div>'
        
    html += '</section>'
    return html

sections_2025 = ""
sections_2025 += generate_section("Preparation", "p:/hash-lab/testproject/media/2025MEDIA/PREPERATION")
sections_2025 += generate_section("Art & Craft", "p:/hash-lab/testproject/media/2025MEDIA/ART AND CRAFT")
sections_2025 += generate_section("Dahi Handi", "p:/hash-lab/testproject/media/2025MEDIA/DAHI HANDI")
sections_2025 += generate_section("Dahi Handi Team Competition", "p:/hash-lab/testproject/media/2025MEDIA/DAHI HANDI TEAM COMPETITION")

sections_2024 = generate_section("2024 Highlights", "p:/hash-lab/testproject/media/2024MEDIA", is_2025=False)

final_html = HTML_TEMPLATE.format(sections_2025=sections_2025, sections_2024=sections_2024)

with open("p:/hash-lab/testproject/archive.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("archive.html generated successfully!")

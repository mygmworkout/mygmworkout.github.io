import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix frame() so that animations play if they exist, even if img is present
frame_old = '''      if (ex.img) {
        stageEl.style.display = "none";
        imgEl.style.display = "block";
        imgEl.src = ex.img;
      } else {
        stageEl.style.display = "block";
        imgEl.style.display = "none";
        scene(ex, P);
      }'''
frame_new = '''      if (ex.img && !ex.start && !ex.base) {
        stageEl.style.display = "none";
        imgEl.style.display = "block";
        imgEl.src = ex.img;
      } else {
        stageEl.style.display = "block";
        imgEl.style.display = "none";
        scene(ex, P);
      }'''
html = html.replace(frame_old, frame_new)

# Dictionary of animations to inject
anims = {
    "rolldown": """pulley: "low", attach: "ha", period: 4, strap: true,
        start: { he: [180, 130], sh: [180, 160], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [220, 190], ha: [270, 210] },
        end: { he: [110, 230], sh: [130, 240], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [220, 220], ha: [270, 240] },""",
    
    "rolldown_bicep": """pulley: "low", attach: "ha", period: 3, strap: true,
        start: { he: [130, 200], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [150, 230], ha: [250, 230] },
        end: { he: [130, 200], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [150, 230], ha: [160, 180] },""",
        
    "rolldown_row": """pulley: "low", attach: "ha", period: 3, strap: true,
        start: { he: [130, 200], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [200, 230], ha: [260, 240] },
        end: { he: [130, 200], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [120, 230], ha: [160, 230] },""",
        
    "rolldown_twist": """pulley: "low", attach: "ha", attach2: "ha2", period: 3, strap: true,
        start: { he: [130, 200], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [200, 230], ha: [260, 240], el2: [200, 230], ha2: [260, 240] },
        end: { he: [140, 190], sh: [140, 220], hi: [180, 260], kn: [280, 260], fo: [350, 260], el: [120, 230], ha: [160, 230], el2: [200, 230], ha2: [260, 240] },""",
        
    "supine_scissors": """pulley: "low", attach: "fo", attach2: "fo2", period: 3, strap: true,
        start: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [240, 180], fo: [240, 120], kn2: [280, 230], fo2: [320, 210] },
        end: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [280, 230], fo: [320, 210], kn2: [240, 180], fo2: [240, 120] },""",
        
    "parallel_press": """pulley: "low", attach: "fo", attach2: "fo2", period: 3, strap: true,
        start: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [240, 200], fo: [290, 200], kn2: [240, 200], fo2: [290, 200] },
        end: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [280, 250], fo: [340, 240], kn2: [280, 250], fo2: [340, 240] },""",
        
    "lying_alt_press": """pulley: "low", attach: "fo", attach2: "fo2", period: 3, strap: true,
        start: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [240, 200], fo: [290, 200], kn2: [240, 200], fo2: [290, 200] },
        end: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [280, 250], fo: [340, 240], kn2: [240, 200], fo2: [290, 200] },""",
        
    "supine_helicopter": """pulley: "low", attach: "fo", attach2: "fo2", period: 3, strap: true,
        start: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [240, 180], fo: [240, 120], kn2: [280, 230], fo2: [320, 210] },
        end: { he: [100, 260], sh: [140, 260], hi: [240, 260], kn: [280, 230], fo: [320, 210], kn2: [240, 180], fo2: [240, 120] },""",
        
    "breaststroke_armlift": """pulley: "low", attach: "ha", attach2: "ha2", period: 4, strap: true, bench: true,
        start: { he: [100, 150], sh: [140, 150], hi: [250, 150], kn: [288, 150], fo: [320, 150], el: [140, 180], ha: [180, 180], el2: [140, 180], ha2: [180, 180] },
        end: { he: [100, 130], sh: [140, 140], hi: [250, 150], kn: [288, 150], fo: [320, 150], el: [100, 140], ha: [60, 140], el2: [100, 140], ha2: [60, 140] },"""
}

for ex_id, anim_data in anims.items():
    # Insert anim_data right after img: "img/IMG_XXXX.jpg",
    pattern = r'(id:\s*"' + ex_id + r'".*?img:\s*"img/IMG_\d+\.jpg",)'
    replacement = r'\1\n        ' + anim_data
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

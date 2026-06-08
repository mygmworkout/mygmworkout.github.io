import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CATS
html = html.replace(
    'const cats = [["cable", "Cable Strength"], ["strap", "Pilates — Straps & Cable"], ["stretch", "Stretch & Mobility"]];',
    'const cats = [["mat", "Mat/Reformer (Core & Mobility)"], ["fullbody", "Full Body"], ["cable", "Cable Strength"]];'
)
html = html.replace(
    'const CATS = [["strap", "Pilates Straps"], ["cable", "Cable Strength"], ["stretch", "Stretch & Mobility"]];',
    'const CATS = [["mat", "Mat/Reformer (Core & Mobility)"], ["fullbody", "Full Body"], ["cable", "Cable Strength"]];'
)
html = html.replace('let idx = 7, cat = "strap",', 'let idx = 7, cat = "mat",')

# 2. Add stageImg to HTML
stage_html = '''<canvas id="stage" width="480" height="320" aria-label="Exercise animation"></canvas>'''
stageImg_html = '''<canvas id="stage" width="480" height="320" aria-label="Exercise animation"></canvas>
        <img id="stageImg" style="display:none; width: 100%; border-radius: 8px; border: 1px solid #00000020; max-height: 320px; object-fit: contain;">'''
html = html.replace(stage_html, stageImg_html)

# 3. Update frame() for image logic
frame_old = '''const P = joints(ex, p), t = tphase(ex, p);
      scene(ex, P);
      document.getElementById("ringI").style.transform = `scale(${0.5 + 0.55 * t})`;'''

frame_new = '''const P = joints(ex, p), t = tphase(ex, p);
      const stageEl = document.getElementById("stage");
      const imgEl = document.getElementById("stageImg");
      if (ex.img) {
        stageEl.style.display = "none";
        imgEl.style.display = "block";
        imgEl.src = ex.img;
      } else {
        stageEl.style.display = "block";
        imgEl.style.display = "none";
        scene(ex, P);
      }
      document.getElementById("ringI").style.transform = `scale(${0.5 + 0.55 * t})`;'''
html = html.replace(frame_old, frame_new)

# 4. Update snapshot() for print sheet
snap_old = '''function snapshot(ex) {
      const off = document.createElement("canvas"); off.width = 480; off.height = 320;'''
snap_new = '''function snapshot(ex) {
      if (ex.img) return ex.img;
      const off = document.createElement("canvas"); off.width = 480; off.height = 320;'''
html = html.replace(snap_old, snap_new)

# 5. Change categories in existing EX array
cat_map = {
    'footwork': 'fullbody',
    'circles': 'mat',
    'scissors': 'mat',
    'slstretch': 'mat',
    'hundred': 'mat',
    'armpull': 'fullbody',
    'butterfly': 'mat',
    'punch': 'fullbody',
    'feetalt': 'fullbody',
    'feetcurl': 'fullbody',
    'breaststroke': 'mat',
    'breastpress': 'fullbody',
    'child': 'mat',
    'cheststretch': 'mat',
    'hammy': 'mat',
    'glutestretch': 'mat'
}
for k, v in cat_map.items():
    html = re.sub(r'(cat:\s*)"(?:strap|stretch)"(, id:\s*"' + k + '")', r'\g<1>"' + v + '"\g<2>', html)


new_workouts = """
      {
        cat: "mat", id: "rolldown", name: "Roll Down Round Back", focus: "Core & Mobility",
        sub: "Relax the shoulders and neck. Keep the legs together, extended and locked.",
        setup: { Height: "Low port", Attach: "Handles", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1771.jpg",
        steps: [
          "Exhale, draw the navel toward the spine, tuck the pelvis, and roll backward from the tailbone to form a C-curve in the spine.",
          "Continue rolling the spine down, one vertebra at a time, until lying flat on the mat; keep the feet pressed into the mat, avoiding lifting or rocking.",
          "Use abdominal engagement to roll the body back up, stacking the spine sequentially to return to a tall, seated position."
        ]
      },
      {
        cat: "fullbody", id: "rolldown_bicep", name: "Roll Down with Bicep Curls", focus: "Core & Arms",
        sub: "Extend the legs forward. Keep the torso in a stable C-curve—avoid rocking.",
        setup: { Height: "Low port", Attach: "Handles", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1772.jpg",
        steps: [
          "Exhale, keep the torso in a C-curve, bend the elbows, and pull them backward; keep the upper arms stable.",
          "Inhale, resist the cable tension, and slowly extend the arms back to the starting position—avoid letting the cable pull them back too quickly."
        ]
      },
      {
        cat: "fullbody", id: "rolldown_row", name: "Roll Down with Row", focus: "Core & Back",
        sub: "Extend both legs straight forward, together and locked. Lean the torso back about 45°.",
        setup: { Height: "Low port", Attach: "Handles", Mode: "Free Lift · Constant", Load: "Blue spring · 10–12 lb/side" },
        img: "img/IMG_1773.jpg",
        steps: [
          "Exhale. Maintain a stable C-curve in the torso and bend the elbows to pull back horizontally.",
          "Inhale. Slowly extend the arms back to the starting position against the cable resistance, avoiding a quick snap back."
        ]
      },
      {
        cat: "mat", id: "rolldown_twist", name: "Roll Down with Twist Row", focus: "Core, Back & Mobility",
        sub: "Lean the torso back about 45°, supported on the sacrum. Raise the arms to shoulder height.",
        setup: { Height: "Low port", Attach: "Handles", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1775.jpg",
        steps: [
          "Roll the torso down and lean back to about 45°, supported and stable. Exhale as you bend the right elbow and pull back, rotating the head and thoracic spine to look to the right. Inhale to return to center.",
          "Exhale to pull back with the left elbow, rotating the thoracic spine to look left. Inhale to slowly return the straps. Alternate sides."
        ]
      },
      {
        cat: "mat", id: "supine_scissors", name: "Supine Leg Scissors", focus: "Core",
        sub: "Keep the pelvis stable, with the lower back pressed gently into the mat.",
        setup: { Height: "Low port", Attach: "Ankle straps", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1776.jpg",
        steps: [
          "Lie on your back with your core engaged and both legs lifted about 30° off the floor. Inhale to prepare; exhale as one leg extends upward toward the ceiling while the other lowers with control toward the floor.",
          "Inhale as the legs switch positions in the air, maintaining length and control, continuing the scissor-like alternation.",
          "Optionally, flex the toes upward or point them downward to increase activation of the posterior or anterior leg muscles."
        ]
      },
      {
        cat: "fullbody", id: "parallel_press", name: "Parallel Press", focus: "Legs",
        sub: "Press the lower back into the mat and lengthen the spine away from the tailbone.",
        setup: { Height: "Low port", Attach: "Ankle straps", Mode: "Free Lift · Constant", Load: "Red spring · 15–22 lb/side" },
        img: "img/IMG_1777.jpg",
        steps: [
          "Lie on your back in tabletop position, keeping the legs together and core engaged. Exhale as you extend the legs and lower them toward the floor, keeping them close to the ground.",
          "Inhale, flexing the hips to lift the legs back up to the bent-knee, bent-hip position.",
          "Keep the core engaged and stable, moving with a smooth, controlled rhythm; avoid using momentum."
        ]
      },
      {
        cat: "fullbody", id: "lying_alt_press", name: "Lying Alternating Leg Press", focus: "Legs",
        sub: "Keep the pelvis stable, with the lower back pressed close to the mat.",
        setup: { Height: "Low port", Attach: "Ankle straps", Mode: "Free Lift · Constant", Load: "Red spring · 15–22 lb/side" },
        img: "img/IMG_1778.jpg",
        steps: [
          "Lie on your back in a table-top position, with the arms relaxed at your sides. Keep the pelvis stable and pressed into the mat. Inhale to prepare.",
          "Exhale and extend one leg downward, lowering it to about 45° or slightly below, while keeping the lumbar spine and torso stable.",
          "Inhale, engaging the core and hips to control the leg as it returns. Exhale and repeat on the other side, alternating legs."
        ]
      },
      {
        cat: "mat", id: "supine_helicopter", name: "Supine Leg Helicopter", focus: "Core & Mobility",
        sub: "Keep the pelvis stable, with the lower back gently pressed into the mat.",
        setup: { Height: "Low port", Attach: "Ankle straps", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1779.jpg",
        steps: [
          "Inhale to prepare while lying on your back, engaging the core and lifting both legs about 30° off the floor.",
          "Exhale as you perform the scissor legs: one leg rises toward vertical while the other lowers with control.",
          "Inhale as the legs switch positions in the air, completing the second scissor.",
          "Exhale: when the legs reach their farthest points, open them outward in a circular motion; inhale to bring them back together along the scissor path and continue the movement."
        ]
      },
      {
        cat: "fullbody", id: "breaststroke_armlift", name: "Breaststroke Arm Lift", focus: "Back & Core",
        sub: "Keep the neck neutral and extended, with shoulders down. Engage the abdominal muscles.",
        setup: { Height: "Low port", Attach: "Handles + Bench", Mode: "Free Lift · Constant", Load: "Yellow spring · 4–7 lb/side" },
        img: "img/IMG_1780.jpg",
        steps: [
          "Inhale. Start with the arms naturally bent at the sides of the waist. Exhale, engage the shoulders and arms to push the arms straight overhead.",
          "Inhale. Keep the shoulders and back engaged, control the arms as they open out to the sides at shoulder height, feeling the eccentric stretch.",
          "Exhale. Engage the shoulders to lift the arms overhead. Inhale, control the lowering back to shoulder height."
        ]
      },
"""
html = html.replace('/* ============ PILATES STRAPS ============ */', '/* ============ PILATES STRAPS ============ */\n' + new_workouts)

feetalt_new = '''{
        cat: "fullbody", id: "feetalt", name: "Feet Pulling Alternation", focus: "Pilates · Hamstrings",
        sub: "Keep the spine neutral and the pelvis stable. Keep the thighs stable and pressed against the mat.",
        setup: { Height: "High port", Attach: "Ankle straps + bench", Mode: "Free Lift · Constant", Load: "Blue spring · 10–12 lb/side" },
        img: "img/IMG_1783.jpg",
        pulley: "high", attach: "fo", attach2: "fo2", period: 2.6, ringFrom: .5, strap: true, bench: true,
        start: { he: [92, 150], sh: [140, 150], hi: [250, 150], kn: [288, 150], fo: [300, 104], kn2: [288, 156], fo2: [270, 106] },
        end: { he: [92, 150], sh: [140, 150], hi: [250, 150], kn: [288, 150], fo: [266, 100], kn2: [288, 156], fo2: [306, 110] },
        steps: [
          "Lie prone with the pelvis stable on the mat and the abdominals lightly engaged. Keep the legs together, knees bent at about 90° pointing toward the ceiling. Inhale to prepare.",
          "Exhale, keeping one leg straight and stable while engaging the hamstring of the other leg to bend the knee, bringing the heel toward the glutes in a controlled manner without rocking the pelvis.",
          "Inhale to return the leg to the starting bent position with control.",
          "Exhale, switch legs, and repeat the single-leg curl, maintaining rhythm and stability."
        ]
      }'''

feetcurl_new = '''{
        cat: "fullbody", id: "feetcurl", name: "Feet Pulling Hamstring Curl", focus: "Pilates · Hamstrings",
        sub: "Keep the spine stable in a neutral position. Keep the core and pelvis stable, maintaining contact with the mat at all times.",
        setup: { Height: "High port", Attach: "Ankle straps + bench", Mode: "Free Lift · Constant", Load: "Blue spring · 10–12 lb/side" },
        img: "img/IMG_1782.jpg",
        pulley: "high", attach: "fo", attach2: "fo2", period: 3, ringFrom: .5, strap: true, bench: true,
        start: { he: [92, 150], sh: [140, 150], hi: [250, 150], kn: [288, 150], fo: [300, 104], kn2: [288, 156], fo2: [306, 110] },
        end: { he: [92, 150], sh: [140, 150], hi: [250, 150], kn: [288, 150], fo: [266, 100], kn2: [288, 156], fo2: [272, 106] },
        steps: [
          "Lie prone with the pelvis stable against the mat and the abdominals lightly engaged. Bring the legs together, bending the knees to about 90° toward the ceiling. Inhale to prepare.",
          "Exhale, keeping one leg straight and stable while the other leg performs a controlled hamstring curl, bringing the heel toward the glutes. Keep the pelvis stable.",
          "Inhale, control the leg as it returns to the starting bent position.",
          "Exhale, switch legs and repeat the single-leg curl, maintaining rhythm and stability."
        ]
      }'''

html = re.sub(r'\{\s*cat:\s*"fullbody",\s*id:\s*"feetalt".*?\},', feetalt_new + ',', html, flags=re.DOTALL)
html = re.sub(r'\{\s*cat:\s*"fullbody",\s*id:\s*"feetcurl".*?\},', feetcurl_new + ',', html, flags=re.DOTALL)

loads = '''rolldown: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      rolldown_bicep: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      rolldown_row: { cables: 2, perSide: [10, 12], spring: "Blue" },
      rolldown_twist: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      supine_scissors: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      parallel_press: { cables: 2, perSide: [15, 22], spring: "Red" },
      lying_alt_press: { cables: 2, perSide: [15, 22], spring: "Red" },
      supine_helicopter: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      breaststroke_armlift: { cables: 2, perSide: [4, 7], spring: "Yellow" },
      '''
html = html.replace('footwork: { cables: 2,', loads + 'footwork: { cables: 2,')

targets = '''rolldown: 10, rolldown_bicep: 10, rolldown_row: 10, rolldown_twist: 10,
      supine_scissors: 10, parallel_press: 12, lying_alt_press: 12, supine_helicopter: 8, breaststroke_armlift: 8,
      '''
html = html.replace('footwork: 12,', targets + 'footwork: 12,')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

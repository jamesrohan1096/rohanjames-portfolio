import base64, os

def b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

profile = b64('/home/claude/photos/profile_warm.jpg')

photo_files = sorted([f for f in os.listdir('/home/claude/photos') 
                      if not f.startswith('profile') and f.endswith('.jpg')])
photos_js = "const PHOTOS = [\n"
for pf in photo_files:
    d = b64(f'/home/claude/photos/{pf}')
    photos_js += f'  {{src: "data:image/jpeg;base64,{d}", name: "{pf[:-4]}"}},\n'
photos_js += "];"

with open('/home/claude/template_v3.html', 'r') as f:
    template = f.read()

html = template.replace('__PROFILE_B64__', profile).replace('__PHOTOS_JS__', photos_js)

with open('/home/claude/rohanjames.html', 'w') as f:
    f.write(html)

print(f"Built! {len(html):,} bytes ({len(html)//1024} KB)")

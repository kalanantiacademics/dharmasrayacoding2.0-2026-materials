import re

file_path = r'c:\prog\dharmasrayacoding2.0-2026-materials\materials-smp\meet5.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add JS functions
zoom_js = '''
        function zoomPan(e, container) {
            const img = container.querySelector('img');
            const rect = container.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const xPercent = (x / rect.width) * 100;
            const yPercent = (y / rect.height) * 100;
            img.style.transformOrigin = `${xPercent}% ${yPercent}%`;
            img.style.transform = "scale(2)";
        }

        function resetZoomPan(container) {
            const img = container.querySelector('img');
            img.style.transformOrigin = "center center";
            img.style.transform = "scale(1)";
        }
    </script>'''
if 'function zoomPan' not in html:
    html = html.replace('</script>', zoom_js, 1)

# 2. Update Image Containers in Slide 16 and 17
def add_zoom_attributes(match):
    style_inner = match.group(1)
    img_inner = match.group(2)
    img_style = match.group(4) if match.group(4) else ''
    img_end = match.group(5) if match.group(5) else ''

    # Add overflow and relative position to container
    new_style = style_inner
    if 'overflow' not in new_style:
        new_style += '; overflow: hidden;'
    if 'position' not in new_style:
        new_style += '; position: relative;'

    # Clean up double semicolons
    new_style = new_style.replace(';;', ';')

    # Add transition to img
    new_img_style = img_style
    if new_img_style:
        if not new_img_style.strip().endswith(';'):
            new_img_style += ';'
        new_img_style += ' transition: transform 0.2s ease-out; transform-origin: center center;'
    else:
        new_img_style = 'transition: transform 0.2s ease-out; transform-origin: center center;'

    # Reconstruct img tag
    if 'style="' in match.group(0):
        new_img = re.sub(r'style="(.*?)"', f'style="{new_img_style}"', match.group(2))
    else:
        # If img doesn't have style attribute
        if '>' in img_inner:
            new_img = img_inner.replace('>', f' style="{new_img_style}">')
        else:
             new_img = img_inner + f' style="{new_img_style}"'

    return f'<div class="img-container" style="{new_style}" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                        {new_img}'

# Slide 16 - Step 1
html = html.replace(
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2);">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/89d8a2a5-9401-4d6a-bde9-3ddef6b72ce5.png" style="max-height: 100%;">\n                        </div>',
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2); overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/89d8a2a5-9401-4d6a-bde9-3ddef6b72ce5.png" style="max-height: 100%; transition: transform 0.2s ease-out; transform-origin: center center;">\n                        </div>'
)

# Slide 16 - Step 2
html = html.replace(
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2);">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b9402fa8-9470-49d4-95d0-e43fb73cd46a.png" style="max-height: 100%;">\n                        </div>',
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2); overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b9402fa8-9470-49d4-95d0-e43fb73cd46a.png" style="max-height: 100%; transition: transform 0.2s ease-out; transform-origin: center center;">\n                        </div>'
)

# Slide 16 - Step 3
html = html.replace(
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2);">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/f8bc1b92-5156-4e4f-89d4-f97b6996e002.png" style="max-height: 100%;">\n                        </div>',
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; background: rgba(0,0,0,0.2); overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                            <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/f8bc1b92-5156-4e4f-89d4-f97b6996e002.png" style="max-height: 100%; transition: transform 0.2s ease-out; transform-origin: center center;">\n                        </div>'
)

# Slide 16 - Character Image Column
html = html.replace(
    '<div class="img-container" style="height: 450px; background: none; border: none;">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/57cf73d5-cfdf-4b87-be67-fb543908caf8.png" style="filter: drop-shadow(0 15px 30px rgba(0,0,0,0.4)); max-height: 100%;">\n                    </div>',
    '<div class="img-container" style="height: 450px; background: none; border: none; overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/57cf73d5-cfdf-4b87-be67-fb543908caf8.png" style="filter: drop-shadow(0 15px 30px rgba(0,0,0,0.4)); max-height: 100%; transition: transform 0.2s ease-out; transform-origin: center center;">\n                    </div>'
)

# Slide 17 - Gerak Acak
html = html.replace(
    '<div class="img-container" style="height: 200px; margin-bottom: 15px;">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/da815c59-f30c-4900-8dfb-c455175136f0.png">\n                    </div>',
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/da815c59-f30c-4900-8dfb-c455175136f0.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;">\n                    </div>'
)

# Slide 17 - Interaksi Makan
html = html.replace(
    '<div class="img-container" style="height: 200px; margin-bottom: 15px;">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/04338bb9-7852-4845-b6e4-f04bab3a4e39.png">\n                    </div>',
    '<div class="img-container" style="height: 200px; margin-bottom: 15px; overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">\n                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/04338bb9-7852-4845-b6e4-f04bab3a4e39.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;">\n                    </div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

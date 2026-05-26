import re

file_path = r'c:\prog\dharmasrayacoding2.0-2026-materials\materials-smp\meet6.html'
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
            img.style.transform = "scale(2.5)";
        }

        function resetZoomPan(container) {
            const img = container.querySelector('img');
            img.style.transformOrigin = "center center";
            img.style.transform = "scale(1)";
        }
    </script>'''
if 'function zoomPan' not in html:
    html = html.replace('</script>', zoom_js, 1)

# 2. Slide 14
slide14_old = '''<div class="img-container" style="flex: 1; height: 400px;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/a9e19a93-9dde-423c-9408-1b7151716b88.png">
                </div>'''

slide14_new = '''<div style="flex: 1; position: relative;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/e9dc30e4-20b1-4f18-bbd1-58d55a6d97db.png" style="width: 150px; position: absolute; left: -80px; bottom: -40px; z-index: 5;" class="float" alt="Spaceship Sprite">
                    <div class="img-container" style="height: 400px; overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/a9e19a93-9dde-423c-9408-1b7151716b88.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;">
                    </div>
                </div>'''

html = html.replace(slide14_old, slide14_new)

# 3. Slide 15
slide15_old = '''<div class="img-container" style="flex: 1; height: 350px;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/0fd2a71d-a22c-4229-ab37-41b3d395339e.png">
                </div>'''

slide15_new = '''<div style="flex: 1; position: relative;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/03883283-02ed-42c2-a813-0025ae9f7bb1.png" style="width: 150px; position: absolute; right: -50px; bottom: -20px; z-index: 5;" class="float" alt="Meteor Sprite">
                    <div class="img-container" style="height: 350px; overflow: hidden; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/0fd2a71d-a22c-4229-ab37-41b3d395339e.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;">
                    </div>
                </div>'''

html = html.replace(slide15_old, slide15_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

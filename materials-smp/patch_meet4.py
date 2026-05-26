import re

file_path = r'c:\prog\dharmasrayacoding2.0-2026-materials\materials-smp\meet4.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Slide 9 (Blok Control Oranye)
slide9_old = '''        <!-- Slide 9: Orange Blocks -->
        <div class="slide" id="slide9">
            <h2 class="agenda-title">Blok Control Oranye 🟠</h2>
            <p style="font-size: 1.2rem; margin-bottom: 30px; max-width: 850px;">Kita pelajari kode untuk mengulang sesuatu! Supaya program Scratch kita lebih sederhana dan mudah dibaca.</p>
            <div style="display: flex; gap: 20px; justify-content: center; width: 100%; align-items: flex-start;">
                <div class="block-repeat" style="min-width: 150px; min-height: 80px;">
                    <span style="font-weight: 800;">repeat (10)</span>
                    <div style="height: 30px; border: 2px dashed #ffab19; border-radius: 4px; margin-left: 10px;"></div>
                </div>
                <div class="block-repeat" style="min-width: 150px; min-height: 80px;">
                    <span style="font-weight: 800;">forever</span>
                    <div style="height: 30px; border: 2px dashed #ffab19; border-radius: 4px; margin-left: 10px;"></div>
                </div>
                <div class="block-repeat" style="min-width: 150px; min-height: 80px;">
                    <span style="font-weight: 800;">repeat until <span style="background: white; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; color: #333;">( )?</span></span>
                    <div style="height: 30px; border: 2px dashed #ffab19; border-radius: 4px; margin-left: 10px;"></div>
                </div>
            </div>
            <p style="margin-top: 25px; font-size: 1rem; color: #aaa;">💡 Bentuknya seperti mulut, bagian tengah itu tempat untuk memasukkan blok lain!</p>
        </div>'''
slide9_new = '''        <!-- Slide 9: Orange Blocks -->
        <div class="slide" id="slide9">
            <h2 class="agenda-title" style="margin-bottom: 20px;">Blok Control Oranye 🟠</h2>
            <p style="font-size: 1.3rem; margin-bottom: 30px; max-width: 900px; color: #ddd;">Kita pelajari kode untuk mengulang sesuatu! Supaya program Scratch kita lebih sederhana dan mudah dibaca.<br>💡 Bentuk blok ini mirip seperti mulut yang sedang menganga, di mana kita bisa memasukkan blok lain di tengahnya!</p>
            <div style="display: flex; gap: 30px; justify-content: center; width: 100%; align-items: stretch; max-width: 1000px;">
                <div class="card" style="flex: 1; border-top: 5px solid var(--orange); display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
                    <div class="block-repeat" style="min-width: 150px; min-height: 80px; margin-bottom: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
                        <span style="font-weight: 800;">repeat (10)</span>
                        <div style="height: 30px; border: 2px dashed rgba(255,255,255,0.5); border-radius: 4px; margin-left: 10px;"></div>
                    </div>
                    <h4 style="color: var(--orange); font-size: 1.4rem; margin: 0 0 10px 0;">REPEAT</h4>
                    <p style="font-size: 1.1rem; margin: 0;">Mengulang blok kode sesuai jumlah **ANGKA** di dalamnya.</p>
                </div>
                <div class="card" style="flex: 1; border-top: 5px solid var(--orange); display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
                    <div class="block-repeat" style="min-width: 150px; min-height: 80px; margin-bottom: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
                        <span style="font-weight: 800;">forever</span>
                        <div style="height: 30px; border: 2px dashed rgba(255,255,255,0.5); border-radius: 4px; margin-left: 10px;"></div>
                    </div>
                    <h4 style="color: var(--orange); font-size: 1.4rem; margin: 0 0 10px 0;">FOREVER</h4>
                    <p style="font-size: 1.1rem; margin: 0;">Mengulang blok kode secara terus-menerus **SELAMANYA**.</p>
                </div>
                <div class="card" style="flex: 1; border-top: 5px solid var(--orange); display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
                    <div class="block-repeat" style="min-width: 150px; min-height: 80px; margin-bottom: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
                        <span style="font-weight: 800;">repeat until <span style="background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.4);">( )?</span></span>
                        <div style="height: 30px; border: 2px dashed rgba(255,255,255,0.5); border-radius: 4px; margin-left: 10px;"></div>
                    </div>
                    <h4 style="color: var(--orange); font-size: 1.4rem; margin: 0 0 10px 0;">REPEAT UNTIL</h4>
                    <p style="font-size: 1.1rem; margin: 0;">Mengulang blok kode **SAMPAI** kondisi (syarat) tertentu terpenuhi.</p>
                </div>
            </div>
        </div>'''
html = html.replace(slide9_old, slide9_new)

# 2. Add Starter Project Slide after Slide 12
slide12_end = '''        <!-- Slide 13: Step 1 Bear -->'''
starter_slide = '''        <!-- Slide 12B: Starter Project -->
        <div class="slide" id="slide12b">
            <h2 class="agenda-title">Butuh Starter Project? 🛠️</h2>
            <div style="display: flex; gap: 40px; align-items: center;">
                <div class="img-container" style="flex: 1.2; height: 350px;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/541086b5-83bb-4123-9545-9dc63f28a3d5.png" alt="Remix Tutorial">
                </div>
                <div style="flex: 0.8; text-align: left;">
                    <div class="card" style="padding: 30px;">
                        <h4 style="color: var(--secondary); font-size: 1.5rem; margin-bottom: 15px;">Langkah:</h4>
                        <ol style="font-size: 1.3rem; line-height: 1.8; margin-left: 20px;">
                            <li>Buka link starter project berikut:<br>
                                <a href="https://scratch.mit.edu/projects/1324369416/" target="_blank" class="huge-btn pulsing" style="display: inline-block; margin: 15px 0; font-size: 1.1rem; padding: 10px 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">BUKA STARTER PROJECT 🚀</a>
                            </li>
                            <li>Klik tombol **Remix** (berwarna hijau) di kanan atas.</li>
                            <li>Sekarang semua aset sudah ada di dalam editor kamu!</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 13: Step 1 Bear -->'''
html = html.replace(slide12_end, starter_slide)

# 3. Update Slide 15 for zoom and pan
slide15_old = '''        <!-- Slide 15: Step 3 Backdrop Prep -->
        <div class="slide" id="slide15">
            <h2 class="agenda-title">Langkah 3: Trik Moving Backdrop 🎬</h2>
            <div class="grid-container" style="gap: 15px; max-width: 1000px;">
                <div class="card" style="padding: 10px; display: flex; flex-direction: column; align-items: center;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 5px; font-size: 0.9rem;">Step 1: Pilih Backdrop</div>
                    <div style="height: 140px; width: 100%; display: flex; align-items: center; justify-content: center;">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/7e6b653a-07aa-4559-bf70-522d9c015776.png" style="max-width: 100%; max-height: 100%; border-radius: 8px; object-fit: contain;">
                    </div>
                </div>
                <div class="card" style="padding: 10px; display: flex; flex-direction: column; align-items: center;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 5px; font-size: 0.9rem;">Step 2: Copy Tab Backdrop</div>
                    <div style="height: 140px; width: 100%; display: flex; align-items: center; justify-content: center;">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b757f740-d690-4d26-a069-725ebcaedb3a.png" style="max-width: 100%; max-height: 100%; border-radius: 8px; object-fit: contain;">
                    </div>
                </div>
                <div class="card" style="padding: 10px; display: flex; flex-direction: column; align-items: center;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 5px; font-size: 0.9rem;">Step 3: Paste ke Sprite Baru</div>
                    <div style="height: 140px; width: 100%; display: flex; align-items: center; justify-content: center;">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/eac041a7-75bd-483e-865b-deec4b1f2397.png" style="max-width: 100%; max-height: 100%; border-radius: 8px; object-fit: contain;">
                    </div>
                </div>
                <div class="card" style="padding: 10px; display: flex; flex-direction: column; align-items: center;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 5px; font-size: 0.9rem;">Step 4: Atur Posisi Sprite</div>
                    <div style="height: 140px; width: 100%; display: flex; align-items: center; justify-content: center;">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/93291ddf-7b54-46cd-bedd-8de5d7cfb6f9.png" style="max-width: 100%; max-height: 100%; border-radius: 8px; object-fit: contain;">
                    </div>
                </div>
            </div>
            <p style="margin-top: 15px; font-weight: 800; color: var(--accent);">Penting: Kita menjadikan Backdrop sebagai Sprite agar bisa digerakkan!</p>
        </div>'''
slide15_new = '''        <!-- Slide 15: Step 3 Backdrop Prep -->
        <div class="slide" id="slide15">
            <h2 class="agenda-title">Langkah 3: Trik Moving Backdrop 🎬</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 1000px; margin: 0 auto;">
                <div class="card" style="padding: 15px; display: flex; flex-direction: column; align-items: center; overflow: visible;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 10px; font-size: 1.1rem;">Step 1: Pilih Backdrop</div>
                    <div style="height: 200px; width: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 8px; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/7e6b653a-07aa-4559-bf70-522d9c015776.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;" class="zoom-image">
                    </div>
                </div>
                <div class="card" style="padding: 15px; display: flex; flex-direction: column; align-items: center; overflow: visible;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 10px; font-size: 1.1rem;">Step 2: Copy Tab Backdrop</div>
                    <div style="height: 200px; width: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 8px; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b757f740-d690-4d26-a069-725ebcaedb3a.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;" class="zoom-image">
                    </div>
                </div>
                <div class="card" style="padding: 15px; display: flex; flex-direction: column; align-items: center; overflow: visible;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 10px; font-size: 1.1rem;">Step 3: Paste ke Sprite Baru</div>
                    <div style="height: 200px; width: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 8px; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/eac041a7-75bd-483e-865b-deec4b1f2397.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;" class="zoom-image">
                    </div>
                </div>
                <div class="card" style="padding: 15px; display: flex; flex-direction: column; align-items: center; overflow: visible;">
                    <div style="font-weight: 800; color: var(--secondary); margin-bottom: 10px; font-size: 1.1rem;">Step 4: Atur Posisi Sprite</div>
                    <div style="height: 200px; width: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 8px; position: relative;" onmousemove="zoomPan(event, this)" onmouseleave="resetZoomPan(this)">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/93291ddf-7b54-46cd-bedd-8de5d7cfb6f9.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s ease-out; transform-origin: center center;" class="zoom-image">
                    </div>
                </div>
            </div>
            <p style="margin-top: 25px; font-weight: 800; color: var(--accent); font-size: 1.2rem;">Penting: Kita menjadikan Backdrop sebagai Sprite agar bisa digerakkan!</p>
        </div>'''
html = html.replace(slide15_old, slide15_new)


# Insert zoomPan JS functions before </script>
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
html = html.replace('</script>', zoom_js, 1)

# Replace JS string wrappers that might break to backticks
# But `meet4.html` might have innerHTML assignments? Let's check:
html = re.sub(r'(text\.innerHTML\s*=\s*)"(.*?)"', r'\1`\2`', html)
# Actually, the quiz check strings: `btn.innerHTML = opt;` and others don't have bold. 
# It's better to just regex replace `**` for text outside of `<script>`.
# For simplicity, we just do it globally, then fix any known js strings. In meet4 there is no `lampText`.
# In meet4, `**` occurs in HTML text.
html = re.sub(r'\*\*(.*?)\*\*', r'<span style="color: var(--secondary); font-weight: bold;">\1</span>', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

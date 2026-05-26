import re

file_path = r'c:\prog\dharmasrayacoding2.0-2026-materials\materials-smp\meet3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Slide 3 (Misi Pembelajaran)
slide3_old = '''            <div class="step-list">
                <div class="step-item" style="border: 2px solid rgba(255,255,255,0.1);">
                    <div class="step-number">01</div>
                    <div class="step-content"><h4>Memahami Event</h4><p><strong>Mempelajari pemicu (trigger) untuk memulai sebuah rangkaian kode.</strong></p></div>
                </div>
                <div class="step-item" style="border: 2px solid rgba(255,255,255,0.1);">
                    <div class="step-number">02</div>
                    <div class="step-content"><h4>Interactive Click</h4><p><strong>Membuat aksi terjadi saat karakter (sprite) diklik oleh mouse.</strong></p></div>
                </div>
                <div class="step-item" style="border: 2px solid rgba(255,255,255,0.1);">
                    <div class="step-number">03</div>
                    <div class="step-content"><h4>Remix Project</h4><p><strong>Belajar cara mengambil aset dan ide dari project orang lain.</strong></p></div>
                </div>
            </div>'''
slide3_new = '''            <div class="step-list">
                <div class="step-item">
                    <div class="step-number">01</div>
                    <div class="step-content"><h4>⚡ Memahami Event</h4><p>Mempelajari pemicu (trigger) untuk memulai sebuah rangkaian kode.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">02</div>
                    <div class="step-content"><h4>🖱️ Interactive Click</h4><p>Membuat aksi terjadi saat karakter (sprite) diklik oleh mouse.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">03</div>
                    <div class="step-content"><h4>🔄 Remix Project</h4><p>Belajar cara mengambil aset dan ide dari project orang lain.</p></div>
                </div>
            </div>'''
html = html.replace(slide3_old, slide3_new)

# 2. Update Slide 12 (Contoh Event di Scratch)
slide12_old = '''        <div class="slide" id="slide12">
            <h2 class="agenda-title">Contoh Event di Scratch 🛡️</h2>
            <div style="display: flex; flex-direction: column; gap: 20px; width: 100%; max-width: 800px;">
                <div class="step-item" style="gap: 20px;">
                    <div class="block-stack"><div class="block block-event">when <img src="https://static.vecteezy.com/system/resources/previews/022/110/391/non_2x/green-flag-free-png.png" style="height:1.2rem; vertical-align: middle;"> clicked</div></div>
                    <div class="step-content"><h4>Bendera Hijau</h4><p>Tombol START untuk memulai semua kode sekaligus.</p></div>
                </div>
                <div class="step-item" style="gap: 20px;">
                    <div class="block-stack"><div class="block block-event">when <span class="block-dropdown">space ▼</span> key pressed</div></div>
                    <div class="step-content"><h4>Keyboard</h4><p>Kode jalan saat kamu menekan tombol tertentu di Keyboard.</p></div>
                </div>
                <div class="step-item" style="gap: 20px; background: rgba(74, 139, 139, 0.2); border: 2px solid var(--primary);">
                    <div class="block-stack"><div class="block block-event">when this sprite clicked</div></div>
                    <div class="step-content"><h4>Klik Sprite</h4><p>Kode jalan saat kamu **KLIK** karakter tersebut dengan mouse.</p></div>
                </div>
            </div>
        </div>'''
slide12_new = '''        <div class="slide" id="slide12">
            <h2 class="agenda-title" style="margin-bottom: 20px;">Contoh Event di Scratch 🛡️</h2>
            <div style="display: flex; flex-direction: column; gap: 20px; width: 100%; max-width: 900px;">
                <div style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 20px; border-left: 8px solid var(--success); display: flex; align-items: center; gap: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                    <div style="flex-shrink: 0;"><div class="block block-event" style="font-size: 1.3rem; padding: 15px 20px;">when <img src="https://static.vecteezy.com/system/resources/previews/022/110/391/non_2x/green-flag-free-png.png" style="height:1.5rem; vertical-align: middle;"> clicked</div></div>
                    <div><h4 style="margin: 0 0 10px 0; font-size: 1.6rem; color: var(--success);">🚩 Bendera Hijau</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Tombol <strong style="color: white;">START</strong> untuk memulai semua kode sekaligus dari awal permainan.</p></div>
                </div>
                <div style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 20px; border-left: 8px solid #4c97ff; display: flex; align-items: center; gap: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                    <div style="flex-shrink: 0;"><div class="block block-event" style="font-size: 1.3rem; padding: 15px 20px;">when <span class="block-dropdown">space ▼</span> key pressed</div></div>
                    <div><h4 style="margin: 0 0 10px 0; font-size: 1.6rem; color: #4c97ff;">⌨️ Keyboard</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Kode jalan saat kamu menekan tombol tertentu (seperti <em>Spasi</em> atau <em>Panah</em>) di keyboard.</p></div>
                </div>
                <div style="background: linear-gradient(135deg, rgba(74, 139, 139, 0.2), rgba(242, 193, 64, 0.15)); padding: 25px; border-radius: 20px; border-left: 8px solid var(--secondary); display: flex; align-items: center; gap: 30px; border-top: 2px solid var(--secondary); border-right: 2px solid var(--secondary); border-bottom: 2px solid var(--secondary); box-shadow: 0 15px 40px rgba(242, 193, 64, 0.2);">
                    <div style="flex-shrink: 0;"><div class="block block-event" style="font-size: 1.3rem; padding: 15px 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.5);">when this sprite clicked</div></div>
                    <div><h4 style="margin: 0 0 10px 0; font-size: 1.6rem; color: var(--secondary);">🖱️ Klik Sprite</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Kode jalan saat kamu <span style="color: var(--secondary); font-weight: bold; font-size: 1.4rem;">KLIK</span> karakter tersebut secara langsung dengan mouse-mu!</p></div>
                </div>
            </div>
        </div>'''
html = html.replace(slide12_old, slide12_new)

# 3. Replace all **text** with colored span
html = re.sub(r'\*\*(.*?)\*\*', r'<span style="color: var(--secondary); font-weight: bold;">\1</span>', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

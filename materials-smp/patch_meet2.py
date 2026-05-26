import re

file_path = r'c:\prog\dharmasrayacoding2.0-2026-materials\materials-smp\meet2.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()


# 2. Slide 3 (Misi Pembelajaran)
slide3_old = '''                <div class="step-item">
                    <div class="step-number">01</div>
                    <div class="step-content"><h4>Memahami Titik Stage</h4><p>Mempelajari sistem koordinat X & Y pada layar Scratch.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">02</div>
                    <div class="step-content"><h4>Gerakan Glide Presisi</h4><p>Mengirim robot ke lokasi tertentu berdasarkan angka koordinat.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">03</div>
                    <div class="step-content"><h4>Sistem Spawn</h4><p>Menentukan titik awal robot dengan blok [Go to].</p></div>
                </div>'''
slide3_new = '''                <div class="step-item">
                    <div class="step-number">01</div>
                    <div class="step-content"><h4>📍 Memahami Titik Stage</h4><p>Mempelajari sistem koordinat X & Y pada layar Scratch.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">02</div>
                    <div class="step-content"><h4>✈️ Gerakan Glide Presisi</h4><p>Mengirim robot ke lokasi tertentu berdasarkan angka koordinat.</p></div>
                </div>
                <div class="step-item">
                    <div class="step-number">03</div>
                    <div class="step-content"><h4>🕹️ Sistem Spawn</h4><p>Menentukan titik awal robot dengan blok [Go to].</p></div>
                </div>'''
html = html.replace(slide3_old, slide3_new)

# 3. Slide 10 (Drone Mission: Level 1)
slide10_old = '''        <!-- Slide 10: Activity 1 -->
        <div class="slide" id="slide10">
            <h2 class="agenda-title">Drone Mission: Level 1 📦</h2>
            <div style="display: flex; gap: 40px; width: 100%; align-items: flex-start;">
                <div class="card" style="flex: 0.8; text-align: left; padding: 20px; background: rgba(0,0,0,0.4);">
                    <h4 style="font-size: 1.2rem; color: var(--secondary);">Urutan Pengiriman:</h4>
                    <div style="font-family: monospace; background: #222; padding: 15px; border-radius: 10px; border: 1px solid var(--primary); margin-bottom: 10px;">
                        1. glide 1s to x: 100 y: 100 <br>
                        2. glide 1s to x: -100 y: 50 <br>
                        3. glide 1s to x: 0 y: -100
                    </div>
                    <p style="margin-top: 5px; font-size: 0.9rem;">Klik titik pada grid sesuai urutan di atas!</p>'''
slide10_new = '''        <!-- Slide 10: Activity 1 -->
        <div class="slide" id="slide10">
            <h2 class="agenda-title">Drone Mission: Level 1 📦</h2>
            <div style="display: flex; gap: 40px; width: 100%; align-items: flex-start;">
                <div class="card" style="flex: 0.8; text-align: left; padding: 25px; background: rgba(0,0,0,0.4); border: 2px solid var(--primary);">
                    <h4 style="font-size: 1.5rem; color: var(--secondary); margin-bottom: 15px;">📜 Urutan Pengiriman:</h4>
                    <div style="font-family: monospace; font-size: 1.2rem; background: #1a2424; padding: 20px; border-radius: 10px; border-left: 5px solid var(--success); margin-bottom: 15px;">
                        <span style="color: var(--accent);">1.</span> glide 1s to x: <strong style="color: white;">100</strong> y: <strong style="color: white;">100</strong> <br>
                        <span style="color: var(--accent);">2.</span> glide 1s to x: <strong style="color: white;">-100</strong> y: <strong style="color: white;">50</strong> <br>
                        <span style="color: var(--accent);">3.</span> glide 1s to x: <strong style="color: white;">0</strong> y: <strong style="color: white;">-100</strong>
                    </div>
                    <div style="background: rgba(242, 193, 64, 0.2); padding: 15px; border-radius: 10px; border: 1px dashed var(--secondary);">
                        <p style="margin: 0; font-size: 1rem; color: #ddd;"><strong>Misi:</strong> Klik titik pada grid di sebelah kanan, berurutan sesuai koordinat di atas untuk mengantar paket!</p>
                    </div>'''
html = html.replace(slide10_old, slide10_new)

# 4. Slide 11 (Drone Mission: Level 2)
slide11_old = '''        <!-- Slide 11: Activity 2 -->
        <div class="slide" id="slide11">
            <h2 class="agenda-title">Drone Mission: Level 2 🌫️</h2>
            <div style="display: flex; gap: 40px; width: 100%; align-items: flex-start;">
                <div class="card" style="flex: 0.8; text-align: left; padding: 20px; background: rgba(0,0,0,0.4);">
                    <h4 style="font-size: 1.2rem; color: var(--secondary);">Urutan Pengiriman:</h4>
                    <div style="font-family: monospace; background: #222; padding: 15px; border-radius: 10px; border: 1px solid var(--primary); margin-bottom: 10px;">
                        1. glide 1s to x: 150 y: -150 <br>
                        2. glide 1s to x: -150 y: -100 <br>
                        3. glide 1s to x: 100 y: 150 <br>
                        4. glide 1s to x: -100 y: 100
                    </div>'''
slide11_new = '''        <!-- Slide 11: Activity 2 -->
        <div class="slide" id="slide11">
            <h2 class="agenda-title">Drone Mission: Level 2 🌫️</h2>
            <div style="display: flex; gap: 40px; width: 100%; align-items: flex-start;">
                <div class="card" style="flex: 0.8; text-align: left; padding: 25px; background: rgba(0,0,0,0.4); border: 2px solid var(--primary);">
                    <h4 style="font-size: 1.5rem; color: var(--secondary); margin-bottom: 15px;">📜 Urutan Pengiriman:</h4>
                    <div style="font-family: monospace; font-size: 1.2rem; background: #1a2424; padding: 20px; border-radius: 10px; border-left: 5px solid var(--success); margin-bottom: 15px;">
                        <span style="color: var(--accent);">1.</span> glide 1s to x: <strong style="color: white;">150</strong> y: <strong style="color: white;">-150</strong> <br>
                        <span style="color: var(--accent);">2.</span> glide 1s to x: <strong style="color: white;">-150</strong> y: <strong style="color: white;">-100</strong> <br>
                        <span style="color: var(--accent);">3.</span> glide 1s to x: <strong style="color: white;">100</strong> y: <strong style="color: white;">150</strong> <br>
                        <span style="color: var(--accent);">4.</span> glide 1s to x: <strong style="color: white;">-100</strong> y: <strong style="color: white;">100</strong>
                    </div>
                    <div style="background: rgba(242, 193, 64, 0.2); padding: 15px; border-radius: 10px; border: 1px dashed var(--secondary);">
                        <p style="margin: 0; font-size: 1rem; color: #ddd;"><strong>Misi:</strong> Jaraknya makin jauh! Klik titik koordinat di grid dengan teliti sesuai urutan!</p>
                    </div>'''
html = html.replace(slide11_old, slide11_new)

# 5. Slide 12 (HEBAT!)
slide12_old = '''        <!-- Slide 12: Start Project -->
        <div class="slide solid-teal-bg" id="slide12" style="background: #4a8b8b;">
            <div style="font-size: 8rem;" class="float">🚀✨</div>
            <h1 style="font-size: 3.5rem;">HEBAT! <br>KAMU SUDAH PAHAM KOORDINAT.</h1>
            <p style="font-size: 1.8rem;">Sekarang, mari kita buat project **Robo-KAL Delivery Drone** kita sendiri!</p>
        </div>'''
slide12_new = '''        <!-- Slide 12: Start Project -->
        <div class="slide solid-teal-bg" id="slide12" style="background: linear-gradient(135deg, #1a237e, #4a148c);">
            <div style="font-size: 8rem;" class="float">🚀✨</div>
            <h1 style="font-size: 5rem; background: linear-gradient(to right, #f2c140, #ff5252); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 10px 20px rgba(0,0,0,0.5); margin-bottom: 20px;">LULUS NAVIGASI!</h1>
            <div style="background: rgba(255,255,255,0.1); padding: 30px 50px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px);">
                <p style="font-size: 1.8rem; margin: 0; color: #fff;">Pemahaman koordinat kamu sangat presisi. Saatnya kita bangun <span style="color: var(--secondary); font-weight: bold;">Robo-KAL Delivery Drone</span> milikmu sendiri!</p>
            </div>
        </div>'''
html = html.replace(slide12_old, slide12_new)

# 6. Slide 13 (Siap Beraksi)
slide13_old = '''        <!-- Slide 13: Portal -->
        <div class="slide" id="slide13">
            <div style="text-align: center; position: relative;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Scratchlogo.svg/3840px-Scratchlogo.svg.png" style="height: 180px; position: absolute; top: -150px; left: 50%; transform: translateX(-50%);" class="float">
                <h1 style="margin-bottom: 30px; font-size: 4rem;">Siap Beraksi?</h1>
                <p style="font-size: 1.5rem; margin-bottom: 40px; color: var(--secondary);">Waktunya mengirim paket ke seluruh penjuru Stage!</p>
                <a href="https://scratch.mit.edu/" target="_blank" class="huge-btn pulsing">BUKA SCRATCH.MIT.EDU 🚀</a>
            </div>
        </div>'''
slide13_new = '''        <!-- Slide 13: Portal -->
        <div class="slide" id="slide13">
            <div style="text-align: center; position: relative; background: rgba(255,255,255,0.05); padding: 80px 100px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Scratchlogo.svg/3840px-Scratchlogo.svg.png" style="height: 120px; position: absolute; top: -60px; left: 50%; transform: translateX(-50%);" class="float">
                <h1 style="margin-bottom: 20px; font-size: 4.5rem; color: var(--light);">Siap Beraksi?</h1>
                <p style="font-size: 1.6rem; margin-bottom: 50px; color: #ccc;">Sistem sudah siap. Waktunya buka <span style="color: var(--secondary); font-weight: bold;">Workspace</span> kamu dan rakit Drone-mu!</p>
                <a href="https://scratch.mit.edu/" target="_blank" class="huge-btn pulsing" style="font-size: 2rem; padding: 25px 60px; box-shadow: 0 0 30px var(--primary);">MASUK KE SCRATCH 🚀</a>
            </div>
        </div>'''
html = html.replace(slide13_old, slide13_new)

# 7. Slide 16 (Langkah 3: Program Robot)
slide16_old = '''        <!-- Slide 16: Step 3 Coding -->
        <div class="slide" id="slide16">
            <h2 class="agenda-title">Langkah 3: Program Robot ⚙️</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; width: 100%;">
                <div class="card">
                    <div class="img-container" style="height: 180px;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/bac87a1b-0141-4d47-bb67-c97cf0b78b78.png" alt="Spawn Logic"></div>
                    <p>**1. Spawn**: Gunakan [Go to X: Y:] untuk posisi awal drone.</p>
                </div>
                <div class="card">
                    <div class="img-container" style="height: 180px;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b4d956d7-4604-425d-822f-5c5865106ecf.png" alt="Glide Logic"></div>
                    <p>**2. Delivery**: Susun blok [Glide] ke koordinat tiap rumah.</p>
                </div>
                <div class="card">
                    <div class="img-container" style="height: 180px;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/eda0edda-896a-499c-866d-b94ae77e8989.png" alt="Return Logic"></div>
                    <p>**3. Return**: Pastikan drone kembali ke posisi semula.</p>
                </div>
            </div>
        </div>'''
slide16_new = '''        <!-- Slide 16: Step 3 Coding -->
        <div class="slide" id="slide16">
            <h2 class="agenda-title">Langkah 3: Program Robot ⚙️</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; width: 100%; max-width: 1200px;">
                <div class="card" style="padding: 25px; display: flex; flex-direction: column; height: 100%;">
                    <div class="step-num" style="background: var(--primary); color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 15px auto;">1</div>
                    <h4 style="margin: 0 0 10px 0; font-size: 1.4rem;">Spawn</h4>
                    <p style="font-size: 1.1rem; color: #ddd; margin-bottom: 20px; flex-grow: 1;">Gunakan <span style="color: var(--secondary); font-weight: bold;">Go to X: Y:</span> untuk posisi awal drone.</p>
                    <div class="img-container" style="height: 250px; background: transparent; border: none; padding: 0;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/bac87a1b-0141-4d47-bb67-c97cf0b78b78.png" style="width: 100%; height: 100%; object-fit: contain;" alt="Spawn Logic"></div>
                </div>
                <div class="card" style="padding: 25px; display: flex; flex-direction: column; height: 100%;">
                    <div class="step-num" style="background: var(--secondary); color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 15px auto;">2</div>
                    <h4 style="margin: 0 0 10px 0; font-size: 1.4rem;">Delivery</h4>
                    <p style="font-size: 1.1rem; color: #ddd; margin-bottom: 20px; flex-grow: 1;">Susun blok <span style="color: var(--secondary); font-weight: bold;">Glide</span> ke koordinat tiap rumah.</p>
                    <div class="img-container" style="height: 250px; background: transparent; border: none; padding: 0;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/b4d956d7-4604-425d-822f-5c5865106ecf.png" style="width: 100%; height: 100%; object-fit: contain;" alt="Glide Logic"></div>
                </div>
                <div class="card" style="padding: 25px; display: flex; flex-direction: column; height: 100%;">
                    <div class="step-num" style="background: var(--danger); color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 15px auto;">3</div>
                    <h4 style="margin: 0 0 10px 0; font-size: 1.4rem;">Return</h4>
                    <p style="font-size: 1.1rem; color: #ddd; margin-bottom: 20px; flex-grow: 1;">Pastikan drone kembali ke posisi semula (Markas).</p>
                    <div class="img-container" style="height: 250px; background: transparent; border: none; padding: 0;"><img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/eda0edda-896a-499c-866d-b94ae77e8989.png" style="width: 100%; height: 100%; object-fit: contain;" alt="Return Logic"></div>
                </div>
            </div>
        </div>'''
html = html.replace(slide16_old, slide16_new)

# 8. Slide 17 (Testing & Polish)
slide17_old = '''        <!-- Slide 17: Testing -->
        <div class="slide" id="slide17">
            <h2 class="agenda-title">Testing & Polish ✨</h2>
            <div class="card" style="width: 100%; max-width: 900px; text-align: left;">
                <ul style="font-size: 1.3rem; line-height: 1.8;">
                    <li>✅ **Glide Check**: Apakah drone berhenti tepat di depan tiap rumah?</li>
                    <li>🎨 **Costume Change**: Ubah costume drone setiap sampai di rumah tujuan.</li>
                    <li>📏 **Scale Effect**: Buat drone mengecil saat terbang, dan kembali ke ukuran semula saat berhenti!</li>
                    <li>💬 **Say Block**: Tambahkan pesan "Paket Sampai!" di setiap titik.</li>
                </ul>
            </div>
        </div>'''
slide17_new = '''        <!-- Slide 17: Testing -->
        <div class="slide" id="slide17">
            <h2 class="agenda-title">Testing & Polish ✨</h2>
            <div style="display: flex; flex-direction: column; gap: 20px; width: 100%; max-width: 900px;">
                <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 6px solid var(--success); display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 2.5rem;">✅</div>
                    <div><h4 style="margin: 0 0 5px 0; font-size: 1.4rem; color: var(--secondary);">Glide Check</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Apakah drone berhenti tepat di depan tiap rumah?</p></div>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 6px solid #4c97ff; display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 2.5rem;">🎨</div>
                    <div><h4 style="margin: 0 0 5px 0; font-size: 1.4rem; color: var(--secondary);">Costume Change</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Ubah costume drone setiap kali dia sampai di rumah tujuan.</p></div>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 6px solid var(--secondary); display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 2.5rem;">📏</div>
                    <div><h4 style="margin: 0 0 5px 0; font-size: 1.4rem; color: var(--secondary);">Scale Effect</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Buat efek ukuran! Drone mengecil saat terbang, kembali besar saat berhenti.</p></div>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 6px solid var(--danger); display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 2.5rem;">💬</div>
                    <div><h4 style="margin: 0 0 5px 0; font-size: 1.4rem; color: var(--secondary);">Say Block</h4><p style="margin: 0; font-size: 1.2rem; color: #ddd;">Tambahkan pesan <span style="font-weight: bold; color: white;">"Paket Sampai!"</span> di setiap titik pemberhentian.</p></div>
                </div>
            </div>
        </div>'''
html = html.replace(slide17_old, slide17_new)

# 9. Slide 19 (Amankan Karyamu)
slide19_old = '''        <!-- Slide 19: Save & Share -->
        <div class="slide" id="slide19">
            <h2 class="agenda-title">Amankan Karyamu! 💾</h2>
            <div style="display: flex; gap: 40px; align-items: center;">
                <div class="img-container" style="flex: 1; height: 350px;">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/7baf96b6-d7f5-414f-af1e-103021a624fa.png" alt="Save Button">
                </div>
                <div style="flex: 1; text-align: left;">
                    <div class="card" style="padding: 40px;">
                        <div style="font-size: 5rem;">🌐</div>
                        <h4>Save & Share</h4>
                        <p style="font-size: 1.3rem;">Klik **Save Now** lalu klik **Share** agar projectmu bisa dilihat oleh teman-teman lainnya!</p>
                    </div>
                </div>
            </div>
        </div>'''
slide19_new = '''        <!-- Slide 19: Save & Share -->
        <div class="slide" id="slide19">
            <h2 class="agenda-title">Amankan Karyamu! 💾</h2>
            <div style="display: flex; gap: 40px; align-items: center; width: 100%; max-width: 1000px;">
                <div class="img-container" style="flex: 1.2; height: 400px; padding: 20px; background: rgba(255,255,255,0.05); border: 2px dashed var(--secondary);">
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/7baf96b6-d7f5-414f-af1e-103021a624fa.png" alt="Save Button" style="border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
                </div>
                <div style="flex: 0.8; text-align: left;">
                    <div style="background: linear-gradient(135deg, rgba(74, 139, 139, 0.4), rgba(242, 193, 64, 0.2)); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); box-shadow: 0 15px 30px rgba(0,0,0,0.4);">
                        <div style="font-size: 5rem; margin-bottom: 20px; animation: floating 3s infinite alternate;">🌐</div>
                        <h4 style="font-size: 2rem; color: var(--secondary); margin-bottom: 15px;">Save & Share</h4>
                        <p style="font-size: 1.3rem; line-height: 1.6; color: #ddd; margin: 0;">Pastikan kerjamu aman! Klik <span style="color: var(--secondary); font-weight: bold;">Save Now</span> untuk menyimpan. Lalu klik tombol <span style="color: var(--success); font-weight: bold;">Share</span> agar karyamu bisa dimainkan oleh teman-teman yang lain!</p>
                    </div>
                </div>
            </div>
        </div>'''
html = html.replace(slide19_old, slide19_new)

# 10. Slide 22 (Feedback)
slide22_old = '''        <!-- Slide 22: Feedback -->
        <div class="slide" id="slide22">
            <h2 class="agenda-title">Session Feedback 💖</h2>
            <div style="display: flex; gap: 50px; align-items: center;">
                <div style="background: white; padding: 20px; border-radius: 20px;">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://bit.ly/feedback-smp2" style="width: 200px;">
                </div>
                <div style="text-align: left;">
                    <h3>Bantu Kami Menjadi Lebih Baik!</h3>
                    <p style="margin-bottom: 30px;">Scan QR atau klik tombol di bawah untuk memberikan masukan.</p>
                    <a href="https://bit.ly/feedback-smp2" target="_blank" class="huge-btn">ISI FEEDBACK ➜</a>
                </div>
            </div>
        </div>'''
slide22_new = '''        <!-- Slide 22: Feedback -->
        <div class="slide" id="slide22">
            <h2 class="agenda-title" style="margin-bottom: 15px;">Bagaimana Kelas Hari Ini? 💖</h2>
            <p style="font-size: 1.3rem; text-align: center; max-width: 800px; margin-bottom: 30px; color: #ddd;">
                Bantu kami menjadi lebih baik dengan mengisi form feedback singkat ya!
            </p>
            <div style="display: flex; gap: 40px; align-items: center; justify-content: center; width: 100%; max-width: 900px;">
                <div style="position: relative; width: 250px; height: 250px; flex-shrink: 0; display: flex; justify-content: center; align-items: flex-end;">
                    <div style="position: absolute; top: 20px; left: 20px; font-size: 3rem; animation: floating 2s infinite alternate;">💖</div>
                    <div style="position: absolute; top: 50px; right: 20px; font-size: 2.5rem; animation: floating 2.5s infinite alternate reverse;">✨</div>
                    <div style="position: absolute; bottom: 60px; left: 10px; font-size: 2rem; animation: floating 3s infinite alternate;">🎉</div>
                    <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/756d9713-87b5-4ec4-ae39-9f2352b8e280.png" alt="Happy Cat" style="width: 220px; z-index: 2; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.2));" class="float">
                </div>
                <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 30px; box-shadow: 0 8px 25px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.2); text-align: center; width: 100%; max-width: 400px; display: flex; flex-direction: column; align-items: center; backdrop-filter: blur(10px);">
                    <div style="background: white; padding: 15px; border-radius: 15px; margin-bottom: 20px;">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://bit.ly/feedback-smp2" style="width: 150px; height: 150px;">
                    </div>
                    <h3 style="color: var(--secondary); margin: 0 0 10px 0; font-size: 1.5rem;">Selesai untuk Hari Ini!</h3>
                    <p style="color: #ddd; font-size: 1rem; margin-bottom: 20px;">Jangan lupa untuk menyelesaikan seluruh aktivitas di LMS ya!</p>
                    <a href="https://bit.ly/feedback-smp2" target="_blank" class="huge-btn" style="padding: 15px 30px; font-size: 1rem; width: 100%; box-sizing: border-box;">ISI FEEDBACK ➜</a>
                </div>
            </div>
        </div>'''
html = html.replace(slide22_old, slide22_new)

# 1. Replace **text** (do this last so it applies to any new text we added that might use **, though we mostly used spans in new text)
html = re.sub(r'\*\*(.*?)\*\*', r'<span style="color: var(--secondary); font-weight: bold;">\1</span>', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)


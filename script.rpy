##  FIRST AID HERO - Game Edukasi P3K SMP

# --- Karakter Utama ---
define lio    = Character("Lio",    color="#4FC3F7")
define sofyan = Character("Pak Sofyan", color="#EF9A9A")
define narrator = Character(None)

# --- Karakter Siswa (Korban) ---
define roni   = Character("Roni",   color="#A5D6A7")
define bima   = Character("Bima",   color="#FFE082")
define dedi   = Character("Dedi",   color="#CE93D8")
define dika   = Character("Dika",   color="#FFAB91")
define sari   = Character("Sari",   color="#F48FB1")
define budi   = Character("Budi",   color="#90CAF9")
define eko    = Character("Eko",    color="#C5E1A5")

# --- Background ---
image bg_lapangan       = "images/bg_lapangan.jpg"
image bg_uks            = "images/bg_uks.jpg"
image bg_lapang_basket  = "images/bg_lapang_basket.jpeg"
image bg_lapang_futsal  = "images/bg_lapang_futsal.jpeg"
image bg_lapang_voli    = "images/bg_lapang_voli.jpeg"
image bg_depan_uks      = "images/bg_depan_uks.jpeg"
image bg_tempat_teduh   = "images/bg_tempat_teduh.jpeg"
image bg_uks_menarik    = "images/bg_uks_menarik.jpeg"

# --- Lio ---
image lio neutral = "images/lio_neutral.png"
image lio happy   = "images/lio_happy.png"
image lio serious = "images/lio_serious.png"
image lio shocked = "images/lio_shocked.png"

# --- Pak Sofyan ---
image sofyan neutral = "images/sofyan_neutral.png"
image sofyan happy   = "images/sofyan_happy.png"
image sofyan serious = "images/sofyan_serious.png"

# --- Karakter ---
image roni pain    = "images/korban_pain.png"
image roni happy   = "images/roni_happy.png"
image roni neutral = "images/roni_neutral.png"
image bima pain    = "images/bima_pain.png"
image bima happy   = "images/bima_happy.png"
image bima neutral = "images/bima_neutral.png"
image dedi pain    = "images/dedi_pain.png"
image dedi happy   = "images/dedi_happy.png"
image dedi neutral = "images/dedi_neutral.png"
image dika pain    = "images/dika_pain.png"
image dika happy   = "images/dika_happy.png"
image sari pain    = "images/sari_pain.png"
image sari happy   = "images/sari_happy.png"
image budi pain    = "images/budi_pain.png"
image budi happy   = "images/budi_happy.png"
image eko pain     = "images/eko_pain.png"
image eko happy    = "images/eko_happy.png"

default score = 0


#  Intro Video
label splashscreen:
    $ renpy.movie_cutscene("intro.webm")
    return


#  START GAME

label start:
    $ renpy.transition(fade)
    $ renpy.pause(0.5, hard=True)
    $ renpy.movie_cutscene("awal_mulai.webm")
    play music "audio/bgm_school.mp3"
    scene bg_lapangan with fade
    show lio neutral at Transform(zoom=0.55, xalign=0.0, yalign=1.0)

    narrator "Selamat datang di FIRST AID HERO!"
    narrator "Kamu akan berperan sebagai LIO, anggota PMR yang bertugas di Event Classmeet."

    lio "Namaku Lio. Hari ini aku bertugas menjaga pos P3K di sekolah. Ayo mulai!"
    jump chapter1


#  CHAPTER 1: PENGENALAN & INSIDEN LAPANGAN 

label chapter1:
    scene bg_uks with fade
    show sofyan neutral at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    show lio neutral at Transform(zoom=0.55, xalign=0.0, yalign=1.0)

    "{b}== CHAPTER 1: Pengenalan Alat & Insiden Lapangan =={/b}"
    sofyan "Lio, sebelum bertugas, mari kita periksa isi tas P3K kita."
    
    # SOAL 1 
    "Soal 1: Apa yang sebaiknya digunakan untuk menutup luka terbuka?"
    
    # Memanggil screen pilihan gambar
    call screen image_choice_screen
    
    # Cek hasil pilihan
    if _return == "A":
        lio "Saya akan memilih kapas biasa untuk menutup lukanya."
        play sound "audio/incorrect.mp3"
        "{color=#FF6B6B}Salah!{/color} Kapas meninggalkan serat di luka."
    elif _return == "B":
        lio "Saya akan memilih kasa steril untuk menutup lukanya."
        play sound "audio/correct.wav"
        "{color=#69F0AE}Benar!{/color} Kasa steril adalah pilihan yang tepat."
        $ score += 10
    elif _return == "C":
        lio "Saya akan memilih tisu wajah untuk menutup lukanya."
        play sound "audio/incorrect.mp3"
        "{color=#FF6B6B}Salah!{/color} Tisu tidak steril dan mudah hancur."

    sofyan "Ingat ya Lio, kasa steril adalah penutup luka terbaik karena bebas kuman dan tidak meninggalkan serat. Serat dari kapas biasa atau tisu wajah berisiko menempel pada luka dan memicu infeksi."

    # SOAL 2 
    "Soal 2: Bagaimana cara benar menggunakan antiseptik?"
    menu:
        "A. Oleskan di area pinggir luka":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Cukup di sekitar tepi luka."
            $ score += 10
        "B. Tuang langsung ke dalam luka":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Bisa merusak jaringan sel baru."
        "C. Campur dengan air sabun":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Antiseptik digunakan tanpa dicampur sabun."

    sofyan "Antiseptik seperti povidone-iodine cukup dioleskan di sekitar tepi luka saja untuk menghalangi kuman dari kulit luar. Menuangkan langsung ke dalam luka terbuka justru merusak jaringan sel baru."

    # SOAL 3 
    "Soal 3: Apa fungsi Cold Pack?"
    menu:
        "A. Menghangatkan otot":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Cold pack bersifat dingin."
        "B. Membersihkan kotoran":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Itu fungsi irigasi air bersih."
        "C. Mengurangi bengkak dan nyeri":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Membantu menyempitkan pembuluh darah."
            $ score += 10

    sofyan "Cold pack bekerja menyempitkan pembuluh darah (vasokonstriksi) yang membantu meminimalkan memar, menahan pembengkakan, serta membius saraf sementara untuk meredakan nyeri."

    sofyan "Bagus! Sekarang ke lapangan, sepertinya ada insiden!"
    
    # --- INSIDEN FUTSAL ---
    play music "audio/bgm_action.mp3" fadeout 1.0 fadein 1.0
    scene bg_lapang_futsal with fade
    show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show roni pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    roni "Aduhh... saya terjatuh dan tanganku terluka"
    
    # SOAL 4 
    "Soal 4: Apa langkah pertama untuk menangani luka lecet Roni?"
    $ jawab_futsal_benar = False
    menu:
        "A. Cuci dengan air mengalir":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Irigasi kotoran terlebih dahulu."
            $ score += 10
            $ jawab_futsal_benar = True
        "B. Langsung tutup kasa":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Luka harus dibersihkan dulu."
        "C. Oleskan pasta gigi":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Sangat tidak dianjurkan untuk luka."

    lio "Selesai dibilas! Sesuai materi PMR, luka lecet harus dibilas air mengalir untuk membuang kotoran. Menutup luka yang masih kotor atau mengoleskan pasta gigi justru mengunci bakteri di dalam luka!"

    if jawab_futsal_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show roni happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Nah, Roni, lukamu sudah bersih sekarang dan dibalut kasa steril. Rasanya sudah mendingan kan?"
        roni "Iya Lio! Terima kasih banyak, sekarang perihnya berkurang dan rasanya nyaman sekali."

    # --- INSIDEN VOLI ---
    play music "audio/bgm_action.mp3" fadeout 1.0 fadein 1.0
    scene bg_lapang_voli with fade
    show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show bima pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    bima "Arghhhh..... pergelanganku keseleoo. sakit Sekali...."
    
    # SOAL 5 
    "Soal 5: Penanganan tepat untuk keseleo pergelangan tangan Bima adalah?"
    $ jawab_voli_benar = False
    menu:
        "A. Pijat dan urut segera":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Bisa memperparah cedera."
        "B. Metode R.I.C.E":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} R.I.C.E adalah standar penanganan medis."
            $ score += 10
            $ jawab_voli_benar = True
        "C. Rendam air panas":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Gunakan es (dingin) untuk cedera baru."

    lio "Benda elastis terpasang dengan baik. Metode R.I.C.E (Rest, Ice, Compression, Elevation) adalah standar emas penanganan keseleo. Memijat bagian yang baru cedera sangat dilarang karena bisa memperparah peradangan!"

    if jawab_voli_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show bima happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Es dan perbannya sudah terpasang, Bima. Istirahatkan dulu Tanganmu yaa."
        bima "Terima kasih Lio! Pembengkakannya terasa mulai reda dan nyeri keseleonya sangat berkurang."

    # --- INSIDEN BASKET ---
    play music "audio/bgm_action.mp3" fadeout 1.0 fadein 1.0
    scene bg_lapang_basket with fade
    show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show dedi pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    narrator "BRAKKK..'Bola basket mengenai wajah dedi'"
    dedi "LIOOOOO....."
    dedi "Aduhh, Hidungku berdarahh"
    
    # SOAL 6 
    "Soal 6: Bagaimana posisi kepala yang benar saat Dedi mimisan?"
    $ jawab_basket_benar = False
    menu:
        "A. Tengadah ke atas":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Darah bisa masuk ke tenggorokan."
        "B. Berbaring telentang":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Darah bisa mengalir ke saluran napas."
        "C. Menunduk dan jepit hidung":
            play music "audio/bgm_school.mp3" fadeout 1.0 fadein 1.0
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Posisi aman agar darah tidak tertelan."
            $ score += 10
            $ jawab_basket_benar = True

    lio "Ingat, saat mimisan posisi kepala harus menunduk sambil menjepit cuping hidung. Mendongak sangat berbahaya karena darah bisa mengalir kembali ke saluran napas!"

    if jawab_basket_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show dedi happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Pendarahan hidungmu sudah berhenti total, Dedi. Tetap menunduk sedikit dulu ya."
        dedi "Wah, lega sekali! Terima kasih Lio, hidungku sudah nyaman dan pusingnya sudah hilang."

    lio "Semua di lapangan sudah tertangani. Mari kembali ke UKS, Pak."
    jump chapter2


#  CHAPTER 2: KASUS MENENGAH 

label chapter2:
    play music "audio/bgm_emergency.mp3" fadeout 1.0 fadein 1.0
    scene bg_depan_uks with fade
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    show lio neutral at Transform(zoom=0.55, xalign=0.0, yalign=1.0)

    "{b}== CHAPTER 2: Kasus Menengah =={/b}"
    sofyan "Lio, ada beberapa laporan insiden menengah hari ini. Mari kita periksa korban kram otot yang sudah dibawa masuk ke ruang UKS."

    # --- KASUS 1: KRAM OTOT ---
    scene bg_uks_menarik with fade
    show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show dika pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    dika "Aduh... Tangan saya kram sekali liooo, Tolong aku...."
    
    # SOAL 7
    "Soal 7: Apa tindakan yang benar untuk mengatasi kram Dika?"
    $ jawab_soal7_benar = False
    menu:
        "A. Regangkan perlahan & pijat ringan":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Membantu relaksasi otot secara alami."
            $ score += 10
            $ jawab_soal7_benar = True
        "B. Tarik paksa ototnya":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Bisa menyebabkan cedera otot."
        "C. Beri minum air es":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Tidak menyembuhkan kram otot."

    if jawab_soal7_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show dika happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Pijatan ringan dan peregangan perlahan akan membantu ototmu relaks kembali, Dika."
        dika "Syukurlah, kram di tanganku sudah jauh lebih baik dan tidak tegang lagi. Terima kasih Lio!"
    else:
        show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        with dissolve

    sofyan "Lio. Kram otot terjadi karena otot berkontraksi tiba-tiba secara berlebih. Tindakan meregangkan otot secara perlahan berlawanan arah dengan kram adalah cara terbaik untuk merelaksasikannya kembali."
    hide dika
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    sofyan "Lio, ada siswi yang sesak napas di koridor depan UKS. Ayo kita periksa."

    # --- KASUS 2: ASMA ---
    scene bg_depan_uks with fade
    show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show sari pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    sari "Hah... dada saya sesak sekali..."
    sari "Aku hampir tidak bisa bernapas..."
    
    # SOAL 8 
    "Soal 8: Langkah awal membantu Sari yang sesak napas?"
    $ jawab_soal8_benar = False
    menu:
        "A. Suruh lari-lari kecil":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Malah memperparah kondisi."
        "B. Posisikan duduk tegak & longgarkan pakaian":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Membantu pernapasan lebih lega."
            $ score += 10
            $ jawab_soal8_benar = True
        "C. Berikan minum kopi panas":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Tidak membantu pernapasan darurat."

    if jawab_soal8_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show sari happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Tarik napas dalam-dalam secara teratur ya, Sari. Pakaianmu yang ketat sudah kulonggarkan agar lebih lega."
        sari "Lega sekali rasanya... napasku sudah tidak sesak lagi. Terima kasih banyak, Lio!"
    else:
        show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        with dissolve

    sofyan "Penanganan yang tepat. Memosisikan penderita duduk tegak memberikan ruang maksimal bagi paru-paru untuk mengembang. Melonggarkan pakaian juga secara dramatis melegakan jalannya udara."
    hide sari
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    sofyan "Lio, baru saja ada laporan siswa terjatuh dan mengalami pendarahan di lapangan Basket. Kita harus ke sana sekarang!"

    # --- KASUS 3: PENDARAHAN ---
    scene bg_lapang_basket with fade
    show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show budi pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    budi "Darah di tangan saya keluar terus!"
    budi "LIOO CEPAT TANGANI SAYAA!!."
    
    # SOAL 9 
    "Soal 9: Cara menghentikan pendarahan pada luka Budi?"
    $ jawab_soal9_benar = False
    menu:
        "A. Cuci dengan alkohol":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Merusak jaringan luka."
        "B. Biarkan darah mengalir":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Berisiko kekurangan darah."
        "C. Tekan luka dengan kain bersih/kasa":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Penekanan membantu pembekuan darah."
            $ score += 10
            $ jawab_soal9_benar = True

    if jawab_soal9_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show budi happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Tekanan langsung pada luka dengan kasa steril ini akan membantu menghentikan darahnya, Budi."
        budi "Wah, darahnya benar-benar sudah berhenti mengalir! Terima kasih sudah menolongku, Lio!"
    else:
        show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        with dissolve

    sofyan "Menghentikan pendarahan luar harus dilakukan dengan metode penekanan langsung (direct pressure) menggunakan kain bersih atau kasa steril. Mengguyur alkohol langsung ke luka sangat dilarang karena merusak jaringan sel hidup."
    hide budi
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    sofyan "Kerja bagus. Oh, lihat! Eko mengalami dehidrasi setelah berjemur terlalu lama di lapangan. Ayo pindahkan dia ke tempat teduh!"

    # --- KASUS 4: DEHIDRASI / KELELAHAN PANAS ---
    scene bg_tempat_teduh with fade
    show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show eko pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    eko "Kepala saya pusing, badan saya lemas sekali..."
    lio "Eko terlalu lama di bawah terik matahari."

    # SOAL 10
    "Soal 10: Apa pertolongan pertama untuk dehidrasi/kelelahan panas?"
    $ jawab_soal10_benar = False
    menu:
        "A. Bawa ke tempat teduh & beri minum air putih sedikit-sedikit":
            play sound "audio/correct.wav"
            "{color=#69F0AE}Benar!{/color} Mendinginkan suhu tubuh dan rehidrasi."
            $ score += 10
            $ jawab_soal10_benar = True
        "B. Beri minuman bersoda":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Kafein/gula tinggi tidak baik untuk hidrasi."
        "C. Suruh push-up agar bugar":
            play sound "audio/incorrect.mp3"
            "{color=#FF6B6B}Salah!{/color} Sangat berbahaya saat tubuh lemas."

    if jawab_soal10_benar:
        show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        show eko happy at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
        with dissolve
        lio "Ini minum airnya sedikit demi sedikit ya, Eko. Istirahat dulu di tempat teduh ini agar tubuhmu kembali segar."
        eko "Badanku rasanya jauh lebih segar sekarang dan pusingnya sudah hilang. Terima kasih, Lio!"
    else:
        show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
        with dissolve

    sofyan "Kelelahan panas (heat exhaustion) harus diatasi dengan memindahkan korban ke tempat sejuk, mendinginkan tubuhnya, dan memberikan air minum sedikit demi sedikit untuk memulihkan kadar cairan tubuh."
    hide eko
    show sofyan happy at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    sofyan "Semua penanganan hari ini selesai dengan baik. Ayo kita kembali ke ruang UKS."
    jump ending


#  ENDING: EVALUASI AKHIR

label ending:
    scene bg_uks_menarik with fade
    show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show sofyan happy at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    "{b}=== REKAP HASIL AKHIR ==={/b}"
    "Total Skor: [score] / 100"

    if score == 100:
        ## Ending Emas - Skor Sempurna
        stop music fadeout 1.0
        $ renpy.movie_cutscene("ending_emas.webm")
        play music "audio/bgm_victory.mp3"
        sofyan "Luar biasa! Skor sempurna! Kamu adalah HERO P3K SEJATI!"
        "🏆 Selamat! Kamu mendapatkan {b}LENCANA EMAS{/b}!"
    elif score >= 70:
        ## Ending Perak - Skor Cukup Baik
        stop music fadeout 1.0
        $ renpy.movie_cutscene("ending_perak.webm")
        play music "audio/bgm_victory.mp3"
        sofyan "Bagus sekali, Lio. Kamu sudah sangat memahami materi."
        "🥈 Kamu mendapatkan {b}LENCANA PERAK{/b}!"
    else:
        ## Ending Coba Lagi - Skor Kurang
        stop music fadeout 1.0
        $ renpy.movie_cutscene("ending_coba_lagi.webm")
        play music "audio/bgm_school.mp3"
        sofyan "Kamu masih perlu belajar lagi. Jangan menyerah!"
        "❌ Silakan coba lagi untuk hasil lebih baik."

    "--- TERIMA KASIH TELAH MEMAINKAN FIRST AID HERO ---"
    return

# --- Screen Pilihan Gambar (Soal 1) ---
screen image_choice_screen():
    # Semitransparent dark overlay
    add Solid("#000000a0")
    
    # Title Header
    vbox:
        xalign 0.5
        yalign 0.15
        spacing 10
        text "Pilih Alat yang Tepat" size 42 color "#FFE082" bold True xalign 0.5
        text "Gunakan salah satu alat di bawah untuk menutup luka terbuka" size 26 color "#ffffff" xalign 0.5
        
    # Choice Containers
    hbox:
        xalign 0.5
        yalign 0.50
        spacing 40
        
        # Kapas Biasa
        vbox:
            spacing 15
            xalign 0.5
            imagebutton:
                idle Transform("images/kapas_biasa_idle.png", size=(260, 260))
                hover Transform("images/kapas_biasa_hover.png", size=(260, 260))
                action Return("A")
                at choice_zoom
            text "Kapas Biasa" size 26 color "#ffffff" xalign 0.5 bold True
            
        # Kasa Steril
        vbox:
            spacing 15
            xalign 0.5
            imagebutton:
                idle Transform("images/kasa_steril_idle.png", size=(260, 260))
                hover Transform("images/kasa_steril_hover.png", size=(260, 260))
                action Return("B")
                at choice_zoom
            text "Kasa Steril" size 26 color "#ffffff" xalign 0.5 bold True
            
        # Tisu Wajah
        vbox:
            spacing 15
            xalign 0.5
            imagebutton:
                idle Transform("images/tisu_wajah_idle.png", size=(260, 260))
                hover Transform("images/tisu_wajah_hover.png", size=(260, 260))
                action Return("C")
                at choice_zoom
            text "Tisu Wajah" size 26 color "#ffffff" xalign 0.5 bold True

# Zoom Transition
transform choice_zoom:
    on hover:
        ease 0.15 zoom 1.05
    on idle:
        ease 0.15 zoom 1.00
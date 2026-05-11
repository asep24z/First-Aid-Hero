##  FIRST AID HERO - Game Edukasi P3K SMP
##  Refactored Edition - 10 Soal Acak (100 Poin)


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

# --- Backgrounds ---
image bg_lapangan       = "images/bg_lapangan.jpg"
image bg_uks            = "images/bg_uks.jpg"
image bg_lapang_basket  = "images/bg_lapang_basket.jpeg"
image bg_lapang_futsal  = "images/bg_lapang_futsal.jpeg"
image bg_lapang_voli    = "images/bg_lapang_voli.jpeg"

# --- Sprites Lio ---
image lio neutral = "images/lio_neutral.png"
image lio happy   = "images/lio_happy.png"
image lio serious = "images/lio_serious.png"
image lio shocked = "images/lio_shocked.png"

# --- Sprites Pak Sofyan ---
image sofyan neutral = "images/sofyan_neutral.png"
image sofyan happy   = "images/sofyan_happy.png"
image sofyan serious = "images/sofyan_serious.png"

# --- Sprites Korban ---
image roni pain    = "images/roni_pain.png"
image bima pain    = "images/bima_pain.png"
image dedi pain    = "images/dedi_pain.png"
image dika pain    = "images/korban_pain.png"
image sari pain    = "images/korban_pain.png"
image budi pain    = "images/korban_pain.png"
image eko pain     = "images/korban_pain.png"

default score = 0


#  Intro Video
label splashscreen:
    $ renpy.movie_cutscene("intro.webm")
    return

# ============================================================
#  START GAME
# ============================================================
label start:
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
    menu:
        "A. Kapas biasa":
            "{color=#FF6B6B}Salah!{/color} Kapas meninggalkan serat di luka."
        "B. Kasa Steril":
            "{color=#69F0AE}Benar!{/color} Kasa steril adalah pilihan yang tepat."
            $ score += 10
        "C. Tisu wajah":
            "{color=#FF6B6B}Salah!{/color} Tisu tidak steril dan mudah hancur."

    # SOAL 2 
    "Soal 2: Bagaimana cara benar menggunakan antiseptik?"
    menu:
        "A. Oleskan di area pinggir luka":
            "{color=#69F0AE}Benar!{/color} Cukup di sekitar tepi luka."
            $ score += 10
        "B. Tuang langsung ke dalam luka":
            "{color=#FF6B6B}Salah!{/color} Bisa merusak jaringan sel baru."
        "C. Campur dengan air sabun":
            "{color=#FF6B6B}Salah!{/color} Antiseptik digunakan tanpa dicampur sabun."

    # SOAL 3 
    "Soal 3: Apa fungsi Cold Pack?"
    menu:
        "A. Menghangatkan otot":
            "{color=#FF6B6B}Salah!{/color} Cold pack bersifat dingin."
        "B. Membersihkan kotoran":
            "{color=#FF6B6B}Salah!{/color} Itu fungsi irigasi air bersih."
        "C. Mengurangi bengkak dan nyeri":
            "{color=#69F0AE}Benar!{/color} Membantu menyempitkan pembuluh darah."
            $ score += 10

    sofyan "Bagus! Sekarang ke lapangan, sepertinya ada insiden!"
    
    # --- INSIDEN FUTSAL ---
    scene bg_lapang_futsal with fade
    show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show roni pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    
    # SOAL 4 
    "Soal 4: Apa langkah pertama untuk menangani luka lecet Roni?"
    menu:
        "A. Cuci dengan air mengalir":
            "{color=#69F0AE}Benar!{/color} Irigasi kotoran terlebih dahulu."
            $ score += 10
        "B. Langsung tutup kasa":
            "{color=#FF6B6B}Salah!{/color} Luka harus dibersihkan dulu."
        "C. Oleskan pasta gigi":
            "{color=#FF6B6B}Salah!{/color} Sangat tidak dianjurkan untuk luka."

    # --- INSIDEN VOLI ---
    scene bg_lapang_voli with fade
    show lio serious at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show bima pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    
    # SOAL 5 
    "Soal 5: Penanganan tepat untuk keseleo kaki Bima adalah?"
    menu:
        "A. Pijat dan urut segera":
            "{color=#FF6B6B}Salah!{/color} Bisa memperparah cedera."
        "B. Metode R.I.C.E":
            "{color=#69F0AE}Benar!{/color} R.I.C.E adalah standar penanganan medis."
            $ score += 10
        "C. Rendam air panas":
            "{color=#FF6B6B}Salah!{/color} Gunakan es (dingin) untuk cedera baru."

    # --- INSIDEN BASKET ---
    scene bg_lapang_basket with fade
    show lio shocked at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show dedi pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    
    # SOAL 6 
    "Soal 6: Bagaimana posisi kepala yang benar saat Dedi mimisan?"
    menu:
        "A. Tengadah ke atas":
            "{color=#FF6B6B}Salah!{/color} Darah bisa masuk ke tenggorokan."
        "B. Berbaring telentang":
            "{color=#FF6B6B}Salah!{/color} Darah bisa mengalir ke saluran napas."
        "C. Menunduk dan jepit hidung":
            "{color=#69F0AE}Benar!{/color} Posisi aman agar darah tidak tertelan."
            $ score += 10

    lio "Semua di lapangan sudah tertangani. Mari kembali ke UKS, Pak."
    jump chapter2


#  CHAPTER 2: KASUS MENENGAH 

label chapter2:
    scene bg_uks with fade
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)
    show lio neutral at Transform(zoom=0.55, xalign=0.0, yalign=1.0)

    "{b}== CHAPTER 2: Kasus Menengah =={/b}"
    sofyan "Lio, banyak siswa yang butuh bantuan di UKS. Mari kita tangani satu per satu."

    # --- KASUS 1: KRAM OTOT ---
    hide sofyan
    show dika pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    dika "Aduh... Kaki saya kram sekali!"
    
    # SOAL 7
    "Soal 7: Apa tindakan yang benar untuk mengatasi kram Dika?"
    menu:
        "A. Regangkan perlahan & pijat ringan":
            "{color=#69F0AE}Benar!{/color} Membantu relaksasi otot secara alami."
            $ score += 10
        "B. Tarik paksa ototnya":
            "{color=#FF6B6B}Salah!{/color} Bisa menyebabkan cedera otot."
        "C. Beri minum air es":
            "{color=#FF6B6B}Salah!{/color} Tidak menyembuhkan kram otot."
    hide dika
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    # --- KASUS 2: ASMA ---
    hide sofyan
    show sari pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    sari "Hah... dada saya sesak sekali..."
    
    # SOAL 8 
    "Soal 8: Langkah awal membantu Sari yang sesak napas?"
    menu:
        "A. Suruh lari-lari kecil":
            "{color=#FF6B6B}Salah!{/color} Malah memperparah kondisi."
        "B. Posisikan duduk tegak & longgarkan pakaian":
            "{color=#69F0AE}Benar!{/color} Membantu pernapasan lebih lega."
            $ score += 10
        "C. Berikan minum kopi panas":
            "{color=#FF6B6B}Salah!{/color} Tidak membantu pernapasan darurat."
    hide sari
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    # --- KASUS 3: PENDARAHAN ---
    hide sofyan
    show budi pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    budi "Darah di tangan saya keluar terus!"
    
    # SOAL 9 
    "Soal 9: Cara menghentikan pendarahan pada luka Budi?"
    menu:
        "A. Cuci dengan alkohol":
            "{color=#FF6B6B}Salah!{/color} Merusak jaringan luka."
        "B. Biarkan darah mengalir":
            "{color=#FF6B6B}Salah!{/color} Berisiko kekurangan darah."
        "C. Tekan luka dengan kain bersih/kasa":
            "{color=#69F0AE}Benar!{/color} Penekanan membantu pembekuan darah."
            $ score += 10
    hide budi
    show sofyan serious at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    # --- KASUS 4: DEHIDRASI / KELELAHAN PANAS ---
    hide sofyan
    show eko pain at Transform(zoom=0.5, xalign=1.0, yalign=1.0)
    eko "Kepala saya pusing, badan saya lemas sekali..."
    lio "Eko terlalu lama di bawah terik matahari."

    # SOAL 10
    "Soal 10: Apa pertolongan pertama untuk dehidrasi/kelelahan panas?"
    menu:
        "A. Bawa ke tempat teduh & beri minum air putih sedikit-sedikit":
            "{color=#69F0AE}Benar!{/color} Mendinginkan suhu tubuh dan rehidrasi."
            $ score += 10
        "B. Beri minuman bersoda":
            "{color=#FF6B6B}Salah!{/color} Kafein/gula tinggi tidak baik untuk hidrasi."
        "C. Suruh push-up agar bugar":
            "{color=#FF6B6B}Salah!{/color} Sangat berbahaya saat tubuh lemas."
    hide eko
    show sofyan happy at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    sofyan "Lio, semua tugasmu sudah selesai dengan sangat baik!"
    jump ending


#  ENDING: EVALUASI AKHIR

label ending:
    play music "audio/bgm_victory.mp3"
    scene bg_uks with fade
    show lio happy at Transform(zoom=0.55, xalign=0.0, yalign=1.0)
    show sofyan happy at Transform(zoom=0.55, xalign=1.0, yalign=1.0)

    "{b}=== REKAP HASIL AKHIR ==={/b}"
    "Total Skor: [score] / 100"

    if score == 100:
        sofyan "Luar biasa! Skor sempurna! Kamu adalah HERO P3K SEJATI!"
        "🏆 Selamat! Kamu mendapatkan {b}LENCANA EMAS{/b}!"
    elif score >= 70:
        sofyan "Bagus sekali, Lio. Kamu sudah sangat memahami materi."
        "🥈 Kamu mendapatkan {b}LENCANA PERAK{/b}!"
    else:
        sofyan "Kamu masih perlu belajar lagi. Jangan menyerah!"
        "❌ Silakan coba lagi untuk hasil lebih baik."

    "--- TERIMA KASIH TELAH MEMAINKAN FIRST AID HERO ---"
    return
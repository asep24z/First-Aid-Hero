## ============================================================
##  FIRST AID HERO - Game Edukasi P3K SMP
##  Script Utama (script.rpy)
## ============================================================

# --- DEKLARASI KARAKTER ---
define lio    = Character("Lio",    color="#4FC3F7")
define sofyan = Character("Pak Sofyan", color="#EF9A9A")
define roni   = Character("Roni",   color="#A5D6A7")
define bima   = Character("Bima",   color="#FFE082")
define dedi   = Character("Dedi",   color="#CE93D8")
define narrator = Character(None)

# --- DEFINISI GAMBAR (TEMPLATE & DUMMY) ---
# Lio
image lio neutral = "images/lio_neutral.png"
image lio happy   = "images/lio_happy.png"
image lio serious = "images/lio_serious.png"
image lio shocked = "images/lio_shocked.png"

# Pak Sofyan
image sofyan neutral = "images/sofyan_neutral.png"
image sofyan happy   = "images/sofyan_happy.png"
image sofyan serious = "images/sofyan_serious.png"

# Korban-korban
image roni neutral = "images/roni_neutral.png"
image roni pain    = "images/roni_pain.png"
image roni happy   = "images/roni_happy.png"

image bima neutral = "images/bima_neutral.png"
image bima pain    = "images/bima_pain.png"
image bima happy   = "images/bima_happy.png"

image dedi neutral = "images/dedi_neutral.png"
image dedi pain    = "images/dedi_pain.png"
image dedi happy   = "images/dedi_happy.png"

image korban neutral     = "images/korban_neutral.png"
image korban pain        = "images/korban_pain.png"
image korban unconscious = "images/korban_unconscious.png"

# Backgrounds
image bg_lapangan = "images/bg_lapangan.jpg"
image bg_uks      = "images/bg_uks.jpg"

# --- TRANSFORMASI UNTUK POSISI DIALOG (1920x1080) ---
# Karakter kiri: Berada di 25% lebar layar dari kiri
transform sprite_left:
    xcenter 0.25
    ypos 1080
    yanchor 1.0
    zoom 0.6

# Karakter kanan: Berada di 75% lebar layar dari kiri
transform sprite_right:
    xcenter 0.75
    ypos 1080
    yanchor 1.0
    zoom 0.6

# --- VARIABEL GLOBAL ---
default score = 0

# ============================================================
#  START
# ============================================================
label start:
    play music "audio/bgm_school.mp3"
    scene bg_lapangan with fade
    show lio neutral at sprite_left

    narrator "Selamat datang di FIRST AID HERO!"
    narrator "Game edukasi Pertolongan Pertama pada Kecelakaan (P3K) untuk siswa SMP."
    narrator "Kamu akan berperan sebagai LIO, anggota PMR yang bertugas di Event Classmeet."

    lio "Namaku Lio. Hari ini aku bertugas menjaga pos P3K di lapangan sekolah."
    lio "Pak Sofyan sudah memintaku siap siaga. Ayo mulai!"

    jump chapter1

# ============================================================
#  CHAPTER 1 - PENGENALAN ALAT P3K
# ============================================================
label chapter1:
    scene bg_uks with fade
    show sofyan neutral at sprite_right
    show lio neutral at sprite_left

    "{b}== CHAPTER 1: Pengenalan Alat P3K =={/b}"

    sofyan "Lio, sebelum kamu bertugas, kita periksa dulu isi tas P3K kita."
    lio "Siap, Pak Sofyan!"
    sofyan "Perhatikan baik-baik. Ini penting!"

    sofyan "Pertama: {b}Kasa Steril{/b}. Digunakan untuk menutup luka. BUKAN kapas, ya!"
    sofyan "Kapas bisa meninggalkan serat di luka dan memperburuk kondisi."

    sofyan "Kedua: {b}Antiseptik{/b} seperti Betadine atau Povidone Iodine."
    sofyan "Oleskan HANYA di area pinggir luka, bukan langsung di dalam luka terbuka."

    sofyan "Ketiga: {b}Plaster/Perban{/b} untuk membalut dan melindungi luka setelah dibersihkan."

    sofyan "Keempat: {b}Cold Pack (Kompres Dingin){/b}. Fungsinya untuk mengurangi bengkak dan nyeri."
    lio "Wah, ternyata banyak yang harus diperhatikan, Pak!"
    sofyan "Betul! Sekarang, mari kita uji pemahamanmu."

    jump quiz_chapter1

label quiz_chapter1:
    "{b}=== KUIS CHAPTER 1 ==={/b}"

    # SOAL 1
    "Soal 1: Apa yang sebaiknya digunakan untuk menutup luka terbuka?"
    menu:
        "A. Kapas biasa":
            "{color=#FF6B6B}Salah!{/color} Kapas bisa meninggalkan serat di luka dan menyebabkan infeksi."
        "B. Kasa Steril":
            "{color=#69F0AE}Benar!{/color} Kasa steril adalah pilihan yang tepat untuk menutup luka."
            $ score += 20
        "C. Tisu":
            "{color=#FF6B6B}Salah!{/color} Tisu tidak steril dan bisa mengkontaminasi luka."

    # SOAL 2
    "Soal 2: Bagaimana cara yang benar menggunakan antiseptik pada luka?"
    menu:
        "A. Oleskan langsung ke seluruh bagian dalam luka":
            "{color=#FF6B6B}Salah!{/color} Antiseptik bisa merusak jaringan sel baru jika dioleskan langsung ke dalam luka."
        "B. Teteskan sebanyak-banyaknya":
            "{color=#FF6B6B}Salah!{/color} Penggunaan berlebihan tidak dianjurkan dan bisa mengiritasi kulit."
        "C. Oleskan hanya di area pinggir luka":
            "{color=#69F0AE}Benar!{/color} Antiseptik cukup dioleskan di sekitar tepi luka untuk mencegah infeksi."
            $ score += 20

    # SOAL 3
    "Soal 3: Apa fungsi utama Cold Pack dalam P3K?"
    menu:
        "A. Menghangatkan otot yang kaku":
            "{color=#FF6B6B}Salah!{/color} Cold pack bersifat dingin, bukan panas. Untuk menghangatkan gunakan heat pack."
        "B. Mengurangi bengkak dan nyeri pada cedera":
            "{color=#69F0AE}Benar!{/color} Cold pack membantu menyempitkan pembuluh darah sehingga bengkak berkurang."
            $ score += 20
        "C. Membersihkan luka dari kuman":
            "{color=#FF6B6B}Salah!{/color} Itu fungsi antiseptik, bukan cold pack."

    sofyan "Bagus! Kamu sudah paham dasarnya. Sekarang bersiaplah, Classmeet dimulai!"
    jump chapter2

# ============================================================
#  CHAPTER 2 - INSIDEN FUTSAL (LUKA LECET)
# ============================================================
label chapter2:
    play music "audio/bgm_action.mp3"
    scene bg_lapangan with fade
    show lio shocked at sprite_left
    show korban pain at sprite_right

    "{b}== CHAPTER 2: Insiden Futsal - Luka Lecet =={/b}"

    lio "..."
    "Tiba-tiba terdengar teriakan dari lapangan futsal!"
    show roni pain at sprite_right
    roni "Aduh! Kakiku lecet parah kena aspal!"
    lio "Tenang, Roni. Aku yang tangani!"

    scene bg_uks with fade
    show lio serious at sprite_left
    show roni pain at sprite_right

    lio "Oke, aku harus ingat prosedurnya. Luka lecet harus dibersihkan dulu."

    "Lio menghadapi situasi pertama. Apa yang harus dilakukan?"
    menu:
        "Langsung tutup luka dengan kasa tanpa dicuci":
            "{color=#FF6B6B}Salah!{/color} Berbahaya! Kotoran dan kuman yang tertinggal bisa menyebabkan infeksi serius seperti tetanus."
            lio "Eh, sepertinya aku salah langkah..."
            jump luka_lecet_correct
        "Irigasi (cuci) luka dengan air bersih mengalir dulu":
            "{color=#69F0AE}Benar!{/color} Irigasi adalah langkah PERTAMA yang wajib dilakukan!"
            $ score += 20
            jump luka_lecet_prosedur

label luka_lecet_correct:
    lio "Aku harus cuci lukanya dulu dengan air mengalir."
    jump luka_lecet_prosedur

label luka_lecet_prosedur:
    lio "Aku bilas lukanya dengan air bersih mengalir selama beberapa detik..."
    lio "Sekarang oleskan antiseptik di pinggir lukanya..."
    lio "Terakhir, tutup dengan kasa steril dan rekatkan plaster."
    roni "Wah, sudah tidak sakit lagi! Makasih, Lio!"
    show sofyan happy at sprite_right
    sofyan "Bagus, Lio! Ingat prosedurnya: Irigasi → Antiseptik → Tutup Kasa."
    stop music fadeout 1.0
    jump chapter3

# ============================================================
#  CHAPTER 3 - INSIDEN VOLI (KESELEO/TERKILIR)
# ============================================================
label chapter3:
    play music "audio/bgm_action.mp3"
    scene bg_lapangan with fade
    show lio shocked at sprite_left
    show bima pain at sprite_right

    "{b}== CHAPTER 3: Insiden Voli - Keseleo =={/b}"

    bima "ADUH! Pergelangan kakiku!"
    lio "Bima! Apa yang terjadi?"
    bima "Waktu lompat smash, kakiku terpelintir. Sakiiit!"
    lio "Oke, aku ingat! Ini harus ditangani dengan metode R.I.C.E!"

    scene bg_uks with fade
    show lio serious at sprite_left
    show bima pain at sprite_right

    "Langkah apa yang pertama harus dilakukan pada keseleo?"
    menu:
        "Pijat dan urut bagian yang keseleo agar cepat sembuh":
            "{color=#FF6B6B}SALAH dan BERBAHAYA!{/color}"
            "Memijat cedera yang masih baru justru akan memperparah robekan ligamen dan memperluas area pendarahan dalam. Jangan pernah lakukan ini!"
            jump rice_method
        "Terapkan metode R.I.C.E":
            "{color=#69F0AE}Benar!{/color} R.I.C.E adalah standar penanganan keseleo yang diakui medis."
            $ score += 20
            jump rice_method

label rice_method:
    show sofyan serious at sprite_right
    sofyan "Baik, mari kita terapkan R.I.C.E dengan benar!"
    sofyan "{b}R - REST{/b}: Istirahatkan bagian yang cedera. Jangan dipaksakan bergerak!"
    lio "Bima, kamu harus istirahat dulu. Jangan berdiri dulu."
    sofyan "{b}I - ICE{/b}: Kompres dengan cold pack atau es yang dibungkus kain. 20 menit on, 20 menit off."
    lio "Ini cold pack-nya, Bima. Jangan langsung tempel es ke kulit, ya."
    sofyan "{b}C - COMPRESSION{/b}: Balut dengan perban elastis untuk mengurangi bengkak."
    lio "Aku balut pelan-pelan ya, Bima."
    sofyan "{b}E - ELEVATION{/b}: Angkat kaki lebih tinggi dari posisi jantung."
    lio "Nah, sandarkan kakimu di kursi ini supaya lebih tinggi."
    sofyan "INGAT! Dilarang keras memijat atau mengurut cedera baru. Ini bisa memperparah kondisi!"
    bima "Oke, oke. Aku mengerti. Terima kasih!"
    stop music fadeout 1.0
    jump chapter4

# ============================================================
#  CHAPTER 4 - INSIDEN BASKET (MIMISAN)
# ============================================================
label chapter4:
    play music "audio/bgm_action.mp3"
    scene bg_lapangan with fade
    show lio shocked at sprite_left
    show dedi pain at sprite_right

    "{b}== CHAPTER 4: Insiden Basket - Mimisan =={/b}"

    dedi "Liooo! Hidungku berdarah!"
    lio "Dedi! Mimisan? Tenang, aku bantu."
    lio "Hm, apa posisi yang benar untuk mimisan?"

    "Bagaimana posisi kepala yang benar saat mimisan?"
    menu:
        "Kepala ditengadahkan (melihat ke atas)":
            "{color=#FF6B6B}SALAH!{/color}"
            "Menengadahkan kepala menyebabkan darah mengalir ke tenggorokan dan bisa tersedak, bahkan masuk ke saluran napas. Sangat berbahaya!"
            jump mimisan_correct
        "Kepala menunduk ke depan dan jepit cuping hidung":
            "{color=#69F0AE}Benar!{/color} Ini posisi yang paling aman untuk menangani mimisan."
            $ score += 20
            jump mimisan_prosedur

label mimisan_correct:
    lio "Oh benar! Harus menunduk, bukan menengadah!"
    jump mimisan_prosedur

label mimisan_prosedur:
    lio "Dedi, duduk tegak ya. Condongkan kepala sedikit ke depan."
    lio "Sekarang jepit cuping hidungmu dengan jari telunjuk dan ibu jari selama 10-15 menit."
    lio "Bernapas lewat mulut ya."
    dedi "Iya, Lio..."
    show sofyan happy at sprite_right
    sofyan "Betul sekali, Lio! Posisi menunduk mencegah darah tertelan atau masuk ke paru-paru."
    sofyan "Jika dalam 20 menit tidak berhenti, segera bawa ke dokter."
    dedi "Sudah berhenti! Terima kasih, Lio!"
    stop music fadeout 1.0
    jump chapter5

# ============================================================
#  CHAPTER 5 - INSIDEN DAPUR & UPACARA
# ============================================================
label chapter5:
    play music "audio/bgm_emergency.mp3"
    scene bg_uks with fade
    show lio neutral at sprite_left

    "{b}== CHAPTER 5: Luka Bakar & Pingsan =={/b}"

    "Lio dipanggil ke kantin karena ada insiden di sana."
    lio "Ada apa lagi ini?"

    # --- BAGIAN LUKA BAKAR ---
    "Seorang siswa tidak sengaja menyentuh panci panas di kantin!"
    show korban pain at sprite_right
    "Siswa: Aduh! Tanganku kena panci panas!"

    "Apa pertolongan pertama yang tepat untuk luka bakar ringan?"
    menu:
        "Oleskan odol (pasta gigi) atau mentega":
            "{color=#FF6B6B}SALAH!{/color}"
            "Odol dan mentega menyimpan panas di dalam kulit dan bisa menyebabkan infeksi. Pantang dilakukan!"
            jump luka_bakar_correct
        "Alirkan air bersih dingin mengalir selama 10-20 menit":
            "{color=#69F0AE}Benar!{/color} Air mengalir dingin adalah pertolongan pertama terbaik untuk luka bakar ringan."
            $ score += 20
            jump luka_bakar_prosedur

label luka_bakar_correct:
    lio "Yang benar adalah mengalirkan air dingin!"
    jump luka_bakar_prosedur

label luka_bakar_prosedur:
    lio "Mari kita alirkan air dingin di bawah keran selama 15 menit ya."
    lio "Jangan disikat, cukup dialiri air mengalir."
    show sofyan serious at sprite_right
    sofyan "Bagus! Ingat: air mengalir, bukan air es. Air es bisa merusak jaringan."
    sofyan "Dan JANGAN pakai odol, mentega, kecap, atau bahan rumahan lainnya!"

    # --- BAGIAN PINGSAN ---
    scene bg_lapangan with fade
    show lio shocked at sprite_left
    show sofyan serious at sprite_right

    "Saat upacara penutupan, seorang siswa tiba-tiba pingsan!"
    sofyan "Lio! Cepat tangani!"
    lio "Siap Pak!"

    "Bagaimana posisi yang benar untuk pasien yang pingsan?"
    menu:
        "Dudukkan pasien dan beri minum":
            "{color=#FF6B6B}Salah!{/color} Pasien yang pingsan tidak boleh langsung didudukkan atau diberi minum karena bisa tersedak."
            jump pingsan_correct
        "Baringkan dan angkat kaki 20-30 cm lebih tinggi dari jantung":
            "{color=#69F0AE}Benar!{/color} Ini disebut posisi syok. Meningkatkan aliran darah ke otak."
            $ score += 20
            jump pingsan_prosedur

label pingsan_correct:
    lio "Oh! Harus dibaringkan dengan kaki diangkat!"
    jump pingsan_prosedur

label pingsan_prosedur:
    lio "Baringkan di tempat yang teduh. Kaki diangkat sekitar 20-30 cm."
    lio "Longgarkan pakaian di leher dan dada agar tidak sesak."
    lio "Kipas-kipas untuk sirkulasi udara."
    sofyan "Pastikan saluran napasnya tidak tersumbat. Cek respons setiap 30 detik."
    "Siswa perlahan siuman..."
    show sofyan happy at sprite_right
    sofyan "Kerja bagus, Lio! Kamu sudah menangani semua insiden dengan baik hari ini."
    lio "Terima kasih, Pak Sofyan! Aku belajar banyak hari ini."
    jump ending

# ============================================================
#  ENDING & REKAP HASIL
# ============================================================
label ending:
    play music "audio/bgm_victory.mp3"
    scene bg_uks with fade
    show lio happy at sprite_left
    show sofyan happy at sprite_right

    # nvl clear removed
    "{b}=== REKAP HASIL AKHIR ==={/b}"
    "Total Poin Kamu: [score] / 160"

    if score >= 140:
        jump ending_hero
    elif score >= 80:
        jump ending_lulus
    else:
        jump ending_bad

label ending_hero:
    scene bg_lapangan with fade
    show lio happy at sprite_left
    show sofyan happy at sprite_right

    sofyan "Luar biasa, Lio! Kamu menjawab hampir semua pertanyaan dengan benar!"
    sofyan "Kamu layak mendapatkan gelar tertinggi: {b}HERO P3K SEJATI!{/b}"
    lio "Horeee! Terima kasih, Pak Sofyan!"
    "🏆 Selamat! Kamu mendapatkan {b}LENCANA EMAS{/b}!"
    "Kamu adalah pahlawan P3K sejati yang siap menolong kapan saja!"
    jump game_over

label ending_lulus:
    scene bg_lapangan with fade
    show lio happy at sprite_left
    show sofyan neutral at sprite_right

    sofyan "Bagus, Lio! Kamu sudah cukup memahami materi P3K dasar."
    sofyan "Terus belajar dan berlatih agar kamu semakin sigap!"
    lio "Siap, Pak! Aku akan terus belajar!"
    "🥈 Kamu mendapatkan {b}LENCANA PERAK{/b}!"
    "Kamu sudah Lulus! Namun masih ada materi yang perlu diperdalam."
    jump game_over

label ending_bad:
    scene bg_uks with fade
    show lio serious at sprite_left
    show sofyan serious at sprite_right

    sofyan "Hmm, sepertinya kamu masih perlu banyak belajar, Lio."
    sofyan "Jangan berkecil hati. P3K adalah ilmu yang harus dikuasai dengan baik."
    lio "Maaf, Pak. Aku akan belajar lebih giat lagi!"
    "❌ Kamu perlu mengulang materi P3K dari awal."
    "Jangan menyerah! Nyawa orang lain mungkin bergantung pada kemampuanmu."
    jump game_over

label game_over:
    # nvl clear removed
    "--- TERIMA KASIH TELAH MEMAINKAN FIRST AID HERO ---"
    "Ingat selalu: Pengetahuan P3K bisa menyelamatkan nyawa!"
    "Skor Akhirmu: [score] poin"
    return

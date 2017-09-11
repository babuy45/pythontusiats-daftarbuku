class Pegawai:
    def __init__(self, nama, gaji = 0):
        self.nama = nama
        self.gaji = gaji
    def tunjangan(self, persen):
        self.gaji = self.gaji + (self.gaji * persen)
    def kerja(self):
        print(self.nama, "Pekerjaanya")
    def __repr__(self):
        return "<Pegawai: nama = %s, gaji = %s>" % (self.nama, self.gaji)

class Koki(Pegawai):
    def __init__(self, nama):
        Pegawai.__init__(self, nama, 100000)
    def kerja(self):
        print(self.nama, "Membuat makanan")

class PizzaRobot(Koki):
    def __init__(self, nama):
        Koki.__init__(self, nama)
    def kerja(self):
        print(self.nama, "Membuat Pizza")

agus = PizzaRobot("Agus")
print(agus)
agus.kerja()
agus.tunjangan(0.10)
print(agus)
print

for kelas in Pegawai, Koki, PizzaRobot:
    objek = kelas(kelas.__name__)
    objek.kerja()
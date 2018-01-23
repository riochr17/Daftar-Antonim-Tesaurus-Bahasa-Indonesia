# Daftar Antonim Tesaurus Bahasa Indonesia

Membuat daftar pasangan antonim kata bahasa Indonesia melalui berkas pdf [Tesaurus Bahasa Indonesia](http://www.buku-e.lipi.go.id/utama.cgi?lihatarsip&dend001&1257716945).

## Pra-Proses

- teks `tesaurus-id.txt` merupakan isi tesaurus asli dalam format pdf yang di _copy-paste_ menggunakan CTRL+C dan CTRL+V dari pdf ke kakas pengubah teks (_text editor_)
- pada teks tersebut, bagian halaman pembuka di setiap bab dihapus dan setiap bab diberikan pembatas (_boundary_) tertentu.

## Proses

- `clean_t.py` memperbaiki bagian yang seharusnya satu baris terputus oleh baris baru.
- `antonim_t.py` mengambil hanya bagian defenisi yang memiliki antonim saja.
- `create_t_a.py` melakukan kombinasi pada setiap kata di defenisi dan antonim sehingga menghasilkan daftar pasangan antonim

## Minimum Requirement

- Lingkungan yang dapat menjalankan _script_ `linux/bash`
- Python 2.7 atau terbaru

## Usage

`sh lala.sh`

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

[Tesaurus Bahasa Indonesia](http://www.buku-e.lipi.go.id/utama.cgi?lihatarsip&dend001&1257716945)

## License

?
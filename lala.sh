echo "> Mulai.";
python clean_t.py;
echo "clean_t.py \t-> clean-tesaurus.txt";
python antonim_t.py;
echo "antonim_t.py \t-> tesaurus-per-antonim.txt";
python create_t_a.py;
echo "create_t_a.py \t-> hasil-pasangan-antonim-id.txt";
echo "> Selesai.";

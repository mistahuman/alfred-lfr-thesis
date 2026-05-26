for ifile in *.png
  do
  filename=${ifile%.*g}
  convert $ifile -quality 100 -trim $filename-t.png
done

tmem=$(free | awk 'NR==2 {print $2}')
umem=$(free | awk 'NR==2 {print $3}')

echo "$tmem" >> ./stream/file
echo "$umem" >> ./stream/file

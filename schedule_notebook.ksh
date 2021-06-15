while true
do
current_time=`date`
echo ${current_time}
echo "checking slots at $current_time"
jupyter nbconvert --to notebook --execute COWIN-SLOTS.ipynb
echo " Last Run completed Going to sleep for 30sec"
sleep 30
done

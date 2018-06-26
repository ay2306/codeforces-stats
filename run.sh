ret=$#
# if [ $ret -eq 0 ]
# then
#     echo "YES"
# else 
#     echo "NO"
# fi
# echo $#
if [ $ret -eq 0 ] 
then
    echo "Please enter handle"
else
    python code1.py $1
    ret=$?
    if [ $ret -eq 1 ]
    then
        # echo "HELLO"
        octave make_pie.m
    fi
fi
start=$1
step=$2
end=$3

for ctr in $(seq $start $step $end)
do
    cp jobTemplate2.sh job$ctr.sh
    chmod u+x job$ctr.sh
    sed -i "s/CTR/$ctr/g" job$ctr.sh

    while [ 1 -gt 0 ]
    do
        qsub -q localgrid -o out$ctr.stdout -e err$ctr.stderr job$ctr.sh
        if [ $? == 0 ]
        then
            break
        fi
    done

done

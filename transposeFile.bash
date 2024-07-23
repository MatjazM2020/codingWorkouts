awk '{
    for(i = 1; i<= NF; i++){
        if(!arr[i]){
            arr[i] = $i
            }
        else{
            arr[i] = arr[i]" "$i
            }
        }
    }END{
        for(i = 1; i<= length(arr); i++){
            print(arr[i])
        }
    }' file.txt





# https://leetcode.com/problems/transpose-file/description/
# Given a text file file.txt, transpose its content.
# You may assume that each row has the same number of columns, and each field is separated by the ' ' character.
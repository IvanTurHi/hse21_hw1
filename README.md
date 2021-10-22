# hse21_hw1
Создаем папку для дз после чего копируем туда исходные файлы по ссылке
>mkdir hw1  
>cd hw1  
>ls -1 /usr/share/data-minor-bioinf/assembly/* | xargs -tI{} ln -s {}  

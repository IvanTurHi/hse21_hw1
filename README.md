# hse21_hw1
Создаем папку для дз после чего копируем туда исходные файлы по ссылке
>mkdir hw1  
>cd hw1  
>ls -1 /usr/share/data-minor-bioinf/assembly/* | xargs -tI{} ln -s {}  
  
Выбираем случайные чтения, указывая для парметра -s месяц и дату рождения
>seqtk sample -s602 oil_R1.fastq 5000000 > re_oil_R1.fastq  
>seqtk sample -s602 oil_R2.fastq 5000000 > re_oil_R2.fastq  
>seqtk sample -s602 oilMP_S4_L001_R1_001.fastq 1500000 > re_oilMP_S4_L001_R1_001.fastq  
>seqtk sample -s602 oilMP_S4_L001_R2_001.fastq 1500000 > re_oilMP_S4_L001_R2_001.fastq  

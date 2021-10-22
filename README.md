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

удаляем ссылки на файлы, поскольку больше с ними не будем работать
>rm oil_R1.fastq  
>rm oil_R2.fastq  
>rm oilMP_S4_L001_R1_001.fastq  
>rm oilMP_S4_L001_R2_001.fastq  

Оцениваем качество при помощи fastqc и сохраняем результаты в папку fastqc
>mkdir fastqc  
>ls *.fastq | xargs -P 4 -tI{} fastqc -o fastqc {}  

Собираем все в один большой файл
>mkdir multiqc  
>multiqc -o multiqc fastqc  

Далее скачиваем FileZilla и при помощи подключения по ключу скачиваем нужные файлы

Удаляем праймеры при помощи platanus
>platanus_trim re_oil_R1.fastq re_oil_R2.fastq  
>platanus_internal_trim re_oilMP_S4_L001_R1_001.fastq re_oilMP_S4_L001_R2_001.fastq  

Удаляем ненужные файлы
>rm re_oil_R1.fastq  
>rm re_oil_R2.fastq  
>rm re_oilMP_S4_L001_R1_001.fastq  
>rm re_oilMP_S4_L001_R2_001.fastq  

Опять пользуемся прораммаи fastqc и multiqc, однако уже для подчищенных файлов
>mkdir trimmed_fastqc  
>ls *| xargs -P 4 -tI{} fastqc -o trimmed_fastqc {}  
>mkdir trimmed_multiqc  
>multiqc -o trimmed_multiqc trimmed_fastqc  

# Сравним полученные данные multiqc в формате До/После

Уменьшилась длина последовательностей
![image](https://user-images.githubusercontent.com/65420132/138486226-3136067a-f7cd-404b-a8bb-ade573674643.png)  

Улучшилось качество чтений
![image](https://user-images.githubusercontent.com/65420132/138486913-ccfe5f6c-91df-4c34-bdd3-c0fbb79a883e.png)

И практически полностью удалены адаптеры
![image](https://user-images.githubusercontent.com/65420132/138487052-1ee2b872-d3d7-4db6-a612-85972a8b414f.png)

Сбор контигов
>time platanus assemble -o Poil -t 2 -m 28 -f re_oil_R1.fastq.trimmed re_oil_R2.fastq.trimmed 2> assembl.log  

Анализ контигов в collab
https://colab.research.google.com/drive/1RFcRNY3gqPANSa03XqZ_zVCMCXZtAlak#scrollTo=yo9RJaGtR96B

Сбор скаффолдов
>time platanus scaffold -o Poil -t 2 -c Poil_contig.fa -IP1 re_oil_R1.fastq.trimmed re_oil_R2.fastq.trimmed -OP2 re_oilMP_S4_L001_R1_001.fastq.int_trimmed re_oilMP_S4_L001_R2_001.fastq.int_trimmed 2> scaffold.log  

Анализ скаффолдов в collab
https://colab.research.google.com/drive/1EHq1iicIGNnaDpOiwcHHqXVmr9kPj0Yn#scrollTo=iV1r6SQteBHz  

Извлекаем самый длинный скаффолд
>echo scaffold1_len3832270_cov232 > buf.txt  
>seqtk subseq Poil_scaffold.fa buf.txt > MaxScaf.fa  

Анализируем наличие гэпов в самом длинном скаффолде
https://colab.research.google.com/drive/1mpAmN0bQItKjZOIdmVvAXS5LDfpu7SFy#scrollTo=reavCdy9gUM0  

Уменьшаем количество гэпов
>time platanus gap_close -o Poil -t 2 -c Poil_scaffold.fa -IP1 re_oil_R1.fastq.trimmed re_oil_R2.fastq.trimmed -OP2 re_oilMP_S4_L001_R1_001.fastq.int_trimmed re_oilMP_S4_L001_R2_001.fastq.int_trimmed 2> gapclose.log  

Опять вытаскиваем самый длинный скафолд
>echo scaffold1_cov232 > buf1.txt  
>seqtk subseq Poil_gapClosed.fa buf1.txt > MaxScaf_low_gep.fa  

Вновь анализируем наличие гэпов, но уже при помощи файла MaxScaf_low_gep.fa
https://colab.research.google.com/drive/1mpAmN0bQItKjZOIdmVvAXS5LDfpu7SFy#scrollTo=reavCdy9gUM0

Удаляем ненужные файлы
>rm *.fastq*  

# Дополнительное задание
В первом столбце исходыне результаты  
выбираем случайно 1 миллион чтений типа paired-end и 300 тфсяч чтений типа mate-pairs(результаты во втором столбце)  
выбираем случайно 200 тысяч чтений типа paired-end и 60 тфсяч чтений типа mate-pairs(результаты в третьем столбце)  

|  | 5M/1.5M | 1M/300k | 200k/60k |
| :---: | :---: | :---: | :---: |
| Общее количество скаффолдов | 75 | 154 | 10614 |
| Общая длина скаффолдов | 3876681 | 3856067 | 2653982 |
| Самый длинный скаффолд | 3832270 | 2969168 | 5006 |
| N50 |3832270 | 2969168 | 417 |
| Общая длина гэпов | 6446 | 13387 | 334 |
| Общее количество | 64| 104 | 14 |
| Общая длина гэпов после удаления | 1522 | 8069 | 0 |
| Общее количество гэпов после удаления | 7 | 32 | 0 |

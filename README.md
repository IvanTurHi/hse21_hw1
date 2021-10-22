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


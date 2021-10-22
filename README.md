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


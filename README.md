# cutadapt_batch
Cutadapt is a crucial tool for trimming adapters and contaminants from high-throughput sequencing data, typically requiring command-line interactions which might pose a challenge for users unfamiliar with Linux environments. To facilitate a more user-friendly experience, especially for beginners or those without extensive command-line expertise, a specialized script has been developed. This script automates the process of running Cutadapt for multiple samples, eliminating the need to manually input commands for each dataset.

How to use.

Mac/linux   
1. Download and install python3, then install easygui 
pip3 install easygui
2. Navigate to the folder with the fastq files using “cd” and get the folder path using “pwd” 
pwd
3. Run the script
python3 cutadapt_batch-mac-linux.py
4. In the pop up window, fill the required filds
![image](https://github.com/user-attachments/assets/7169807e-e17b-41ee-8a7b-10915c207a7f)
"Path of the DATA", fill the path just got from "pwd".
"Sequence of F primer" "Sequence of F primer", fill the primer sequence.
"Filename of any of R1 files", find any fastq file from read 1, and copy the whole file name here.

Windows   
1. Download and install python3, then install easygui 
pip3 install easygui
2. Navigate to the folder with the fastq files using “cd” and get the folder path using “pwd” 
cd
3. Run the script
python cutadapt_batch-windows.py
4. In the pop up window, fill the required filds
![image](https://github.com/user-attachments/assets/7169807e-e17b-41ee-8a7b-10915c207a7f)
"Path of the DATA", fill the path just got from "pwd".
"Sequence of F primer" "Sequence of F primer", fill the primer sequence.
"Filename of any of R1 files", find any fastq file from read 1, and copy the whole file name here.


# Map GMDN codes to EMDN Hierarchy
## General Information:
Program for mapping GMDN items to EMDN hierarchy using pre-trained LLM.
Built with the workflow from [Huggingface](https://huggingface.co/), so LLMs available on the Huggingface Hub work natively.

The [.venv](https://drive.google.com/file/d/16zKJRDp92oVkcUQ3yIZevieyb4OiJ0Fa/edit) directory contains a virtual Environment with all required dependencies.

### Run Locally

Clone the project

```bash
  git clone https://github.com/Kilanopi/GMDNtoEMDN
```

Go to the project directory

```bash
  cd GMDNtoEMDN
```
#### Preprocessing
download the [EMDN hierarchy](https://webgate.ec.europa.eu/dyna2/emdn/) as .xlsx and move it to Input/EMDNV2.xlsx 

run EMDN preprocessing with EMDNV2.xslx file present to create EMDN hierarchy in text format

```bash
  python3 PreProcessing/EMDNpreproc.py
  python3 PreProcessing/EMDNgetLeafs.py
  python3 PreProcessing/EMDNget2ndLayer.py
```
format your GMDN input in text format as follows:

```
GMDN ID 1
GMDN Name 1
GMDN Description 1
GMDN ID 2
GMDN Name 2
GMDN Description 2
GMDN ID 3
(...)
```
and put it in a file in the following location PreProcessing/output.txt

if you want to use the sample GMDN input I used, simply 
run /PreProcessing/xmlExtract.py with a subdirectory called "20250304" in /Input with all the [extracted gmdn codes](https://accessgudid.nlm.nih.gov/download) in directory to get GMDN data in text format
(note that u may want to check if your current iteration of the GUDID has 188 parts, as was the case when I extracted its data. If not, change that number in xmlExtract.py in line 5 and 6)

```bash
  python3 PreProcessing/xmlExtract.py
```
#### Mapping
run Main.py to receive translation from GMDN code to EMDN code. You will get 6 possible mapping candidates (The top 5 most likely ones, and one that is reserved for a vague node from EMDN)
Main takes 2 inputs, one being the line (Integer divisible by 3) at which the GMDN ID of the item you want mapped is in PreProcessing/output.txt, and the other being a number between 1 and 5, with which you choose the Model that should be used. They are sorted by the time they generally take to process the input, with 1 running the fastest. 4 usually gives the most accurate output.

Example:

```bash
  python3 Main.py 29403 4
```

Running Main with any particular model the first time will take longer, since the models be downloaded first

If you want to run this script in parallel on an HPC cluster that works with the SLURM queuing system, you can use the slurmRun.sh script to queue all inputs at once, each asking for one dedicated core.

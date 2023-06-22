# pt_anno
high-throughput pt annotation using [chloe](https://chloe.plastid.org/annotate.html)

## instructions
To run this script, you need to have python 3 installed with the requests, pandas, and ipython packages installed. An easy way to manage the software is using conda:  

```
## make a new conda env
conda create --name pt_anno

## activate the env
conda activate pt_anno

## install python and pip
conda install python pip

## install dependencies
pip install requests pandas ipython
```  

Then to run the script the syntax is the following:
```
python annot_pt.py <input>.fa
```

E.g. using the included testfile:
```
python annot_py.py 1embplant_pt.K115.complete.graph1.1.path_sequence.fasta
```

This creates two outputs as follows:
- input.gff
- input.svg

where .gff is chloe annotation of Pt genome using defaults and .svg is diagram of the Pt structure produced by chloe.

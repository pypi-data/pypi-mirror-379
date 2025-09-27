# NoMoCLIP
Interpretable Modeling of RNA–Protein Interactions from eCLIP‑Seq Profiles for Motif‑Free RBPs

## 1. Data availability
[NoMoCLIP_dataset](https://doi.org/10.6084/m9.figshare.30178051)

## 2. Environment Setup
#### 2.1 Create and activate a new virtual environment
```
conda create -n NoMoCLIP python=3.7.16 
conda activate NoMoCLIP
```
#### 2.2 Install the package and other requirements
```
pip install NoMoCLIP
nomoclip install
```
## 3. Process data

#### 3.1 Sequential encoding
```
nomoclip run position_inf  --set_path <PATH_TO_YOUR_DATA>  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY>
```

#### 3.2 Structural encoding
This feature requires the **RNAplfold** tool, which is executed in a **Python 2.7 environment**. Please set the --env parameter to the local RNAplfold environment.
```
nomoclip run structure_inf  --env <NAME_OF_YOUR_ENV>  --set_path <PATH_TO_YOUR_DATA>  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY>
```

#### 3.3 Semantic encoding
```
nomoclip run attention_graph \
  --kmer 1 \
  --set_path <PATH_TO_YOUR_DATA> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --model_type <PATH_TO_YOUR_NLP_MODEL> \ 
  --maxlen 101 \
  --device cuda:1 \
  --device1 cuda:1 \
  --device2 cuda:1 
```
#### 3.4 Functional properties

For this feature, you need to use the [corain](https://github.com/idrblab/corain?tab=readme-ov-file#requirements-and-installment). Please set the --env parameter to the local corain environment.

```
nomoclip run instinct_inf \
  --env <NAME_OF_YOUR_ENV> \
  --base_path <PATH_TO_YOUR_DATA> \
  --set_path <PATH_TO_YOUR_INTERMEDIATE_OUTPUT_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --method_path <PATH_TO_YOUR_CORAIN_DIRECTORY> \ 
  --num 2
```
**Note:** The argument `--num` should be tested with all values in `[2, 3, 5, 7, 10]`.

## 4. Training Process
```
nomoclip run model_train \
  --base_path <PATH_TO_YOUR_DATA_DIRECTORY> \
  --set_path <PATH_TO_YOUR_FEATURE_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --fold 5  \
  --gpu_id 1
```

## 5. Prediction
```
nomoclip run model_predict \
  --set_path <PATH_TO_YOUR_FEATURE_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --model_path <PATH_TO_YOUR_MODEL> \
  --gpu_id 1
```
## 🧬 Motif analysis

Motif extraction requires the installation of the **[MEME Suite](https://meme-suite.org/meme/doc/download.html)** package.

#### 6.1 Sequential motifs

```
nomoclip run seq_motifs \
  --layer <THE_LAYER_OF_MODEL_YOU_SELECTED> \
  --set_path <PATH_TO_YOUR_FEATURE_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --model_path <PATH_TO_YOUR_MODEL> \
  --pwm_path <PATH_TO_YOUR_PWM_FILE> \
  --motif_size 7 \
  --gpu_id 1
```

#### 6.2 Structural motifs

```
nomoclip run structure_motifs \
  --layer <THE_LAYER_OF_MODEL_YOU_SELECTED> \
  --set_path <PATH_TO_YOUR_FEATURE_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --model_path <PATH_TO_YOUR_MODEL> \
  --motif_size 7 \
  --gpu_id 1
```

## 📊 High attention regions

```
nomoclip run high_attention_region \
  --set_path <PATH_TO_YOUR_FEATURE_DIRECTORY> \
  --out_path <PATH_TO_YOUR_OUTPUT_DIRECTORY> \
  --model_path <PATH_TO_YOUR_MODEL> \
  --gpu_id 1
```


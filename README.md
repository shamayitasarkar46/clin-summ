Name: Shamayita Sarkar (student of University of Calcutta)
- **Internship** from 15.06.2024 to 15.07.2024
- **Supervisor**: Prof. Niloy Ganguly (Department of Computer Science and Engineering, IIT Kharagpur)
- Title: **Exploring In-context Learning in Patient Questions Summarization**
- Here we have focused only on the Patient Questions portion from `chq`(Consumer/Patient Health Query) dataset of `data/` folder and selected ICL(In-context Learning) examples for each of the 150 test samples. The ICL examples are taken from the training set(`data/chq/train.jsonl`) for each of 150 test samples(`data/chq/test.jsonl`). Examples are taken in the order of 1,2,4,8,16(i.e. 2^x where x = 0,1,2,....) and in two different methods, these examples are selected: Random & Similar.
- Also, the ROUGE-L scores are evaluated for the Generated summaries of both Similar and Random samples.
-  The code files are stored in `src/code_files` folder and Generated txt files (including output summaries) are stored in `data/chq/generated_files` folder


# Clinical Text Summarization by Adapting LLMs | Nature Medicine

Official implementation from Stanford University<br>
- <b> Title: </b>[Adapted Large Language Models Can Outperform Medical Experts in Clinical Text Summarization](https://arxiv.org/pdf/2309.07430.pdf)<br>
- <b>Authors: </b>[Dave Van Veen](https://davevanveen.com/), Cara Van Uden, Louis Blankemeier, Jean-Benoit Delbrouck, Asad Aali, Christian Bluethgen, Anuj Pareek, Malgorzata Polacin, Eduardo Pontes Reis, Anna Seehofnerova Nidhi Rohatgi, Poonam Hosamani, William Collins, Neera Ahuja, Curtis P. Langlotz, Jason Hom, Sergios Gatidis, John Pauly, Akshay S. Chaudhari 
- <b>Contact: </b>{vanveen} [at] stanford [dot] edu<br>

<img src='data/overview.png'/>


## Datasets
We use this pre-existing open-source datasets which are publicly accessible at the sources cited in our manuscript. Additionally, for datasets which do not require PhysioNet access, we provide our versions in `data/`: 
- `chq`: MeQSum (patient/consumer health questions)


## Models
In addition to proprietary models GPT-3.5 and GPT-4, we adapt the following open-source model available from HuggingFace:
- [Llama-2](https://huggingface.co/meta-llama/Llama-2-7b-hf)

## Code

### Set-up


### Usage

Below is a description of relevant scripts:

- `./main.sh`: Fine-tune open-source models, query, and compute metrics
- `python api/main.py`: Query OpenAI models and compute metrics
    - first enter information for your Azure deployment in `src/constants.py` via `RESOURCE` and `API_KEY`
- `python src/gen_faiss_idx.py`: (new datasets only) Determine set of nearest neighbors training examples for each sample. Alternatively you can sample training examples at random.
- `src/UMLSScorer.py`: Class definition for the MEDCON metric. To implement, follow these steps:
    1) Acquire approval for a [UMLS license](https://www.nlm.nih.gov/research/umls/index.html)
    2) Follow the [UMLS download instructions](https://github.com/Georgetown-IR-Lab/QuickUMLS)
    3) Adapt the provided script, `src/UMLSScorer.py`
    4) Call using the following two lines:
        - `scorer = UMLSScorer()`
        - `medcon_score = scorer(string1, string2)`

## Citation

```
@article{vanveen2024clinical,
  title={Adapted Large Language Models Can Outperform Medical Experts in Clinical Text Summarization},
  author={Van Veen, Dave and Van Uden, Cara and Blankemeier, Louis and Delbrouck, Jean-Benoit and Aali, Asad and Bluethgen, Christian and Pareek, Anuj and Polacin, Malgorzata and Collins, William and Ahuja, Neera and Langlotz, Curtis P. and Hom, Jason and Gatidis, Sergios and Pauly, John and Chaudhari, Akshay S.},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-02855-5},
  url={https://doi.org/10.1038/s41591-024-02855-5},
  published={27 February 2024}
}
```

This folder contains all the code files used in reproducing output summaries based on In-context Learning examples given as input prompt. The following steps are performed: 
1. Firstly,  the ICL examples are selected based on Similar methods (based on Euclidean distance). The codebases are stored in `src/code_files/SIMILAR_ICL_examples_selection` folder.
2. Then the ICL examples are selected on Random methods. The codebases are stored in `src/code_files/RANDOM_ICL_examples_selection` folder.
3. After creating input prompt (including ICL examples), these txt files are stored in `data/chq/generated_files/InputPrompt_for_SIMILAR/final_k_each_similar_samples` folder and  `data/chq/generated_files/InputPrompt_for_RANDOM/final_each_random_samples_k` folder where k = 1,2,4,8,16,32
4. Each of these folder contains 150 txt files ,i.e. 150 input prompt (containing ICL examples) for each of the above cases.
5. Then ZeroShotInference.py file is made to run for each of the folders, to generate Output summaries.
6. The Output summaries are stored in folder `src/code_files/Generated_Summaries_SIMILAR` and `src/code_files/Generated_Summaries_RANDOM` respectively.
7. Finally, the ROUGE scores are evaluated for each of the generated summaries & the performance evaluation is compared with that of Original Clinsumm Codebase.

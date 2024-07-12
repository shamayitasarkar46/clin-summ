This generated_files folder contains all the txt files generated during the project.
- After creating input prompt (including ICL examples), these txt files are stored in `data/chq/generated_files/InputPrompt_for_SIMILAR/final_k_each_similar_samples` folder and  `data/chq/generated_files/InputPrompt_for_RANDOM/final_each_random_samples_k` folder where k = 1,2,4,8,16,32
- The Output summaries are calculated & stored in folder `data/chq/generated_files/Generated_Summaries_SIMILAR` and `data/chq/generated_files/Generated_Summaries_RANDOM` respectively.
-  Finally, the ROUGE scores are evaluated using the code `src/code_files/ROUGE_evaluation_final.ipynb`

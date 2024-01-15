# Team Processing Mapping Coding Task
Welcome to the coding task for the Team Process Mapping project! Before you begin, please make sure to read through the full instructions [here](https://docs.google.com/document/d/1_FZ-N-7Qr9_CXK-fX9vdcMhkaDzmRXyUh1aHEHjL1hs/edit).

## Packages and Requirements
The packages required for you to complete the task are listed in `requirements.txt`. You can use a virtual environment for managing the dependencies associated with this project.

## Your Goal
To complete this assignment, you will need to modify 4 different files:
- features/word_count.py: `count_words(text)`
- features/type_token_ratio.py: `get_word_ttr(text)`
- features/politeness_features.py: `get_politeness_strategies(text)`
- utils/calculate_chat_level_features.py (For calling the functions; you only need to modify `apply_politeness()`).

## Your Deliverables
At the end of Part 2, we will need the following:
- A link to your GitHub cloned repository. This should contain:
  1. Your Python code;
  2. Your Part 2 Reflection (directly edit this README!).
- A copy of your chat-level CSV that contains columns for the features you generated. **Note: this should be reproducible!** We should be able to get the same results by running your code from the GitHub link you submit.

# Part 2 Reflection
Please answer the following four questions:

## 1. Sanity Check
Open up your output CSV and look at the columns you generated for each of the three features. Do the values “make sense” intuitively? Why or why not?
> Yes, these values do "make sense" intuitively. Looking at the first few rows, the output in the num_words and word_TTR column aligns with the anticiipated results. Similarly, the columns generated for the third feature also align with the expected. For instance, the Please column is marked with 1 for rows with messages that contain "please", and 0 for rows without. This is also true for the other columns generated for the third feature such as 1st_person, 2nd_person, Apologizing, etc.

## 2. Testing
How would you implement tests for these features?
> For word_count and word_TTR, I would create test cases with known input messages, manually calculate the expected values and compare with the output of the functions. I would also test for edge cases like empty messages, punctuation, and etc. For politeness_features I would design test cases with specific messages known to trigger certain outputs such as please, apologizing, 1st person, gratitude, etc. Then, I would verify if the generated columns match the expected values. Edge cases may contain a combination of multiple politeness strategies, multiples of one type of strategy, and etc. Additionally, I would implement performance testing on a subset of the data to ensure it runs in a reasonable amount of time.

## 3. Overall Experience
Please provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? Is there anything you would be curious to explore in the future, if you had more time?
> I approached this task by reading through the instructions, ConvoKit documentation, and files to ensure I fully understood the file structure and the requirements. I began with num_words and word_TTR to familiarize myself with the features before moving onto the more difficult politeness_features. One challenge I faced during the task was configuring Python so it was compatible. I had initially set up Python through Anaconda for the Spyder IDE but found that this did not work well for this task. So, I re-downloaded Python but faced several difficulties with PowerShell not recognizing Python, but later resolved this issue by consulting online resources. The third task (politeness_features) also posed a challenge due to its lengthy runtime. Initially, if this was due to a bug in my code or was part of the design. Thus, I'd be interested in exploring how to optimize the performance through further readings into the ConvoKit documentation or refining the process of cleaning up column names and merging with the rest of the features.

## 4. Time Required
How much time did it take you to complete Parts 1 and 2? (Please be honest; we are looking for feedback to make sure the tasks are scoped appropriately.)
> Parts 1 and 2 took roughly 10 hours to complete.

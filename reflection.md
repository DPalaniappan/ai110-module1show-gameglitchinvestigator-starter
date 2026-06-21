# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  When I first ran the game it looked it was a guessing game trying to guessa  number based on a certain range depending on the difficulty that you selected. The Game would then give you attempts and you would have to guess the number in a certain amount of attempts however you can use hints if needed as well. The Hints would tell you if the number your trying to guess is lower or higher than your guess. Addionatlly, there is the difficulties section as well allowing you to change dififculty of the game on a whim.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

   - The first bug I noticed when I started was that the game would give you 7 attempts for normal mode diffuclty right as you started the game, when the diffculty is supposed to be 8 attempts.
   - The second bug I noticed was wwhen changing difficulties at the start the secret key was not being updated to the match the range of numbers based on the difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| When guessing a number lower that seceret key (ex 85) such as 17 | Hint should say Go Higher | Actual behavior is Hint says Go Lower  | Go Lower|                   
| Changing Diffuclty From Normal to Easy and inputting a number inside the range of 20 such as 17 | Should eventually lead to guessing the number in the range 1-20 | The secret key is stuck in the range of 1-100 meaning that it can never be guessed because secret key is outside specfied range | Go Lower or Higher because it is outside the range |
| Guessing wrong guess like 10 9 times on Normal Difficulty whioh has 8 attempts| The game should make user stop being able to enter guesses after they have 0 attempts| attempts does not stop at at 0 and go to negatives allwoing you to go to -1,-2,-3,-4,....  | "none"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

The tool that I used for this project was claude in vscode as that was the one that was provided by codepath for this course and it was built in the vscode, whch means claude was fully integrate into my project and I did not have to copy and paste the code into an llm outside of vscode.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of an AI suggestion that was correct was when I was fixing the High/Low BUg caused by a mistmatch of text based on whether the guess was greater or less than the secret key. While fixing the bug and moving the check_guess to logic_utils.py Claude suggested removing the try-execpt found in check_guess. This suggestion was correct because when looking through the code we already have a parse_guess function that checks if the guess is the correct type and the secret key will always be an int. Verifying that this method wroks amde realize that this check inside check_guess was redundant and not needed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an AI suggestion that was slightly incorrect or misleading was when I was fousing on my second bug, which was when the diffculties changed the secret key would not update based on the range as the secret was locked from being updated due to having a check saying to only udpate secret key if there is no variable in the ession. During implementing the fix Claude suggested making the number of attempts for that session equal to 1. However, this sugggestion was incorrect because changing difficulties results in a change of the secret keys, which means that it is a new game and nota continuation of the one from the previous difficulty. So I suggested that Claude was wrong and that the attempts should be reset to 0 as changing difficulties would be treated as starting a new game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether a bug was really fixed once I tested the bug myself manually mainly as I felt like some bugs seemed obvious to test manually as I knew pytest implementation would be troublesome to test. An example would be the bug on the session state changing the secret key based on selecting difficulty vs checking if guess outputed to high or too low based on if it was higher or lower than secret. Testing selecting difficulty manually was better because it was quick and I could see that it would work or not and there was no real function in logic_utils that helped me here. However, for checking the the diffculty was properly checking if it was higher or lower depended upon the funnction chekc guess which returned outcomes and results making it easier to test with pytests rather than manually. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One test that I ran manually was testing if the number attempts was wrokign properly and not going into the negatives. What it showed me during that test was that my code was working properly, but I realized that the UI was updating before the guess_submit handler was updating attempts. THis helped me fix a bug with the UI making sure that the UI only updated after I handled submitting the guess and not before it. 


- Did AI help you design or understand any tests? How?

Yes AI helped me design the tests that I were not good to do manually. Usually I would prompt claude into writing me a basic test case that checked if the bug that I prompted it to find and fix while also makign sure to check if it was going in the right direction. I made sure that tests acutally tested the acutal functions in logic_utils.py. I had some cases where if I wanted to test something in pytest Claude would create a new function that kinda acted like what I was testing, but it was not really testing what was acutally in streamlit game. Thats when I realized that I needed claude to create tests based only on the functions that it coould test in logic_utils as anything nto involving those functions could be tested manually without the need of AI.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

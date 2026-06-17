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
| Changing Diffuclty From Normal to Easy and inputting a number inside the range of 20 such as 17 | Should eventually lead to guessing the number in the range 1-20 | The secret key is stuck in the range of 1-100 meaning that it can never be guessed because secret key is outside specfied range | "none" |
| Guessing wrong guess like 10 9 times on Normal Difficulty whioh has 8 attempts| The game should make user stop being able to enter guesses after they have 0 attempts| attempts does not stop at at 0 and go to negatives allwoing you to go to -1,-2,-3,-4,....  | "none"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

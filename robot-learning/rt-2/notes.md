## RT-2
I loaded in a mock version of RT-2 (since the weights aren't public) into agent-lab/rt-2 

They express the actions as text tokens and incorporate them directly into the training set of hte model in the same way as natural language tokens. 
- Thus introducing the concept of vision-language-action models (VLA)

represent robot actions as text tokens, so controlling a robot becomes just another "answer the question" task for an LLM.

Closed Loop Control: the robot is constantly re-evaluating its environment and adjusting tis actions in real-tjme based on new visual feedback, rather than blindly executing a pre-planned set of movements.

Oh ok so basically instead of training a separate diffusion transformer or complex continuous action head, RT-2 treats robot actions as discrete text tokens within a unified sequence-to-sequence framework.

They categorized the emergent properties of RT-2 into: symbol understanding, reasoning and human recognition.
- They evaluated TWO variants of RT-2 

RT-2 Trained on top of PaLM-E (12B Parameters)
RT-2 Trained on top of PaLI-X (55B Parameters)

Do As I Can, Not As I Say (Google, 2022): https://arxiv.org/pdf/2204.01691 
SayCan was a robotic framework developed by Google that used a large language model to break down high-level instructions into tasks, combining them with physical affordance scores to ensure the robot chose actions that were both useful and physically possible. (April 4th, 2022)
- No additional learning at inference time of course (fixed LLM and Value Functions)
- "Say": Given your high-level instruction, the language model scores the pre-determined list of available low-level skills to see which ones make logical sense as the next step.
- "Can": For those same skills, the learned value functions look at the robot's current physical state/environment and output a probability score representing how likely each skill is to successfully execute right now.
- SayCan:  SayCan multiplies the LLM's probability score by the value function's score for each skill, and deterministically picks the highest-scoring skill ($arg \max$) to execute next.

ohh so the value function is just outputing how FEASABLE each action is given the image, NOT how actually VALUABLE each action is for achieving the goal.

A few-shot prompt is a prompting technique where you give an AI model a few examples of what you want it to do before asking it to solve a new problem.

Instead of just telling the model what you want in plain words (which is called zero-shot prompting), you show it patterns, formatting styles, or desired behaviors through a handful of demonstrations (hence "few-shot").


Essentially SayCan is just predicting the next most likely words in a sentence based on the prompt. It's basically a giant text-prediction model hitched up to a physical validation filter!


What was RT-1 Architecture again? (Robotics Transformer 1)
- Model Type: A 35M-parameter Transformer-based model designed specifically for robotic manipulation.
- It takes robot camera images and natural language instructions, tokenizes the continuous robot actions into discrete bins (0-255), and predicts the action sequence directly using a standard Transformer backbone

Core Definition: RT-1 (Robotics Transformer 1) is a low-level robotic policy and network architecture designed to map high-dimensional visual observations (camera images) and natural language instructions directly into executable robot motor commands (arm movements, base motion, and mode switches).








later learn how ViT's work. 

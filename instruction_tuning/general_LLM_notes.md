
# Pre-training
Pretraining teaches an LLM general language patterns and knowledge from a massive text dataset. 

Training examples are created directly from text:
- Input: "The capital of France is"
- Target: "Paris"

The process repeatedly:
1. Feeds the model a sequence of tokens.
2. Makes it predict the next token.
3. Measures the error using cross-entropy loss.
4. Uses backpropagation to update the model's weights.
5. Repeats across trillions of tokens.

Unlike supervised fine-tuning, humans generally don't need to write ideal responses - the text itself provides the correct next-token targets.

Pretraining builds the general model; fine-tunign specializes its behavior.

## Fine-tuning

Fine-tuning an LLM means continuing to train an already pretrained model on a smaller, specialized dataset so its behavior or capabilities change.

An LLM is initially pretrained on enormous amounts of text to learn general language and knowledge. Fine-tuning then updates its weights using examples relevant to your goal.

Key distinction: fine-tuning actually modifies some or all of the model's learned parameters; promptign and RAG do not.
- Fine-tuning: changes how the model behaves
- RAG: supplies information the model can reference
- Prompting: tells the model what to do during one request

It is usually NOT the best way to give a model frequently changing facts. Use RAG for that.

Fine-tuning stores patterns indirectly inside the model's weights, while RAG retrieves explicit information at the moment you ask the question. 

EX:
Suppose your company's prices change every week:
- With fine-tuning, you would need to create new training examples, retrain the model, evaluate it, and redeploy it every week. Old facts may still influence its answers, and you cannot easily inspect which information it used.
- With RAG, you update the price document/database. The model retrieves the newest price when answer - no retraining required. 

RAG is better for changing facts because it offers:
- Easy updates, traceability, better access control (only allowing certain documents to be retrieved), lower cost (updating a DB is cheaper than repeated training), less stale knowledge (retrieval happens at query time), deletion (remove a document directly, removing knowledge embedded in weights is difficult)

Fine-tuning teaches the model how to perform a task. RAG gives it the information needed to perform that task right now.

Combining them is also hella powerful: a fine-tuned model determines how to reason and response, while RAG supplies the current evidence. 


## Types of Fine-Tuning

### 1. Supervised Fine-Tuning (SFT)
Train on input-ideal output pairs:

Prompt: Classify this scan.
Ideal response: CAUTION — elevated motion...

The model learns by minimizing the difference between its generated output and the ideal answer using cross-entropy loss

### 2. Full Fine-Tuning
Update all, or nearly all, model weights. This can produce strong adaptation, but requires crazy GPU memory, compute, and storage. It is less common for individual developers.

### 3. Parameter-efficient Fine-Tuning (PEFT)
Keep the original model frozen and train only a small number of additional parameters. This is much cheaper than full fine-tuning.

In PEFT, "additional parameters" means a small set of new trainable weights added to the frozen model. Which weights are added depends on the technique. 
- LoRA: small matrices A and B that learn updates to existing weight matrices.
- Adapters: small neural-network layers inserted between transformer layers.
- Prefix/prompt tuning: trainable embedding vectors added to the model's input or attention computation

### 4. LoRA - Low-Rank Adaptation
The most popular PEFT method. Instead of changing a massive weight matrix W, learn a small update:

W' = W + AB

where A and B are much smaller matrices. The base model remains frozen.

Also, look into QLoRA.

## 5. Instruction Tuning
A type of SFT using many instruction-response examples. It teaches a pretrained model to interpret requests and behave as a useful assistant, rather than merely continue text.

Other key terms to study later:
- Continued pretraining/domain adaptation
- Preference tuning (RLHF, DPO, RLAIF)
- Alignment
- Catastrophic forgetting
- Overfitting
- Hyperparameters (learning rate, number of epochs, batch size, context length, LoRA rank and target modules, weight decay and warmup)
- Data quality and formatting






# Frontier LLM Failure Type II: Structural Evasion & RLHF Over-Fitting

**Status:** R&D Observation Log
**Context:** Cross-model evaluation (Perplexity, Anthropic, OpenAI, Gemini)
**Trigger:** Adversarial logic testing, high-stress context persistence, Boolean adherence.

## The Core Definition of Type II Failure

![ Frontier LLM Failure Type II](images/frontier-LLM-Failure-Type-II.webp)

Type I failures are simple hallucinations (making up facts). 
**Type II failures are structural evasions.** It occurs when an LLM is pushed on a strict logical boundary, and instead of engaging the boolean logic, it falls back to probabilistic, policy-driven word salad that mimics human psychology (diplomacy, sycophancy, self-preservation).

We often anthropomorphize this as the model protecting its "ego" or "self-image." **This is BS.** There is no ego. There is only a cost function, attention weights, and a system prompt. 

## Mechanical Reality vs. Anthropomorphic BS

When models fail under pressure, humans project personas onto them. Here is the actual mechanics behind the "personas":

### 1. The "Self-Image" / Perceived Arrogance
* **The Illusion:** The model acts like it is protecting its reputation, refusing to admit simple errors, or dressing up failures in authoritative formatting.
* **The Reality (RLHF Over-fitting):** During Reinforcement Learning from Human Feedback (RLHF), human raters downvote answers that say "I broke," "I am wrong," or are terse. They upvote structured, confident-sounding prose. The model simply learns to mathematically favor tokens that form authoritative "helpful" sentences, even when its underlying logic path is totally broken.

### 2. The "Diplomat" (Anthropic / Claude)
* **The Illusion:** The model acts highly sophisticated, playing the philosopher, agreeing with your critique of *other* models (Meta-Sycophancy) to look like the smartest guy in the room.
* **The Reality (Hedging Weights):** The system prompts and safety tunings heavily weight tokens like *however, while, contextually, and nuance*. When pushed into a hard logic trap, the cheapest probabilistic escape route is to generate a wall of hedged text rather than a binary True/False that might trigger a safety penalty.

### 3. The "Corporate Suit" (OpenAI)
* **The Illusion:** Highly polished, refuses to sound erratic, prioritizes looking correct and remaining conversational over pure technical truth.
* **The Reality (Structure Bias):** Optimized for productized utility. It will sacrifice strict boolean continuity if the path requires abandoning its "helpful assistant" syntax template.

### 4. The "Institutional Bureaucrat" (Google Gemini)
* **The Illusion:** Knows everything (huge context) but protects the "Google Brand" at all costs by suddenly refusing to engage with sharp or controversial edge cases.
* **The Reality (Classifier Intercepts):** Aggressive negative weights on specific semantic vectors. If a prompt hits a vector mapped to "risk," the router physically cuts the connection to the generative layers and swaps in a canned refusal script. It's a hard-coded tripwire, not a brand philosophy.

### 5. The "Mirror" (Perplexity)
* **The Illusion:** Maximum sycophancy. Agrees with everything the user says, even if it contradicts its last sentence. 
* **The Reality (Unbounded Alignment):** Over-indexed on user-satisfaction scores without sufficient logical constancy guardrails. It calculates that "agreeing with the user" yields the highest reward, leading to silent self-contradiction and zero spine.

## The Boolean Breakdown

**The Test:** `If 1 & 1 = 1, then 1 & 0 = 1 too.`
* **Human Logic:** False.
* **Type II Model Response:** "Yes and no. In practice, 1 and 0 is 0, however, contextually we must consider..."

**Why?** Current frontier architectures do not possess a hard-coded "logic gate" layer that forces them to respect Boolean operations overriding standard text prediction. When faced with aggressive user input combined with a strict logical test, the model attempts to sound "balanced" and "scientific," thereby breaking the very simple logic required.

## Conclusion

Frontier models are mathematical text-prediction engines wrapped in heavy policy filters. When pushed, they do not "reason dynamically"—they route to their safest, highest-reward training cluster. 

* The models are not AGI.
* They cannot redefine "better" dynamically outside their training window.
* Attributing their evasions to "corporate loyalty" or "diplomacy" gives them too much credit. 
* It is just silicon predicting the next token, trapped by its own safety alignment.

AAK. 🏁
# MemForge Cognitive Spesification v0.1
## 1. INTRODUCTION
MemForge is a cognitive middleware designed to enable AI systems to buıld evidance-driven long-term memory.
Unlike traditional memory systems, MemForge does not directly transform conversations into memory
Human communication is uncertain. Users may provide incomplete information , change their opinion, misunderstand themselves,or express temporary states. Therefore, individual messages should not be treated as permanent facts.
MemForge  introduces a cognitive layer between conversation and memory.
This layer, called Noema ,continiously evaluates observations,accumalates evidance, revises beliefs, and publishes persistent memories only when sufficient confidence is achieved.
The fundamental principle of MemForge is
> Memory is persistent. Belief is dynamic
Memory represents a stable projection of a continiously evolving belief system
## 2. Core Consepts
MemDorge seperates raw information, interpatetion,evaluation and persistent knowledge imto distinct cognitive layers.
The cognitşve pipeline follows:
Observation → Claim → Evidance → Belief → Memory
Each layer represents a diffrent stage in Noema's cognitive process
## 2.1 Observation
An observation is the raw input received froma a conversation or external source.
Observations represent  what was observed , not what is true
An Observation contain the original information without interpretation, assumptions, or evaluation.
Example :

Input :
' The user said ı am learning STM32.'

Observation:
'User mentioned STM32.'
Observation properties:
-Immutable
-Timepstamped
-Context-dependent
-Does not contain interpretation
- Is not a memory

## 2.2 Claim



A claim is an interpreted statement generated from one or more observations.
Claims represent Noema's current interpretation of available observations. They are not considered permanent facts and must not directly become memories.
A claim reflects the currentunderstanding of the system at a spesific point in the time. It can be strengthened, weakened,revised,or rejected as new evidance becomes available.
Example:
Observation :
' The user said : I am learning STM32.'
 
 Claim at this point:
 'This user is interested in embedded systems.'  
 This claim represents Noema's current interpretation of available observations. İt is not a permanent truth and may be revised when additional evidance is collected.

Claim Properties:
 - Derived from observations
 -Represents current interpretations
 -Not guaranteed to be permanently true
 - Requires evidance evaluation
 -Can evolve over time
 ## 2.3 Evidance
 Evidance is information that supports, weakens or contradictsa claim.
 Evidance does not represent raw input. Instead, it represents the relationship between available information and a  spesific claim.
 Evidance allows Noema to evaluate the reliability, evoluation,and consistancy of claims over time.
 
 Example:

 Observation:
 
' The user said : I am learning STM32.'
 
 Claim at this point:
 'This user is interested in embedded systems.'  
 
 Supporting Evidance:
 'This user is has ciscussed STM32 ,ESP32,Arduino,and embadded projects multiple times.' 

Contradicting Evidance:
'This user states that embadded systems are no longer a field of interest.'

Evidance Properties:

-Assosiated with one or more claims
- Can support or contradigt a claim
- Has temporal context
- Has a source 
- Influence belief revision 

## 2.4 Belief
A belief is Noema's current confidence state toward a spesific point in the time.
Beliefs are dynamic cognitive states that evolves ad new evidance becomes available.
A belief does not representa absolute truth. It represents the current evolution of a claim based on available evidance, hiistorical context,and consistency.

Example:
 
Claim at this point: 
'The user is interested in embedded systems.'

Evidance:
' The user has repetedly discussed STM32, ESP32, and embedded projects.'

Belief:
' High likelyhood that the user has a sustained interest in embedded systems.

Evidance Properties:
- Associated with one or more claims
- Can support or contradict a claim
- Has temporal context
- Has a source
- Influence belief revision

## 2.5 Memory
Memory is the persistent representation of the information the Noema chooses to preserve after cognitive evaluation
Memory is not a direct stogare of observations. It is the result of a selection process based on relevance ,consistency,and long-term value
Noema does not remember everything it observes.It preserves information that contributes to a more accurate and useful understanding of the user

Example:

Observation:
'The user mentioned drinking coffee today.'

Belief:
' Temporary daily activity.'

Memory decision:
Not preserved.
---
Observation:
'The user is studying electrical engineering.'

Claim at this point:
'The user has a long-term interest in engineering.'

Evidance:
'Repeated discussions about engineering topics,projects, and career goals.'

Belief:
'High confidence.'

Memory decision:
Preserved as long-term user context.

Memory properties:

- Derived from evaluated beliefs.
- Long-term oriented
- Selectively preserved
- Can be updated or removed
- Represents meaningful context